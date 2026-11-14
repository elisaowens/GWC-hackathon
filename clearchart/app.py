"""
app.py
======
The "brain" of the website. It does three jobs:
  1. Creates the Flask app.
  2. Defines the three pages (called "routes").
  3. Teaches the templates a trick: automatically highlight medical words.

Run it with:   python app.py
Then open:     http://127.0.0.1:5001
"""

import re                                   # "regular expressions": powerful text searching
from datetime import datetime               # to show today's date on the home page

from flask import Flask, render_template    # Flask itself + the function that fills in HTML pages
from markupsafe import Markup, escape       # tools that keep HTML safe (explained below)

import data                                 # our own file: data.py


# ----------------------------------------------------------------------
# STEP 1: create the app
# __name__ tells Flask where this file is, so it can find the "templates"
# and "static" folders sitting next to it.
# ----------------------------------------------------------------------
app = Flask(__name__)


# ----------------------------------------------------------------------
# STEP 2: the medical-word highlighter
#
# Goal: turn  "Your hemoglobin is low"  into
#       'Your <span class="jargon" data-term="hemoglobin">hemoglobin</span> is low'
# The CSS then underlines the span and the JavaScript shows the pop-up.
# ----------------------------------------------------------------------

# 2a. Build a lookup table: every spelling -> the glossary key it belongs to.
#     Example: "kidney" -> "kidneys",  "kidneys" -> "kidneys",  "ldl" -> "ldl cholesterol"
def build_term_lookup():
    lookup = {}
    for key, entry in data.GLOSSARY.items():
        lookup[key.lower()] = key
        for alias in entry.get("aliases", []):
            lookup[alias.lower()] = key
    return lookup


TERM_LOOKUP = build_term_lookup()

# 2b. Build ONE search pattern that finds any of those spellings.
#     - sorted longest-first, so "ldl cholesterol" is tried before "cholesterol"
#     - re.escape makes sure characters like "-" are treated as plain text
#     - \b means "word boundary", so "heart" does NOT match inside "heartbeat"
#     - IGNORECASE means "Hemoglobin" and "hemoglobin" both match
spellings_longest_first = sorted(TERM_LOOKUP, key=len, reverse=True)
JARGON_PATTERN = re.compile(
    r"\b(" + "|".join(re.escape(word) for word in spellings_longest_first) + r")\b",
    re.IGNORECASE,
)


# 2c. The filter itself. Templates call it like:  {{ some_text | jargon }}
#     SAFETY NOTE: we escape() every normal piece of text, which turns
#     characters like < and > into harmless symbols. That way, if text ever
#     contains HTML, it can't break the page. Only OUR <span> is real HTML,
#     and Markup(...) is how we tell Flask "this part is trusted".
@app.template_filter("jargon")
def mark_jargon(text):
    text = str(text)
    pieces = []          # we collect the finished output pieces here
    last_end = 0         # where the previous match finished

    for match in JARGON_PATTERN.finditer(text):
        # the normal text before this medical word
        pieces.append(escape(text[last_end:match.start()]))

        # the medical word, wrapped in a span
        key = TERM_LOOKUP[match.group(0).lower()]
        pieces.append(
            Markup('<span class="jargon" data-term="{}" tabindex="0">{}</span>').format(
                key, match.group(0)
            )
        )
        last_end = match.end()

    # whatever text is left after the last medical word
    pieces.append(escape(text[last_end:]))
    return Markup("").join(pieces)


# ----------------------------------------------------------------------
# STEP 3: the pages
# @app.route("/...") says "when someone visits this address, run the
# function underneath". The function name (home, overview, results) is
# also what templates use in url_for("home").
# render_template fills a file from the templates/ folder with our data.
# ----------------------------------------------------------------------
@app.route("/")
def home():
    now = datetime.now()
    today = f"{now:%A, %B} {now.day}"       # e.g. "Saturday, November 14"
    return render_template(
        "home.html",
        patient=data.PATIENT,
        today=today,
        action_items=data.ACTION_ITEMS,
        home_tabs=data.HOME_TABS,
    )


@app.route("/overview")
def overview():
    return render_template(
        "overview.html",
        conditions=data.CONDITIONS,
        status_info=data.STATUS_INFO,
    )


@app.route("/results")
def results():
    return render_template(
        "results.html",
        tests=data.TESTS,
        glossary=data.GLOSSARY,
    )


# ----------------------------------------------------------------------
# STEP 4: start the server
# This block only runs when you do "python app.py" (not when another file
# imports this one, like our test file does).
# debug=True  -> the page reloads itself when you save a file, and errors
#                show helpful details. Turn it OFF for a real public site.
# port=5001   -> avoids a clash with the macOS "AirPlay" feature, which
#                uses the default port 5000.
# ----------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5001)
