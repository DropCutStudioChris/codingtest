// Pomodoro countdown engine — pure and DOM-free (POM-001).
// No document/window references; this file is unit-testable in isolation.

const WORK_MINUTES = 25;
const BREAK_MINUTES = 5;
const WORK_SECONDS = WORK_MINUTES * 60;
const BREAK_SECONDS = BREAK_MINUTES * 60;

// Create a fresh timer state.
function newState() {
  return { phase: "work", secondsLeft: WORK_SECONDS, completedSessions: 0 };
}

// Advance one second. Switches phase automatically at zero.
function tick(state) {
  state.secondsLeft -= 1;
  if (state.secondsLeft <= 0) {
    switchPhase(state);
  }
  return state;
}

// Flip work <-> break. Ending a work phase counts a completed session.
function switchPhase(state) {
  if (state.phase === "work") {
    state.completedSessions += 1;
    state.phase = "break";
    state.secondsLeft = BREAK_SECONDS;
  } else {
    state.phase = "work";
    state.secondsLeft = WORK_SECONDS;
  }
  return state;
}

// Return to the start of a work interval (keeps the completed-session tally).
function reset(state) {
  state.phase = "work";
  state.secondsLeft = WORK_SECONDS;
  return state;
}
