document.addEventListener("DOMContentLoaded", function () {
  function renderAll() {
    // Everything carries raw $...$ / $$...$$ delimiters: article bodies
    // (.unit-body), plain-text fields (descriptions / quotes), and info
    // pages. The auto-render extension typesets them all in place; it
    // skips <code>/<pre> by default, so code spans are left untouched.
    if (window.renderMathInElement) {
      document
        .querySelectorAll(
          ".unit-body, .unit-quote, .unit-entry-desc, .info-page",
        )
        .forEach(function (el) {
          renderMathInElement(el, {
            delimiters: [
              { left: "$$", right: "$$", display: true },
              { left: "$", right: "$", display: false },
            ],
            throwOnError: false,
          });
        });
    }
  }
  if (window.katex && window.renderMathInElement) {
    renderAll();
  } else {
    window.addEventListener("load", renderAll);
  }
});
