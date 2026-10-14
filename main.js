// UI controller: wires controls, displays time, tallies sessions (POM-002/POM-004/POM-006).

let state = newState();
let totalSessions = parseInt(localStorage.getItem("pomodoroSessions") || "0", 10);
let lastCompleted = state.completedSessions;

function format(seconds) {
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return String(m).padStart(2, "0") + ":" + String(s).padStart(2, "0");
}

// Read the chosen work/break minutes from the duration controls.
function readDurations() {
  const work = parseInt(document.getElementById("work-minutes").value, 10) || 25;
  const brk = parseInt(document.getElementById("break-minutes").value, 10) || 5;
  return { work, brk };
}

// Persist completed sessions and refresh the tally.
function syncSessions() {
  if (state.completedSessions > lastCompleted) {
    totalSessions += state.completedSessions - lastCompleted;
    lastCompleted = state.completedSessions;
    localStorage.setItem("pomodoroSessions", String(totalSessions));
    document.getElementById("sessions").textContent = String(totalSessions);
  }
}

// Visible cue when the phase changes (work <-> break).
function cue() {
  const el = document.getElementById("phase");
  el.classList.remove("cue");
  void el.offsetWidth; // restart the animation
  el.classList.add("cue");
}

function render() {
  document.getElementById("time").textContent = format(state.secondsLeft);
  const phase = state.phase === "work" ? "Work" : "Break";
  const el = document.getElementById("phase");
  if (el.textContent !== phase) {
    el.textContent = phase;
    cue();
  }
  syncSessions();
}

let timerId = null;

function startTimer() {
  if (timerId !== null) return;
  const { work, brk } = readDurations();
  state = newState(work, brk);
  lastCompleted = state.completedSessions;
  timerId = setInterval(function () {
    tick(state);
    render();
  }, 1000);
  render();
}

function pauseTimer() {
  if (timerId !== null) {
    clearInterval(timerId);
    timerId = null;
  }
}

function resetTimer() {
  pauseTimer();
  reset(state);
  render();
}

document.getElementById("start").addEventListener("click", startTimer);
document.getElementById("pause").addEventListener("click", pauseTimer);
document.getElementById("reset").addEventListener("click", resetTimer);

document.getElementById("sessions").textContent = String(totalSessions);
render();
