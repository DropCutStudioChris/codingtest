"""Contract checks for POM-004: session tally persistence and phase cue."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestSessions(unittest.TestCase):
    def _read(self, name: str) -> str:
        path = ROOT / name
        self.assertTrue(path.exists(), f"{name} not found")
        return path.read_text(encoding="utf-8")

    def test_tally_element_present(self):
        html = self._read("index.html")
        self.assertIn('id="sessions"', html)

    def test_persistence_via_localstorage(self):
        main = self._read("main.js")
        self.assertIn("localStorage", main)
        self.assertIn("pomodoroSessions", main)

    def test_phase_cue_present(self):
        main = self._read("main.js")
        self.assertIn("cue", main)
        self.assertIn("cue", self._read("style.css"))


if __name__ == "__main__":
    unittest.main()
