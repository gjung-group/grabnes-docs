// GRABNES site script.
// Long identifiers in table cells (input keys such as
// Interlayer.ChangeLatticeParameterForSrivaniModel, Fortran names with
// underscores) get line-break opportunities after "." and "_", so narrow
// table columns wrap them at a natural point instead of in mid-word.
document.addEventListener("DOMContentLoaded", () => {
  // a "." or "_" between word characters: Bands.NumPoints, calc.F90, mem_gen
  // (not the dots of .false. or of a sentence end)
  const pattern = /(?<=\w)([._])(?=[A-Za-z])/g;
  for (const cell of document.querySelectorAll("article table td")) {
    const walker = document.createTreeWalker(cell, NodeFilter.SHOW_TEXT);
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    for (const node of nodes) {
      if (node.parentElement.closest(".math, mjx-container, script")) continue; // leave TeX alone
      if (!pattern.test(node.nodeValue)) continue;
      pattern.lastIndex = 0;
      const parts = node.nodeValue.split(pattern);
      const frag = document.createDocumentFragment();
      for (const part of parts) {
        frag.append(part);
        if (part === "." || part === "_") frag.append(document.createElement("wbr"));
      }
      node.replaceWith(frag);
    }
  }
});
