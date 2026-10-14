"""Contract checks for the POM-001 countdown engine.

There is no Node runtime on this machine, so these tests assert the engine's
observable contract from its source: the required constants and functions
exist, the durations are correct, and the engine stays DOM-free.
"""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP_JS = ROOT / "app.js"


class TestTimerEngine(unittest.TestCase):
    def _read(self) -> str:
        self.assertTrue(APP_JS.exists(), f"{APP_JS} not found")
        return APP_JS.read_text(encoding="utf-8")

    def test_durations_defined(self):
        src = self._read()
        self.assertIn("WORK_MINUTES", src)
        self.assertIn("BREAK_MINUTES", src)
        self.assertRegex(src, r"WORK_MINUTES\s*=\s*25")
        self.assertRegex(src, r"BREAK_MINUTES\s*=\s*5")

    def test_engine_functions_defined(self):
        src = self._read()
        for fn in ("newState", "tick", "switchPhase", "reset"):
            self.assertIn(fn, src, f"missing function: {fn}")

    def test_tick_decrements_seconds(self):
        src = self._read()
        self.assertRegex(src, r"secondsLeft\s*-=\s*1")

    def test_engine_is_dom_free(self):
        src = self._read()
        for token in ("document.", "window.", "getElementById", "addEventListener"):
            self.assertNotIn(token, src, f"engine references the DOM: {token}")


if __name__ == "__main__":
    unittest.main()
