# AGENTS.md

This repository uses **Anvil Plan Spec (APS)** for planning and task
authorisation. Plans are the source of truth and live in `plans/`.

## Rules for agents

- Read `plans/aps-rules.md` before planning or executing work.
- The plan is **non-executable intent** until a work item is `Ready`.
- A work item with status `Ready` is your **authorisation** to implement.
  No `Ready` item → do not start changing code.
- Every work item has an `Intent`, `Expected Outcome`, and a `Validation`
  command. Completion is not "the agent stopped" — it is the validation
  command passing.
- Use the `aps` CLI to drive the loop:
  - `aps next` — find the next authorised work item
  - `aps start <ID>` — mark In Progress and build focused context
  - `aps complete <ID> --learning "..."` — record completion + a learning
  - `aps lint plans` — validate plan structure
- Record new work as `Draft`; only a human decision promotes it to `Ready`.
