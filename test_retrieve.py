import json
import unittest
from pathlib import Path

from retrieve import retrieve


class RetrieveTests(unittest.TestCase):
    books = json.loads(Path(__file__).with_name("runbooks.json").read_text())

    def test_returns_cited_kafka_runbook(self):
        self.assertEqual(retrieve("kafka consumer lag", self.books)["citation"], "KAFKA-01")

    def test_out_of_scope_abstains(self):
        self.assertEqual(retrieve("printer toner", self.books),
                         {"decision": "review", "citation": None})

    def test_tie_abstains(self):
        self.assertEqual(retrieve("lag", self.books * 2)["decision"], "review")

    def test_empty_query_abstains(self):
        self.assertEqual(retrieve("", self.books)["decision"], "review")
