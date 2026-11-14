# ClearChart

A patient-portal demo (in the style of MyChart) built for a 7-hour healthcare hackathon.
It explains medical information in plain language.

* **Home** - welcome message, action items, and four tabs
* **Overview** - body model + a sidebar of conditions (click one to highlight the body area and see details)
* **Test Results** - lab results where medical words are underlined; hover for a definition or a mini body picture

All patient data is **made up**. Visits and Medications are "Coming soon" tabs.

## Run it (first time)

```bash
# 1. make a private Python environment inside the project folder
python -m venv .venv

# 2. turn it on
#    Windows (PowerShell):  .venv\Scripts\Activate.ps1
#    Windows (cmd):         .venv\Scripts\activate.bat
#    Mac / Linux:           source .venv/bin/activate

# 3. install Flask
pip install -r requirements.txt

# 4. start the app
python app.py
```

Open http://127.0.0.1:5001 in your browser. Stop the server with `Ctrl+C`.

In VS Code, press `Ctrl+Shift+P` -> "Python: Select Interpreter" and pick the one inside `.venv`.

## Check for bugs before you push

```bash
python -m unittest -v
```

## Where things live

| File | What it is |
| --- | --- |
| `app.py` | The server: three pages + the medical-word highlighter |
| `data.py` | **All the content** (conditions, test results, glossary, action items) |
| `templates/base.html` | Top bar + footer shared by every page |
| `templates/home.html`, `overview.html`, `results.html` | The three pages |
| `templates/_body.html` | The body drawing (SVG) |
| `static/css/style.css` | All the styling |
| `static/js/overview.js` | Click behaviour on the Overview page |
| `static/js/results.js` | Hover pop-ups on the Test Results page |
| `static/images/` | Placeholder pictures for each condition |
| `test_app.py` | Automatic checks |

## Common changes

**Add a condition** - copy one block in `CONDITIONS` in `data.py`, give it a new `id`, and pick a `region` that exists in `templates/_body.html`.

**Add a medical word** - add an entry to `GLOSSARY` in `data.py`. It is highlighted everywhere automatically. Use `"kind": "anatomy"` plus a `region` to get the mini body picture.

**Use real stock photos** - save the photo in `static/images/` and change the file name in `data.py` (for example `"images/wrist-swollen.jpg"`). Check the license first; Unsplash, Pexels and Wikimedia Commons list theirs. Keep the `alt` text accurate.

**Turn on the Visits or Medications tab** - build the page (a route in `app.py` + a template), then replace `"endpoint": None` with the route name in `HOME_TABS`.

## Working together on GitHub

* Pull before you start: `git pull`
* Work on different files when you can. A natural split: one person owns `templates/overview.html`, `_body.html` and `overview.js`; the other owns `results.html`, `results.js` and the glossary in `data.py`.
* Use a branch per feature: `git checkout -b results-page`, then open a Pull Request, or merge when ready.
* Commit small and often: `git add .` then `git commit -m "Add hover tooltips"` then `git push`.
* `.gitignore` already keeps `.venv` and `__pycache__` out of the repo.
