"""Contract checks for the POM-007 duration persistence."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestDurationPersistence(unittest.TestCase):
    def _read(self, name):
        path = ROOT / name
        self.assertTrue(path.exists(), f"{name} not found")
        return path.read_text(encoding="utf-8")

    def test_persistence_key_defined(self):
        main = self._read("main.js")
        self.assertIn("pomodoroDurations", main)

    def test_uses_localstorage(self):
        main = self._read("main.js")
        self.assertIn("localStorage", main)

    def test_restores_on_load(self):
        main = self._read("main.js")
        self.assertIn("restoreDurations", main)

    def test_saves_durations(self):
        main = self._read("main.js")
        self.assertIn("JSON.stringify", main)

    def test_restore_wired_at_startup(self):
        main = self._read("main.js")
        self.assertIn("restoreDurations();", main)


if __name__ == "__main__":
    unittest.main()
