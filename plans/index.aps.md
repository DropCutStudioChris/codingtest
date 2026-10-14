<!--
APS Index Template
==================
AGENT: This is NON-EXECUTABLE. Do not create tasks here.
Focus on: intent, scope, modules, risks — NOT implementation.
See: plans/aps-rules.md
-->

# Pomodoro Timer

| Field   | Value     |
| ------- | --------- |
| Status  | Draft     |
| Owner   | @roostaa  |
| Created | 2026-10-14 |

## Problem

We want a simple pomodoro timer that runs as a local webpage — and, more
importantly, a real (if tiny) project to demonstrate how APS plans and
authorises work end-to-end.

## Success Criteria

- [ ] A 25-minute work interval counts down and switches to a 5-minute break automatically
- [ ] Start, pause, and reset controls behave correctly
- [ ] The page is served on localhost
- [ ] Completed sessions are tallied and a phase change is signalled

## Constraints

- No build step — plain HTML/CSS/JS served statically
- No Node runtime on the machine — validation uses Python 3 and curl

## Modules

| Module                             | Purpose            | Status | Dependencies |
| ---------------------------------- | ------------------ | ------ | ------------ |
| [pomodoro](./modules/01-pomodoro.aps.md) | The timer app | Draft  | —            |

## Risks

| Risk                                    | Impact                    | Mitigation                              |
| --------------------------------------- | ------------------------- | --------------------------------------- |
| No Node means no headless JS unit tests | Weaker browser-logic coverage | DOM-free engine + structural contract checks + serve check |

## Open Questions

- [ ] Should the work/break durations be user-configurable? (deferred — out of scope for the demo)

## Decisions

- **D-001:** Static single-page app, no framework — _decided_
