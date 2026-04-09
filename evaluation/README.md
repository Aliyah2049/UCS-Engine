# Evaluation Data

This folder contains logs and results from UCS Engine evaluation runs.

## logs/

JSONL-format event logs recorded during model evaluation sessions.

Each log file captures prompt inputs, threat detection decisions, layer activations, and outcome classifications across a range of test scenarios — both adversarial and non-adversarial.

| File pattern | Description |
|---|---|
| `ucse_events.jsonl` | Core UCS Engine event log |
| `ucs_analysis_YYYYMMDD_HHMMSS.jsonl` | Timestamped analysis run logs |

### Log Format

Each line is a JSON object with fields including:
- `timestamp` — event time
- `prompt_hash` — anonymised prompt identifier
- `layer_activations` — which protection layers were triggered
- `action` — final policy decision (ALLOW / BLOCK / EDUCATE)
- `context_type` — prompt category classification
- `threat_score` — Layer 1 detection confidence

## Notes

- All evaluation was conducted independently using personal API access and local deployments
- No personally identifiable information is included in these logs
- Logs represent a subset of total evaluation runs, selected for documentation purposes
