# On Call Runbook Retriever walkthrough

## Business problem

Responders need a cited runbook for incident symptoms and an explicit review outcome when the local catalog provides weak evidence.

## Reproduce the workflow

Run `python3 retrieve.py "kafka consumer lag"` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
{
  "decision": "suggest",
  "citation": "KAFKA-01",
  "next_step": "Check consumer lag by partition and compare with input rate."
}
```

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
