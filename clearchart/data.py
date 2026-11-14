"""
data.py
=======
Every piece of information the app shows lives in THIS one file.
Everything here is FAKE demo data for a made-up patient.

Why keep it separate from app.py?
  * Teammates can edit the content without touching the page logic.
  * Fewer merge conflicts on GitHub (you're editing different files).

HOW THIS FILE IS BUILT
  Python "dictionaries" look like  {"key": "value"}  and "lists" look like
  [item1, item2].  Below, we mostly have LISTS of DICTIONARIES, e.g. a list
  of conditions where each condition is a dictionary.

  GOTCHA FOR TEMPLATES: never name a dictionary key  items, values, keys,
  get, copy, update, pop or clear.  Those are built-in dictionary methods and
  the HTML templates would grab the method instead of your data.
"""

# ----------------------------------------------------------------------
# 1. THE PATIENT
# ----------------------------------------------------------------------
PATIENT = {
    "first_name": "Jordan",
    "full_name": "Jordan Rivera",
}

# ----------------------------------------------------------------------
# 2. HOME PAGE TABS
# "endpoint" is the NAME of the Python function in app.py that shows the page.
# endpoint = None means "not built yet", so the tile shows "Coming soon".
# To switch on a tab later: build its page, then replace None with its name.
# ----------------------------------------------------------------------
HOME_TABS = [
    {"label": "Overview", "icon": "🧍", "blurb": "See your conditions on a body map", "endpoint": "overview"},
    {"label": "Visits", "icon": "📅", "blurb": "Past and upcoming appointments", "endpoint": None},
    {"label": "Medications", "icon": "💊", "blurb": "Your medicines and refills", "endpoint": None},
    {"label": "Test Results", "icon": "🧪", "blurb": "Lab results in plain language", "endpoint": "results"},
]

# ----------------------------------------------------------------------
# 3. ACTION ITEMS (the notifications on the home page)
# level  -> controls the colour on the page: "urgent", "new" or "info"
# tag    -> the little word shown on the card (so colour is never the only clue)
# endpoint + anchor -> where the "View" link goes.
#   anchor is the part after the # in a web address. For the Overview page it
#   is the condition's id and the page opens that condition automatically.
# ----------------------------------------------------------------------
ACTION_ITEMS = [
    {
        "title": "Your blood sugar needs attention",
        "message": "Your latest HbA1c test is high. See what to watch for.",
        "level": "urgent",
        "tag": "Urgent",
        "endpoint": "overview",
        "anchor": "type-2-diabetes",
        "link_text": "View condition",
    },
    {
        "title": "New test results are ready",
        "message": "Your Nov 3 lab results were posted. We explained the medical words for you.",
        "level": "new",
        "tag": "New",
        "endpoint": "results",
        "anchor": "",
        "link_text": "View results",
    },
    {
        "title": "Wrist check-up on Nov 20 at 2:30 PM",
        "message": "Your care team will check how your wrist is healing.",
        "level": "info",
        "tag": "Reminder",
        "endpoint": "overview",
        "anchor": "fractured-wrist",
        "link_text": "View condition",
    },
    {
        "title": "Your thyroid levels changed",
        "message": "Your TSH result is above the normal range. Learn what that means.",
        "level": "info",
        "tag": "Reminder",
        "endpoint": "results",
        "anchor": "thyroid",
        "link_text": "View results",
    },
]

# ----------------------------------------------------------------------
# 4. CONDITION STATUSES
# The key is the exact words shown to the patient.
# "css"  -> part of the CSS class that colours the badge.
# "help" -> a one-sentence plain-English explanation of the status.
# ----------------------------------------------------------------------
STATUS_INFO = {
    "Resolved": {
        "css": "resolved",
        "help": "This has healed or gone away. No action is needed right now.",
    },
    "Critical": {
        "css": "critical",
        "help": "This needs prompt attention. Follow your care plan and call your care team if it gets worse.",
    },
    "Being Monitored": {
        "css": "monitored",
        "help": "Your care team is keeping an eye on this and will check in regularly.",
    },
}

