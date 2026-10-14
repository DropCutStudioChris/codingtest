<!--
APS Module: Pomodoro Timer
See: plans/aps-rules.md
ID: POM
-->

# Pomodoro Timer

| ID  | Owner    | Status |
| --- | -------- | ------ |
| POM | @roostaa | Complete |

## Goal

A minimal browser-based pomodoro timer: 25-minute focus intervals, 5-minute
breaks, with controls and a served webpage.

## Success Criteria

- [ ] Focus/break intervals count down and auto-switch
- [ ] Start/pause/reset controls work
- [ ] Page is served on localhost
- [ ] Completed sessions are tallied and a phase change is signalled

## Work Items

### POM-001: Countdown engine

- **Status:** Complete: 2026-10-14
- **Intent:** A pure, DOM-free countdown engine that drives the pomodoro timing
- **Expected Outcome:** `app.js` exposes work/break durations and a `tick`-style step that decrements seconds and switches phase (work ↔ break) with a round counter at zero — with no DOM or browser references
- **Validation:** `python3 -m unittest tests.test_timer`
- **Learning:** "Keep the timer engine DOM-free so it stays unit-testable without a browser or Node runtime"
- **Non-scope:** Any UI, controls, or serving

### POM-002: Controls and display

- **Status:** Complete: 2026-10-14
- **Intent:** Let the user start, pause, and reset the timer and see the remaining time
- **Expected Outcome:** The page shows a time readout and start/pause/reset buttons wired to the POM-001 engine
- **Validation:** `python3 -m unittest tests.test_controls`
- **Learning:** "Split the pure engine (app.js) from the DOM wiring (main.js) so the countdown stays testable in isolation"
- **Dependencies:** POM-001
- **Non-scope:** Styling polish, session tally, notifications

### POM-003: Serve on localhost

- **Status:** Complete: 2026-10-14
- **Intent:** Make the timer reachable as a local webpage
- **Expected Outcome:** A static page is served at `http://127.0.0.1:8000/` and returns the timer page
- **Validation:** `python3 tests/check_serve.py`
- **Learning:** "Static serving needs no framework — python3 -m http.server is enough for a localhost demo"
- **Dependencies:** POM-002
- **Non-scope:** Hosting beyond localhost, HTTPS, or a custom server framework

### POM-004: Session tally and phase cue

- **Status:** Complete: 2026-10-14
- **Intent:** Track completed focus sessions and signal when a phase changes
- **Expected Outcome:** A completed-session count persists across page reloads, and a phase change produces a visible or audible cue
- **Validation:** `python3 -m unittest tests.test_sessions`
- **Learning:** "Persist the tally in localStorage and cue on phase-change detection rather than timer events, so reloads and multi-tick boundaries stay correct"
- **Dependencies:** POM-001
- **Non-scope:** Statistics dashboards, sound design, desktop notifications
