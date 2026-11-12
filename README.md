# On-call Runbook Retriever

An offline Python lab for on-call responders. It ranks synthetic runbooks with TF-IDF cosine similarity, cites a matching runbook, and asks for review when the match is weak or tied.

## Quick start

Run `python3 retrieve.py "kafka consumer lag"` from the repository. The sample returns `KAFKA-01`. Try `python3 retrieve.py "printer toner"` to see the review decision.

## Scope

The lab uses two synthetic runbooks. It makes no external calls. The similarity threshold has no production calibration.