# ----------------------------------------------------------------------
# 5. CONDITIONS (the Overview page sidebar)
#
# id            unique name with no spaces (used in web addresses)
# region        which spot on the body model lights up. It MUST match a
#               data-region name inside templates/_body.html
# region_label  the words shown under the body model
# images        file names live in static/images/. They are PLACEHOLDERS right
#               now. To use a real stock photo, drop it into that folder and
#               change the file name here (for example "images/wrist.jpg").
# ----------------------------------------------------------------------
CONDITIONS = [
    {
        "id": "type-2-diabetes",
        "name": "Type 2 Diabetes",
        "category": "Long-term disease",
        "status": "Critical",
        "region": "pancreas",
        "region_label": "Pancreas (middle of the belly)",
        "description": (
            "Your body has trouble using insulin, a hormone made by the pancreas that moves "
            "sugar from your blood into your cells. Sugar builds up in your blood instead. "
            "It is managed with food choices, activity, and usually medicine."
        ),
        "looks_like": {
            "image": "images/type-2-diabetes-looks.avif",
            "alt": "Placeholder image for how type 2 diabetes can look on the skin",
            "text": (
                "Diabetes often has no visible signs. Some people notice darker, velvety "
                "patches of skin on the neck or armpits, or cuts and sores that heal slowly."
            ),
        },
        "getting_worse": {
            "image": "images/type-2-diabetes-worse.png",
            "alt": "Placeholder image for signs that diabetes is getting worse",
            "signs": [
                "Very strong thirst and needing to urinate much more often",
                "Blurry vision",
                "Sores on your feet that heal slowly or look infected",
                "Blood sugar readings that stay above the target your doctor gave you",
                "Nausea, vomiting, fruity-smelling breath, or confusion: get emergency help right away",
            ],
        },
        "getting_better": {
            "image": "images/type-2-diabetes-better.jpg",
            "alt": "Placeholder image for signs that diabetes is getting better",
            "signs": [
                "Blood sugar readings move closer to your target",
                "Less thirst and fewer bathroom trips",
                "More energy during the day",
                "Your next HbA1c test (your 3-month average blood sugar) is lower than before",
            ],
        },
    },
    {
        "id": "fractured-wrist",
        "name": "Fractured Wrist",
        "category": "Broken bone",
        "status": "Being Monitored",
        "region": "right-wrist",
        "region_label": "Right wrist",
        "description": (
            "You have a crack in one of the bones of your right wrist (the forearm bone on "
            "the thumb side). A cast keeps it still for about 6 weeks while the bone heals."
        ),
        "looks_like": {
            "image": "images/fractured-wrist-looks.jpg",
            "alt": "Placeholder image of a swollen, bruised wrist",
            "text": (
                "Swelling and bruising around the wrist, tenderness, and sometimes a wrist "
                "that looks bent or crooked. Under a cast you may not see the wrist, but "
                "your fingers may look a little puffy."
            ),
        },
        "getting_worse": {
            "image": "images/fractured-wrist-worse.jpeg",
            "alt": "Placeholder image of pale, swollen fingers coming out of a cast",
            "signs": [
                "Fingers turn pale or blue, or feel cold",
                "New numbness or tingling in your fingers",
                "Pain gets stronger instead of slowly easing",
                "Swelling that does not go down when you raise your arm above your heart",
                "Your cast feels very tight, smells bad, or has fluid leaking through",
            ],
        },
        "getting_better": {
            "image": "images/fractured-wrist-better.jpg",
            "alt": "Placeholder image of a healing wrist with a fading bruise",
            "signs": [
                "Pain gradually fades",
                "Swelling shrinks and bruises change from purple to green to yellow",
                "You can wiggle your fingers more easily",
                "Follow-up X-rays show the bone knitting back together",
            ],
        },
    },
    {
        "id": "hypothyroidism",
        "name": "Underactive Thyroid",
        "category": "Hormone condition",
        "status": "Being Monitored",
        "region": "thyroid",
        "region_label": "Thyroid (front of the neck)",
        "description": (
            "Your thyroid is a small butterfly-shaped gland in the front of your neck. "
            "When it is underactive (called hypothyroidism), it makes too little thyroid "
            "hormone and your body slows down. A daily pill replaces the missing hormone."
        ),
        "looks_like": {
            "image": "images/hypothyroidism-looks.jpeg",
            "alt": "Placeholder image of the signs of an underactive thyroid",
            "text": (
                "Often subtle: a puffy face, dry skin, thinning hair, or a swelling at the "
                "front of the neck."
            ),
        },
        "getting_worse": {
            "image": "images/hypothyroidism-worse.jpg",
            "alt": "Placeholder image of signs that a thyroid problem is getting worse",
            "signs": [
                "Feeling extremely tired or cold all the time",
                "Weight gain without any change in how you eat",
                "New swelling in your neck or trouble swallowing",
                "Very slow heartbeat, or feeling confused or very sleepy: get medical help right away",
            ],
        },
        "getting_better": {
            "image": "images/hypothyroidism-better.jpg",
            "alt": "Placeholder image of signs that a thyroid problem is getting better",
            "signs": [
                "More energy",
                "Skin and hair feel less dry",
                "You feel warmer and less sluggish",
                "Your next thyroid blood test (TSH) is closer to normal",
            ],
        },
    },
    {
        "id": "eczema",
        "name": "Eczema (Skin Rash)",
        "category": "Skin condition",
        "status": "Resolved",
        "region": "left-elbow",
        "region_label": "Left inner elbow",
        "description": (
            "Eczema is a common skin condition that causes dry, itchy, red patches. "
            "It is not contagious. Yours was on the inside of your left elbow and has "
            "cleared up, though eczema can come back."
        ),
        "looks_like": {
            "image": "images/eczema-looks.jpg",
            "alt": "Placeholder image of an eczema rash on the inner elbow",
            "text": (
                "Dry, rough, red or darker patches of skin, sometimes with tiny bumps. "
                "Scratching can make the skin look scaly or thickened."
            ),
        },
        "getting_worse": {
            "image": "images/eczema-worse.jpg",
            "alt": "Placeholder image of an eczema rash that is inflamed and cracked",
            "signs": [
                "Skin cracks, oozes clear fluid, or forms yellow crusts (possible infection)",
                "The rash spreads to new areas",
                "Itching keeps you awake at night",
                "Painful blisters or a fever",
            ],
        },
        "getting_better": {
            "image": "images/eczema-better.jpg",
            "alt": "Placeholder image of calm, healing skin on the inner elbow",
            "signs": [
                "Itching eases",
                "Redness fades and the skin colour evens out",
                "Skin feels soft instead of rough and scaly",
                "Longer stretches between flare-ups",
            ],
        },
    },
]

