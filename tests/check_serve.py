"""Serve check for POM-003: start the static server, fetch the page, assert it's the timer.

Exits 0 on success, non-zero on failure — used directly as the work item's
Validation command.
"""

import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PORT = 8000
URL = f"http://127.0.0.1:{PORT}/"


def main() -> int:
    server = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(PORT), "--bind", "127.0.0.1"],
        cwd=str(ROOT),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        body = ""
        status = None
        for _ in range(50):
            try:
                with urllib.request.urlopen(URL, timeout=1) as resp:
                    status = resp.status
                    body = resp.read().decode("utf-8", errors="replace")
                break
            except (urllib.error.URLError, OSError):
                time.sleep(0.2)
        else:
            print("FAIL: server did not come up")
            return 1

        if status != 200:
            print(f"FAIL: expected HTTP 200, got {status}")
            return 1
        if "Pomodoro" not in body:
            print("FAIL: served page is not the timer")
            return 1

        print(f"OK: served pomodoro page at {URL} (HTTP {status})")
        return 0
    finally:
        server.terminate()
        try:
            server.wait(timeout=5)
        except subprocess.TimeoutExpired:
            server.kill()


if __name__ == "__main__":
    sys.exit(main())
