# Replay evidence

Captured stdout is compared with a checked-in baseline.

## Demo 1

Result: **PASS**

````text
{
  "decision": "suggest",
  "citation": "KAFKA-01",
  "next_step": "Check consumer lag by partition and compare with input rate."
}
````

## Weak match

Result: **PASS**

````text
{
  "decision": "review",
  "citation": null
}
````