# ----------------------------------------------------------------------
# 6. TEST RESULTS
# flag must be exactly "Normal", "Low" or "High".
# Any medical word that is in GLOSSARY (section 7) is highlighted
# automatically on the page. You do NOT mark them by hand.
# ----------------------------------------------------------------------
TESTS = [
    {
        "id": "cbc",
        "name": "Complete Blood Count (CBC)",
        "date": "Nov 3, 2026",
        "summary": (
            "A complete blood count counts the cells in your blood. Most of your results "
            "are normal, but your hemoglobin is a little low, which can be a sign of mild anemia."
        ),
        "rows": [
            {
                "name": "Hemoglobin",
                "value": "11.2",
                "unit": "g/dL",
                "normal_range": "12.0 – 15.5",
                "flag": "Low",
                "meaning": "Slightly low. Your red blood cells may be carrying less oxygen than usual, which can cause tiredness.",
            },
            {
                "name": "White blood cell count",
                "value": "7.1",
                "unit": "×10³/µL",
                "normal_range": "4.5 – 11.0",
                "flag": "Normal",
                "meaning": "Normal. No sign that your body is fighting an infection.",
            },
            {
                "name": "Platelet count",
                "value": "245",
                "unit": "×10³/µL",
                "normal_range": "150 – 450",
                "flag": "Normal",
                "meaning": "Normal. Your blood should clot well.",
            },
        ],
    },
    {
        "id": "metabolic",
        "name": "Metabolic Panel",
        "date": "Nov 3, 2026",
        "summary": (
            "A metabolic panel checks your blood sugar and how well your kidneys are "
            "filtering waste. Your blood sugar is above target, which fits with your "
            "type 2 diabetes. Your kidney result is normal."
        ),
        "rows": [
            {
                "name": "Fasting glucose",
                "value": "168",
                "unit": "mg/dL",
                "normal_range": "70 – 99",
                "flag": "High",
                "meaning": "High. Your blood sugar is above target even before eating. Insulin from your pancreas may not be working as well as it should.",
            },
            {
                "name": "HbA1c",
                "value": "8.4",
                "unit": "%",
                "normal_range": "Below 5.7",
                "flag": "High",
                "meaning": "High. Your average blood sugar over the last 2 to 3 months has been above target. Your care team may set a personal goal for you, often under 7%.",
            },
            {
                "name": "Creatinine",
                "value": "0.9",
                "unit": "mg/dL",
                "normal_range": "0.6 – 1.1",
                "flag": "Normal",
                "meaning": "Normal. Your kidneys appear to be filtering waste well.",
            },
        ],
    },
    {
        "id": "lipid",
        "name": "Lipid Panel",
        "date": "Nov 3, 2026",
        "summary": (
            "A lipid panel measures cholesterol and other fats in your blood. High LDL "
            "and triglycerides can slowly raise your risk of heart disease, so your care "
            "team may talk with you about food, exercise, and medicine. Your liver makes "
            "much of your body's cholesterol."
        ),
        "rows": [
            {
                "name": "LDL cholesterol",
                "value": "142",
                "unit": "mg/dL",
                "normal_range": "Below 100",
                "flag": "High",
                "meaning": "High. Too much of this \"bad\" cholesterol can build up in blood vessel walls over time and strain your heart.",
            },
            {
                "name": "HDL cholesterol",
                "value": "52",
                "unit": "mg/dL",
                "normal_range": "40 or higher",
                "flag": "Normal",
                "meaning": "Normal. This is the \"good\" cholesterol that helps carry extra cholesterol away.",
            },
            {
                "name": "Triglycerides",
                "value": "180",
                "unit": "mg/dL",
                "normal_range": "Below 150",
                "flag": "High",
                "meaning": "A bit high. Eating fewer sugary and fatty foods and getting more exercise can help.",
            },
        ],
    },
    {
        "id": "thyroid",
        "name": "Thyroid Panel",
        "date": "Nov 3, 2026",
        "summary": (
            "A thyroid panel checks how well your thyroid is working. Your TSH is high and "
            "your Free T4 is low. Together, that pattern fits an underactive thyroid "
            "(hypothyroidism). Your care team may adjust your medicine."
        ),
        "rows": [
            {
                "name": "TSH",
                "value": "6.8",
                "unit": "mIU/L",
                "normal_range": "0.4 – 4.0",
                "flag": "High",
                "meaning": "High. Your pituitary gland is signalling your thyroid to work harder, which is common when the thyroid is underactive.",
            },
            {
                "name": "Free T4",
                "value": "0.7",
                "unit": "ng/dL",
                "normal_range": "0.8 – 1.8",
                "flag": "Low",
                "meaning": "Slightly low. Your thyroid is making a little less hormone than your body needs.",
            },
        ],
    },
]

