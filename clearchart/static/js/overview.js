// overview.js
// Makes the Overview page interactive:
//   click a condition tab -> open its mini tab + light up the body model.

(function () {
  "use strict";   // asks JavaScript to be stricter, so typos become errors

  // ---- Step 1: grab the page elements we need ----
  const tabs = Array.from(document.querySelectorAll(".condition-tab"));
  const regions = Array.from(document.querySelectorAll(".body-svg .region"));
  const caption = document.getElementById("model-caption");
  const defaultCaption = caption.textContent;      // remember the starting message

  // ---- Step 2: small helper functions ----

  // Find the mini tab that belongs to a tab button.
  // The button's aria-controls attribute holds the id of its panel.
  function panelFor(tab) {
    return document.getElementById(tab.getAttribute("aria-controls"));
  }

  // Light up ONE region of the body (and turn all the others off).
  // Passing null turns everything off.
  function highlight(regionName) {
    regions.forEach(function (region) {
      region.classList.toggle("highlight", region.dataset.region === regionName);
    });
  }

  function closeTab(tab) {
    tab.setAttribute("aria-expanded", "false");
    panelFor(tab).hidden = true;
  }

  // Open one tab. First close all of them, so only one is open at a time.
  function openTab(tab) {
    tabs.forEach(closeTab);
    tab.setAttribute("aria-expanded", "true");
    panelFor(tab).hidden = false;
    highlight(tab.dataset.region);                 // reads data-region="..."
    caption.textContent = "Highlighted area: " + tab.dataset.regionLabel;
  }

  function closeAll() {
    tabs.forEach(closeTab);
    highlight(null);
    caption.textContent = defaultCaption;
  }

  // ---- Step 3: react to clicks ----
  tabs.forEach(function (tab) {
    tab.addEventListener("click", function () {
      const isOpen = tab.getAttribute("aria-expanded") === "true";
      if (isOpen) {
        closeAll();            // clicking an open tab closes it
      } else {
        openTab(tab);
      }
    });
  });

  // ---- Step 4: open a condition straight from a link ----
  // The home page links to addresses like /overview#fractured-wrist.
  // The text after the # is the condition id.
  function openFromHash() {
    const id = window.location.hash.slice(1);      // drop the "#"
    if (!id) {
      return;
    }
    const tab = tabs.find(function (t) {
      return t.dataset.conditionId === id;         // reads data-condition-id="..."
    });
    if (tab) {
      openTab(tab);
      tab.scrollIntoView({ behavior: "smooth", block: "nearest" });
    }
  }

  openFromHash();                                  // when the page first loads
  window.addEventListener("hashchange", openFromHash);   // and if the # changes later
})();
