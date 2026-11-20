<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Claim and protocol records

Use only relevant rows; embed them in an existing facts/workspace file.

| Fact ID | Actual content | Source location and linked version | Status | Supported claim and boundary |
| --- | --- | --- | --- | --- |
| [ID] | [Operation/result] | [Table/label/log/run/page/config] | verified / author-confirmed/run-untraced / pending / conflict / superseded | [Scope and counterexample] |

| Protocol item | Actual operation | Source/state | Consequence for reporting |
| --- | --- | --- | --- |
| Data/sample/labels | [Dataset version, exclusions, mapping] | [Source] | [Evaluated scope] |
| Splits and fitting | [Unit, preprocessing fits, overlap checks] | [Source] | [Selection/test independence] |
| Selection | [Data, objective, epoch/config rule] | [Source] | [Selected vs universal claim] |
| Predictor | [Members, probability/logit/vote, batch/test-time operations] | [Source] | [Actual inference cost/dependence] |
| Aggregation/uncertainty | [Order, repetition unit/count, estimator] | [Source] | [Mean/SD/CI interpretation] |
| Baselines | [Quoted/reproduced/adapted; known differences] | [Source] | [Comparability scope] |

Claim audit: original claim → supporting source → counterevidence → keep/narrow/remove decision → all cross-section locations to update. Author confirmation and runtime verification are distinct states.
