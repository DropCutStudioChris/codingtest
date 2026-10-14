"""Contract checks for the POM-002 controls and display.

Asserts the page exposes start/pause/reset controls and a time readout, and
that the UI controller wires them to the POM-001 engine.
"""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestControls(unittest.TestCase):
    def _read(self, name: str) -> str:
        path = ROOT / name
        self.assertTrue(path.exists(), f"{name} not found")
        return path.read_text(encoding="utf-8")

    def test_controls_present(self):
        html = self._read("index.html")
        for cid in ("start", "pause", "reset"):
            self.assertIn(f'id="{cid}"', html, f"missing control #{cid}")

    def test_time_display_present(self):
        html = self._read("index.html")
        self.assertIn('id="time"', html)

    def test_scripts_referenced(self):
        html = self._read("index.html")
        self.assertIn("app.js", html)
        self.assertIn("main.js", html)

    def test_wiring_references_engine(self):
        main = self._read("main.js")
        for name in ("newState", "tick", "reset", "setInterval"):
            self.assertIn(name, main, f"controller missing {name}")
        for cid in ("start", "pause", "reset"):
            self.assertIn(cid, main, f"control {cid} not wired")


if __name__ == "__main__":
    unittest.main()
