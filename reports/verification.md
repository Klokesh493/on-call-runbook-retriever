# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 retrieve.py "kafka consumer lag"
{
  "decision": "suggest",
  "citation": "KAFKA-01",
  "next_step": "Check consumer lag by partition and compare with input rate."
}
test_empty_query_abstains (test_retrieve.RetrieveTests) ... ok
test_out_of_scope_abstains (test_retrieve.RetrieveTests) ... ok
test_returns_cited_kafka_runbook (test_retrieve.RetrieveTests) ... ok
test_tie_abstains (test_retrieve.RetrieveTests) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
````
