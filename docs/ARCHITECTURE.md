# On Call Runbook Retriever architecture

An offline Python lab for on-call responders. It ranks synthetic runbooks with TF-IDF cosine similarity, cites a matching runbook, and asks for review when the match is weak or tied.

```mermaid
flowchart LR
    A["Incident symptoms and local runbook catalog"]
    B["Rank documents by lexical similarity"]
    C{"Best score clears threshold and is unique?"}
    D["Return runbook citation and next step"]
    E["Request operator review"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