# ----------------------------------------------------------------------
# 7. GLOSSARY: the medical words that get highlighted
#
# The dictionary key is the word in lowercase.
# kind     "definition" -> hover shows a short explanation
#          "anatomy"    -> hover shows the explanation AND a mini body picture
# region   (anatomy only) which spot on the body lights up. It MUST match a
#          data-region name in templates/_body.html
# aliases  other spellings that should highlight too (plurals, abbreviations)
# ----------------------------------------------------------------------
GLOSSARY = {
    # ---- plain definitions ----
    "complete blood count": {
        "label": "Complete blood count (CBC)",
        "kind": "definition",
        "text": "A common blood test that counts the different kinds of cells in your blood.",
        "aliases": ["cbc"],
    },
    "hemoglobin": {
        "label": "Hemoglobin",
        "kind": "definition",
        "text": "A protein inside red blood cells that carries oxygen from your lungs to the rest of your body. Low levels can make you feel tired or short of breath.",
    },
    "red blood cells": {
        "label": "Red blood cells",
        "kind": "definition",
        "text": "Cells that carry oxygen around your body. Your body makes them in your bone marrow.",
        "aliases": ["red blood cell"],
    },
    "white blood cell": {
        "label": "White blood cells",
        "kind": "definition",
        "text": "Cells that fight germs and infections. A high count can mean your body is fighting something.",
        "aliases": ["white blood cells"],
    },
    "platelet": {
        "label": "Platelets",
        "kind": "definition",
        "text": "Tiny cell pieces that help your blood form clots, so cuts stop bleeding.",
        "aliases": ["platelets"],
    },
    "anemia": {
        "label": "Anemia",
        "kind": "definition",
        "text": "Not having enough healthy red blood cells or hemoglobin, so your body gets less oxygen. It can cause tiredness and pale skin.",
    },
    "metabolic panel": {
        "label": "Metabolic panel",
        "kind": "definition",
        "text": "A group of blood tests that check your blood sugar and how well your kidneys are working.",
    },
    "glucose": {
        "label": "Glucose",
        "kind": "definition",
        "text": "Blood sugar. It is your body's main source of energy, but too much for too long can damage blood vessels and nerves.",
    },
    "hba1c": {
        "label": "HbA1c",
        "kind": "definition",
        "text": "A blood test that shows your average blood sugar over the past 2 to 3 months. Doctors use it to see how well diabetes is controlled.",
    },
    "creatinine": {
        "label": "Creatinine",
        "kind": "definition",
        "text": "A waste product made by your muscles. Healthy kidneys filter it out, so a high level can mean the kidneys are not working well.",
    },
    "insulin": {
        "label": "Insulin",
        "kind": "definition",
        "text": "A hormone that lets sugar move from your blood into your cells for energy. In type 2 diabetes, the body does not respond to insulin well.",
    },
    "type 2 diabetes": {
        "label": "Type 2 diabetes",
        "kind": "definition",
        "text": "A long-term condition where your body does not use insulin well, so sugar builds up in your blood.",
    },
    "lipid panel": {
        "label": "Lipid panel",
        "kind": "definition",
        "text": "A group of blood tests that measure cholesterol and other fats in your blood.",
    },
    "cholesterol": {
        "label": "Cholesterol",
        "kind": "definition",
        "text": "A waxy, fat-like substance in your blood. Your body needs some, but too much can build up inside your blood vessels.",
    },
    "ldl cholesterol": {
        "label": "LDL cholesterol",
        "kind": "definition",
        "text": "The \"bad\" cholesterol. It can build up inside blood vessels and raise your risk of heart disease. Lower is better.",
        "aliases": ["ldl"],
    },
    "hdl cholesterol": {
        "label": "HDL cholesterol",
        "kind": "definition",
        "text": "The \"good\" cholesterol. It helps carry extra cholesterol away from your blood vessels. Higher is better.",
        "aliases": ["hdl"],
    },
    "triglycerides": {
        "label": "Triglycerides",
        "kind": "definition",
        "text": "A type of fat in your blood. Extra calories your body does not need right away are stored as triglycerides.",
    },
    "thyroid panel": {
        "label": "Thyroid panel",
        "kind": "definition",
        "text": "A group of blood tests that check how well your thyroid is working.",
    },
    "tsh": {
        "label": "TSH (thyroid-stimulating hormone)",
        "kind": "definition",
        "text": "A signal from your brain that tells your thyroid how hard to work. When the thyroid is underactive, TSH goes up because the brain is asking for more thyroid hormone.",
        "aliases": ["thyroid-stimulating hormone"],
    },
    "free t4": {
        "label": "Free T4",
        "kind": "definition",
        "text": "The main hormone made by your thyroid. \"Free\" means the part that is ready for your body to use.",
        "aliases": ["t4"],
    },
    "hypothyroidism": {
        "label": "Hypothyroidism",
        "kind": "definition",
        "text": "An underactive thyroid. The gland makes too little hormone, so your body slows down. It can cause tiredness, feeling cold, and weight gain.",
    },
    "hormone": {
        "label": "Hormone",
        "kind": "definition",
        "text": "A chemical messenger made by a gland. It travels in your blood and tells other parts of your body what to do.",
    },
    # ---- anatomy: these also show a mini body picture ----
    "thyroid": {
        "label": "Thyroid",
        "kind": "anatomy",
        "region": "thyroid",
        "text": "A small butterfly-shaped gland at the front of your neck. It makes hormones that control your energy and how fast your body works.",
        "aliases": ["thyroid gland"],
    },
    "kidneys": {
        "label": "Kidneys",
        "kind": "anatomy",
        "region": "kidneys",
        "text": "Two bean-shaped organs on either side of your lower back. They filter waste and extra water out of your blood to make urine.",
        "aliases": ["kidney"],
    },
    "pancreas": {
        "label": "Pancreas",
        "kind": "anatomy",
        "region": "pancreas",
        "text": "An organ tucked behind your stomach. It makes insulin and juices that help you digest food.",
    },
    "liver": {
        "label": "Liver",
        "kind": "anatomy",
        "region": "liver",
        "text": "A large organ on the upper right side of your belly. It cleans your blood, helps digest food, and makes cholesterol.",
    },
    "heart": {
        "label": "Heart",
        "kind": "anatomy",
        "region": "heart",
        "text": "The muscle in your chest that pumps blood around your body.",
    },
    "pituitary gland": {
        "label": "Pituitary gland",
        "kind": "anatomy",
        "region": "head",
        "text": "A pea-sized gland at the base of your brain. It makes TSH and other hormones that tell your other glands what to do.",
        "aliases": ["pituitary"],
    },
}


