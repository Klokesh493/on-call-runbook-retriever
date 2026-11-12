# On Call Runbook Retriever architecture

An offline Python lab for on-call responders. It ranks synthetic runbooks with TF-IDF cosine similarity, cites a matching runbook, and asks for review when the match is weak or tied.

```mermaid
flowchart LR
    N0["CLI arguments"]
    N1["retrieve.py"]
    N2["Rank runbooks with lexical similarity and defer weak or tied results to an operator."]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
