# On Call Runbook Retriever walkthrough

## Business problem

An offline Python lab for on-call responders. It ranks synthetic runbooks with TF-IDF cosine similarity, cites a matching runbook, and asks for review when the match is weak or tied.

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
