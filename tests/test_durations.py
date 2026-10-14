"""Contract checks for POM-005: configurable durations in the engine.

There is no Node runtime on this machine, so these tests assert the engine's
observable contract from its source: `newState` accepts caller-supplied work
and break durations, defaults to 25/5 when omitted, and countdowns/phase
switches use the durations stored on the state rather than fixed constants.
"""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP_JS = ROOT / "app.js"


class TestConfigurableDurations(unittest.TestCase):
    def _read(self) -> str:
        self.assertTrue(APP_JS.exists(), f"{APP_JS} not found")
        return APP_JS.read_text(encoding="utf-8")

    def test_defaults_still_defined(self):
        src = self._read()
        self.assertRegex(src, r"WORK_MINUTES\s*=\s*25")
        self.assertRegex(src, r"BREAK_MINUTES\s*=\s*5")

    def test_newstate_accepts_durations(self):
        src = self._read()
        # newState takes work and break lengths, defaulting to the constants.
        self.assertRegex(
            src,
            r"newState\s*\(\s*workMinutes\s*=\s*WORK_MINUTES\s*,\s*breakMinutes\s*=\s*BREAK_MINUTES\s*\)",
            "newState should accept optional work/break minutes defaulting to 25/5",
        )

    def test_state_stores_durations(self):
        src = self._read()
        self.assertIn("workSeconds", src, "state should store workSeconds")
        self.assertIn("breakSeconds", src, "state should store breakSeconds")

    def test_seconds_left_derives_from_caller_duration(self):
        src = self._read()
        self.assertRegex(src, r"secondsLeft\s*:\s*workMinutes\s*\*\s*60")

    def test_phase_switch_uses_state_durations(self):
        src = self._read()
        self.assertIn("state.breakSeconds", src)
        self.assertIn("state.workSeconds", src)

    def test_engine_stays_dom_free(self):
        src = self._read()
        for token in ("document.", "window.", "getElementById", "addEventListener"):
            self.assertNotIn(token, src, f"engine references the DOM: {token}")


if __name__ == "__main__":
    unittest.main()
