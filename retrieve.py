"""Retrieve a cited runbook with TF-IDF cosine similarity."""
import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path


def tokens(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def retrieve(query, runbooks, threshold=0.25):
    if not runbooks or not 0 < threshold <= 1:
        raise ValueError("provide runbooks and a threshold in (0, 1]")
    documents = [Counter(tokens(book["symptoms"])) for book in runbooks]
    frequency = Counter(word for document in documents for word in document)

    def vector(counts):
        return {word: count * (1 + math.log((1 + len(documents)) /
                                            (1 + frequency[word])))
                for word, count in counts.items()}

    def similarity(left, right):
        denominator = math.hypot(*left.values()) * math.hypot(*right.values())
        return sum(value * right.get(word, 0) for word, value in left.items()) / denominator if denominator else 0

    query_vector = vector(Counter(tokens(query)))
    scores = [similarity(query_vector, vector(document)) for document in documents]
    rank = sorted(range(len(scores)), key=lambda index: (-scores[index], runbooks[index]["id"]))
    best = rank[0]
    if scores[best] < threshold or (len(rank) > 1 and math.isclose(scores[best], scores[rank[1]])):
        return {"decision": "review", "citation": None}
    book = runbooks[best]
    return {"decision": "suggest", "citation": book["id"], "next_step": book["next_step"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--runbooks", type=Path, default=Path(__file__).with_name("runbooks.json"))
    args = parser.parse_args()
    print(json.dumps(retrieve(args.query, json.loads(args.runbooks.read_text())), indent=2))
