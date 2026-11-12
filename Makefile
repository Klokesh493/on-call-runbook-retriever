PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) -B -m unittest discover -v
	$(PYTHON) retrieve.py "kafka consumer lag"

.PHONY: replay
replay:
	$(PYTHON) tools/replay_examples.py --report reports/replay.md
