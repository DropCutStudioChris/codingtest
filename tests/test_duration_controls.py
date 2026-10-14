"""Contract checks for the POM-006 duration controls."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestDurationControls(unittest.TestCase):
    def _read(self, name):
        path = ROOT / name
        self.assertTrue(path.exists(), f"{name} not found")
        return path.read_text(encoding="utf-8")

    def test_duration_inputs_present(self):
        html = self._read("index.html")
        self.assertIn('id="work-minutes"', html)
        self.assertIn('id="break-minutes"', html)

    def test_controller_reads_durations(self):
        main = self._read("main.js")
        self.assertIn("work-minutes", main)
        self.assertIn("break-minutes", main)
        self.assertIn("newState", main)

    def test_durations_applied_on_start(self):
        main = self._read("main.js")
        self.assertIn("readDurations", main)
        self.assertIn("setInterval", main)

    def test_displays_chosen_durations(self):
        self.assertIn("format", self._read("main.js"))
        self.assertIn('id="time"', self._read("index.html"))


if __name__ == "__main__":
    unittest.main()
