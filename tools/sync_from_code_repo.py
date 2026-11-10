#!/usr/bin/env python3
"""Sync the mirrored parts of this site with the GRABNES code repository.

The source is always the ``main`` branch of https://github.com/gjung-group/grabnes
(a shallow clone into a temporary directory, via GitPython). ``--src PATH`` points
to an existing checkout instead, for offline work; its HEAD commit is read, the
working tree is not.

Usage:
    uv run python tools/sync_from_code_repo.py            # apply
    uv run python tools/sync_from_code_repo.py --check    # report only, exit 1 on drift

Mirrored automatically (verbatim copies of tracked files):
    docs/development/**.md (except README.md)  -> development/
    docs/user-guide/*.md                        -> user-guide/   (input-keys.md is
                                                   generated upstream: copied, not edited)
    examples/<ex>/ (all but reference/)         -> assets/downloads/examples/<ex>/
    examples/<ex>/reference/*.png               -> assets/images/examples/
    lanczosKuboCode/Src                         -> reference/units.md, reference/api/ (gen_api_reference.py)

Hand-written pages that are derived from upstream sources cannot be synced
automatically. Their upstream git object hashes are recorded in
tools/sync-state.json and any change is reported as MANUAL:
    docs/development/README.md        -> development/index.md
    docs/theory/tapw-procedure.tex    -> theory/tapw-procedure.md
    examples/README.md, examples/*/README.md -> examples/*.md
    tools/input/{gendata,parser,gendata_schema}.py -> user-guide/yaml-json-input.md
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from git import Repo

REPO_URL = "https://github.com/gjung-group/grabnes.git"
ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "tools" / "sync-state.json"
SRC_UNITS = "lanczosKuboCode/Src"
WATCH = [
    "docs/development/README.md",
    "docs/theory/tapw-procedure.tex",
    "examples/README.md",
    "tools/input/gendata.py",
    "tools/input/parser.py",
    "tools/input/gendata_schema.py",
]

# Directories fully managed by this script (files not upstream any more are removed),
# except the hand-written index pages.
MANAGED = {
    "development": {"index.md"},
    "user-guide": {"index.md", "yaml-json-input.md"},
    "assets/downloads/examples": set(),
    "assets/images/examples": set(),
}


def plan(repo: Repo) -> dict[Path, object]:
    """Map every destination file to the upstream blob that provides it."""
    blobs = {b.path: b for b in repo.head.commit.tree.traverse() if b.type == "blob"}
    files: dict[Path, object] = {}

    for path, blob in blobs.items():
        parts = path.split("/")
        if path.startswith("docs/development/") and path.endswith(".md") and path != "docs/development/README.md":
            files[ROOT / "development" / path.removeprefix("docs/development/")] = blob
        elif path.startswith("docs/user-guide/") and path.endswith(".md"):
            files[ROOT / "user-guide" / path.removeprefix("docs/user-guide/")] = blob
        elif parts[0] == "examples" and len(parts) >= 3 and parts[2] != "reference":
            files[ROOT / "assets/downloads/examples" / "/".join(parts[1:])] = blob

    pngs: dict[str, list[str]] = {}
    for path in blobs:
        parts = path.split("/")
        if parts[0] == "examples" and len(parts) == 4 and parts[2] == "reference" and path.endswith(".png"):
            pngs.setdefault(parts[1], []).append(path)
    for ex, paths in pngs.items():
        for path in paths:
            name = f"{ex}.png" if len(paths) == 1 else f"{ex}_{Path(path).stem}.png"
            files[ROOT / "assets/images/examples" / name] = blobs[path]
    return files


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", help="existing checkout of the code repo (default: fresh clone of main)")
    ap.add_argument("--check", action="store_true", help="report drift without writing; exit 1 if any")
    a = ap.parse_args()

    with tempfile.TemporaryDirectory() as tmp:
        repo = Repo(a.src) if a.src else Repo.clone_from(REPO_URL, Path(tmp) / "grabnes", branch="main", depth=1)
        commit = repo.head.commit.hexsha
        print(f"source: {a.src or REPO_URL} @ {commit[:7]}")
        tree = repo.head.commit.tree

        files = plan(repo)
        changed = [d for d, b in sorted(files.items()) if not d.exists() or d.read_bytes() != b.data_stream.read()]
        removed = sorted(
            f
            for d, keep in MANAGED.items()
            if (ROOT / d).exists()
            for f in (ROOT / d).rglob("*")
            if f.is_file() and f not in files and f.relative_to(ROOT / d).as_posix() not in keep
        )

        # hand-written pages and the generated reference: compare recorded object hashes
        state = json.loads(STATE.read_text()) if STATE.exists() else {"trees": {}}
        watch = WATCH + sorted(
            b.path for b in tree["examples"].traverse() if b.type == "blob" and b.path.count("/") == 2
            and b.path.endswith("/README.md")
        )
        hashes = {p: tree[p].hexsha for p in watch}
        hashes[SRC_UNITS] = tree[SRC_UNITS].hexsha
        manual = [p for p in watch if state["trees"].get(p) != hashes[p]]
        units_stale = state["trees"].get(SRC_UNITS) != hashes[SRC_UNITS] or not (ROOT / "reference/units.md").exists()

        for f in changed:
            print(f"  update      {f.relative_to(ROOT)}")
        for f in removed:
            print(f"  remove      {f.relative_to(ROOT)}")
        if units_stale:
            print("  regenerate  reference/units.md")
        for p in manual:
            print(f"  MANUAL      upstream {p} changed (or no baseline): review the page derived from it")

        drift = bool(changed or removed or units_stale or manual)
        if not drift:
            print("up to date")
            return 0
        if a.check:
            print("drift found (check mode, nothing written)")
            return 1

        for dst in changed:
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(files[dst].data_stream.read())
        for f in removed:
            f.unlink()
        for d in MANAGED:  # drop emptied directories
            base = ROOT / d
            for sub in sorted(base.rglob("*"), reverse=True) if base.exists() else []:
                if sub.is_dir() and not any(sub.iterdir()):
                    sub.rmdir()
        if units_stale:
            # gen_api_reference.py reads sources from disk, so give it the checkout
            subprocess.run(
                [sys.executable, str(ROOT / "tools/gen_api_reference.py"), "--src", str(Path(repo.working_dir) / SRC_UNITS)],
                check=True, cwd=ROOT,
            )
        STATE.write_text(json.dumps({"commit": commit, "trees": hashes}, indent=2, sort_keys=True) + "\n")
        print(f"synced to {commit[:7]}; review MANUAL items and run the -W build")
    return 0


if __name__ == "__main__":
    sys.exit(main())
