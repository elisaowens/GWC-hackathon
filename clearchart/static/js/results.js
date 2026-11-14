// results.js
// Shows a pop-up when you hover over (or tab to) a highlighted medical word.
//   - normal words: a short definition
//   - body-part words: the definition PLUS a mini picture of the area

(function () {
  "use strict";

  // ---- Step 1: grab the things we need ----
  // The glossary was placed in the page as JSON data by results.html.
  const glossary = JSON.parse(document.getElementById("glossary-data").textContent);
  const tooltip = document.getElementById("tooltip");
  const bodyTemplate = document.getElementById("body-template");
  const terms = Array.from(document.querySelectorAll(".jargon"));
  let activeTerm = null;           // the word whose pop-up is showing right now

  // ---- Step 2: make a mini body picture with one region lit up ----
  function makeMiniBody(regionName) {
    const original = bodyTemplate.querySelector(".body-svg");
    if (!original) {
      return null;
    }
    const svg = original.cloneNode(true);          // true = copy everything inside too
    svg.classList.add("mini-body");
    svg.setAttribute("aria-hidden", "true");       // the text already says it all

    svg.querySelectorAll(".region").forEach(function (region) {
      const isMatch = region.dataset.region === regionName;
      region.classList.toggle("highlight", isMatch);
      if (isMatch && region.dataset.view) {
        svg.setAttribute("viewBox", region.dataset.view);   // zoom in on the area
      }
    });
    return svg;
  }

  // ---- Step 3: fill the pop-up with content ----
  // We use textContent (not innerHTML) so glossary text can never inject HTML.
  function fillTooltip(entry) {
    tooltip.textContent = "";                      // empty it first

    const title = document.createElement("strong");
    title.className = "tooltip-title";
    title.textContent = entry.label;
    tooltip.appendChild(title);

    if (entry.kind === "anatomy") {
      const picture = makeMiniBody(entry.region);
      if (picture) {
        tooltip.appendChild(picture);
      }
    }

    const description = document.createElement("p");
    description.textContent = entry.text;
    tooltip.appendChild(description);
  }

  // ---- Step 4: put the pop-up next to the word ----
  function positionTooltip(term) {
    // park it at the top-left so we can measure its real size
    tooltip.style.left = "0px";
    tooltip.style.top = "0px";

    const wordBox = term.getBoundingClientRect();  // where the word is on screen
    const tipBox = tooltip.getBoundingClientRect();
    const margin = 8;

    let left = wordBox.left;
    let top = wordBox.bottom + margin;             // default: just below the word

    // keep it inside the window sideways
    if (left + tipBox.width > window.innerWidth - margin) {
      left = window.innerWidth - tipBox.width - margin;
    }
    if (left < margin) {
      left = margin;
    }
    // not enough room below? show it above the word instead
    if (top + tipBox.height > window.innerHeight - margin) {
      top = wordBox.top - tipBox.height - margin;
    }
    if (top < margin) {
      top = margin;
    }

    tooltip.style.left = left + "px";
    tooltip.style.top = top + "px";
  }

  // ---- Step 5: show and hide ----
  function show(term) {
    const entry = glossary[term.dataset.term];     // reads data-term="..."
    if (!entry) {
      return;                                      // unknown word: do nothing
    }
    activeTerm = term;
    fillTooltip(entry);
    tooltip.hidden = false;                        // must be visible BEFORE we measure it
    term.setAttribute("aria-describedby", "tooltip");
    positionTooltip(term);
  }

  function hide() {
    tooltip.hidden = true;
    if (activeTerm) {
      activeTerm.removeAttribute("aria-describedby");
      activeTerm = null;
    }
  }

  // ---- Step 6: listen for the mouse and keyboard ----
  terms.forEach(function (term) {
    term.addEventListener("mouseenter", function () { show(term); });
    term.addEventListener("mouseleave", hide);
    term.addEventListener("focus", function () { show(term); });   // keyboard users (Tab key)
    term.addEventListener("blur", hide);
    term.addEventListener("click", function () { show(term); });   // phones: tap to show
  });

  // tap anywhere else (or press Escape) to close
  document.addEventListener("click", function (event) {
    if (!event.target.closest(".jargon")) {
      hide();
    }
  });
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      hide();
    }
  });

  // The pop-up is fixed to the WINDOW, not the page. So if the page scrolls
  // while a pop-up is open (for example when the Tab key scrolls a word into
  // view), move the pop-up so it stays next to its word.
  window.addEventListener("scroll", function () {
    if (activeTerm) {
      positionTooltip(activeTerm);
    }
  }, true);
})();
