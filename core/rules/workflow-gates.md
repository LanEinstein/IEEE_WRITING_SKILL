<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Workflow Gates (G16): Propose, Wait for Approval, Then Act

These are the hard process rules of the suite. They are not style advice: a
workflow that skips a gate is a broken run, regardless of output quality.

## The propose-then-go discipline (applies to ieee-write and ieee-polish)

1. **Never edit a manuscript file directly.** For every proposed change,
   present a proposal first:
   - a table of `original -> proposed` for each affected sentence, plus
   - a one-line rationale per change, naming the rule ID (G/S/D) that
     motivates the change.
2. **Wait for an explicit approval token** from the user (`go`, `implement`,
   or an equivalent unambiguous instruction) before applying anything.
   Silence, partial comments, or questions are NOT approval. If the user
   modifies a proposal, re-present the modified version and wait again.
3. **One paragraph at a time.** Draft or polish exactly one paragraph per
   proposal cycle. Never batch several paragraphs into one approval, and
   never continue to the next paragraph before the current one is approved.

## Mandatory gates by workflow

| Gate | Where | Condition to pass |
|---|---|---|
| Outline approval | ieee-write, after the outline | The user explicitly states the outline review has passed. Iterate on feedback until that statement is given. |
| Per-paragraph go | ieee-write drafting, ieee-polish editing | Explicit `go` for the current paragraph. |
| Polish consent | ieee-polish entry (when suggested after writing) | The user accepts the polish offer. |
| Big-action page | any workflow | Before any long compilation batch, any external upload, or any action outside the paper directory, state the intent and wait for consent. |

## Editor-buffer overwrite guard

After applying an approved edit, re-read the modified region and confirm the
new text is present. If a later read shows the old text again, an IDE buffer
has overwritten the change from a stale copy. Stop immediately, list the
affected edits by content comparison (line numbers drift and cannot be
trusted), and ask the user to reload the file in the editor before re-applying.

## Reporting discipline

- Report outcomes faithfully: if a compilation fails or a check finds
  violations, report the real output. Never describe a skipped step as done.
- The numbers iron rule of `core/rules/verification-protocol.md` (V4) applies
  to every gate report: no number appears in a deliverable before the tool
  output that produced the number has been observed.
