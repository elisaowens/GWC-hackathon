"""
test_app.py
===========
A "smoke test": it automatically visits every page and checks that nothing is
broken. Run it BEFORE every git push:

    python -m unittest -v

It uses only built-in Python tools, so there is nothing extra to install.
"""

import re
import unittest
from pathlib import Path

from app import app, mark_jargon
import data

HERE = Path(__file__).parent


class ClearChartTests(unittest.TestCase):

    def setUp(self):
        # test_client() is a fake browser built into Flask
        self.client = app.test_client()

    def get_html(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, f"{url} did not load")
        return response.get_data(as_text=True)

    # ---------- the three pages ----------
    def test_home_page(self):
        html = self.get_html("/")
        self.assertIn("Welcome back, Jordan", html)
        self.assertIn("Action items", html)
        for label in ("Overview", "Visits", "Medications", "Test Results"):
            self.assertIn(label, html)
        # Visits and Medications are not built, but for the demo they must LOOK
        # like working tiles: all 4 tiles share the same style, none say "Coming soon"
        self.assertEqual(html.count('class="tile"'), 4)
        self.assertNotIn("Coming soon", html)

    def test_home_action_links_point_at_real_pages(self):
        html = self.get_html("/")
        self.assertIn('href="/overview#type-2-diabetes"', html)
        self.assertIn('href="/results#thyroid"', html)

    def test_overview_page(self):
        html = self.get_html("/overview")
        for condition in data.CONDITIONS:
            self.assertIn(condition["name"], html)
            self.assertIn(f'id="panel-{condition["id"]}"', html)
        for status in ("Resolved", "Critical", "Being Monitored"):
            self.assertIn(status, html)

    def test_overview_shows_patient_details(self):
        html = self.get_html("/overview")
        labels = ("Sex", "Height", "Weight", "Age", "Date of Birth", "Date of Last Visit")
        for label in labels:
            self.assertIn(f"<dt>{label}</dt>", html)
        for key in ("sex", "height", "weight", "age", "date_of_birth", "last_visit"):
            self.assertIn(f"<dd>{data.PATIENT[key]}</dd>", html)
        # the details box must come BEFORE the body drawing
        self.assertLess(html.index('class="patient-facts"'), html.index('class="body-svg"'))

    def test_footer_text_is_gone_from_every_page(self):
        for url in ("/", "/overview", "/results"):
            html = self.get_html(url)
            self.assertNotIn("<footer", html)
            self.assertNotIn("Not real medical advice", html)

    def test_css_uses_the_palette(self):
        css = (HERE / "static" / "css" / "style.css").read_text(encoding="utf-8").upper()
        for color in ("#BBDEF0", "#00A6A6", "#EFCA08", "#F49F0A", "#F08700"):
            self.assertIn(color, css)

    def test_results_page(self):
        html = self.get_html("/results")
        for test in data.TESTS:
            self.assertIn(f'id="{test["id"]}"', html)
        self.assertIn('class="jargon"', html)
        self.assertIn('data-term="hemoglobin"', html)

    # ---------- the data hangs together ----------
    def test_every_highlighted_word_is_in_the_glossary(self):
        html = self.get_html("/results")
        used = set(re.findall(r'data-term="([^"]+)"', html))
        self.assertTrue(used, "no words were highlighted at all")
        for key in used:
            self.assertIn(key, data.GLOSSARY)

    def test_every_region_exists_in_the_body_drawing(self):
        svg_source = (HERE / "templates" / "_body.html").read_text(encoding="utf-8")
        regions_in_svg = set(re.findall(r'data-region="([^"]+)"', svg_source))
        for condition in data.CONDITIONS:
            self.assertIn(condition["region"], regions_in_svg, condition["name"])
        for key, entry in data.GLOSSARY.items():
            if entry["kind"] == "anatomy":
                self.assertIn(entry["region"], regions_in_svg, key)
        # every region also needs a zoom box for the mini pictures
        self.assertEqual(
            len(re.findall(r'data-region="', svg_source)),
            len(re.findall(r'data-view="', svg_source)),
        )

    def test_every_image_file_exists(self):
        for condition in data.CONDITIONS:
            for section in ("looks_like", "getting_worse", "getting_better"):
                path = HERE / "static" / condition[section]["image"]
                self.assertTrue(path.exists(), f"missing image: {path}")

    def test_static_files_are_served(self):
        for url in ("/static/css/style.css", "/static/js/overview.js", "/static/js/results.js"):
            # "with" closes the file Flask opened to serve the response
            with self.client.get(url) as response:
                self.assertEqual(response.status_code, 200, url)

    # ---------- the highlighter ----------
    def test_jargon_highlights_words_and_keeps_case(self):
        out = str(mark_jargon("Your Hemoglobin is low."))
        self.assertIn('data-term="hemoglobin" tabindex="0">Hemoglobin</span>', out)

    def test_jargon_prefers_the_longest_match(self):
        out = str(mark_jargon("LDL cholesterol"))
        self.assertEqual(out.count("<span"), 1)
        self.assertIn('data-term="ldl cholesterol"', out)

    def test_jargon_handles_aliases_and_plurals(self):
        out = str(mark_jargon("kidneys and kidney"))
        self.assertEqual(out.count('data-term="kidneys"'), 2)

    def test_jargon_ignores_partial_words(self):
        # "heart" must not match inside "heartbeat"
        self.assertNotIn("<span", str(mark_jargon("A steady heartbeat")))

    def test_jargon_escapes_html(self):
        out = str(mark_jargon("<script>alert(1)</script> hemoglobin"))
        self.assertNotIn("<script>", out)
        self.assertIn("&lt;script&gt;", out)


if __name__ == "__main__":
    unittest.main()