# ----------------------------------------------------------------------
# 8. SAFETY NET
# This function runs every time the app starts. If a teammate makes a typo
# (for example the status "Critcal"), the app stops immediately with a clear
# message instead of silently showing something broken on demo day.
# ----------------------------------------------------------------------
def check_data():
    # every condition needs a known status and a unique id
    seen_ids = set()
    for condition in CONDITIONS:
        if condition["status"] not in STATUS_INFO:
            raise ValueError(
                f"Condition '{condition['name']}' has an unknown status "
                f"'{condition['status']}'. Use one of: {list(STATUS_INFO)}"
            )
        if condition["id"] in seen_ids:
            raise ValueError(f"Two conditions share the id '{condition['id']}'")
        seen_ids.add(condition["id"])

    # every test result needs a known flag
    for test in TESTS:
        for row in test["rows"]:
            if row["flag"] not in ("Normal", "Low", "High"):
                raise ValueError(
                    f"Result '{row['name']}' has flag '{row['flag']}'. "
                    "Use Normal, Low or High."
                )

    # glossary words must be unique, and anatomy words need a region
    seen_words = {}
    for key, entry in GLOSSARY.items():
        if entry["kind"] not in ("definition", "anatomy"):
            raise ValueError(f"Glossary word '{key}' has unknown kind '{entry['kind']}'")
        if entry["kind"] == "anatomy" and "region" not in entry:
            raise ValueError(f"Anatomy word '{key}' needs a 'region'")
        for spelling in [key] + entry.get("aliases", []):
            spelling = spelling.lower()
            if spelling in seen_words:
                raise ValueError(
                    f"'{spelling}' is used by both '{seen_words[spelling]}' and '{key}'"
                )
            seen_words[spelling] = key


check_data()
