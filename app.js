// Pomodoro countdown engine — pure and DOM-free (POM-001).
// No document/window references; this file is unit-testable in isolation.

const WORK_MINUTES = 25;
const BREAK_MINUTES = 5;

// Create a fresh timer state. Callers may supply custom work/break lengths
// in minutes; omitted arguments fall back to the default 25/5 durations.
function newState(workMinutes = WORK_MINUTES, breakMinutes = BREAK_MINUTES) {
  return {
    phase: "work",
    secondsLeft: workMinutes * 60,
    completedSessions: 0,
    workSeconds: workMinutes * 60,
    breakSeconds: breakMinutes * 60,
  };
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
    state.secondsLeft = state.breakSeconds;
  } else {
    state.phase = "work";
    state.secondsLeft = state.workSeconds;
  }
  return state;
}

// Return to the start of a work interval (keeps the completed-session tally).
function reset(state) {
  state.phase = "work";
  state.secondsLeft = state.workSeconds;
  return state;
}
