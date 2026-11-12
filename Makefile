PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) -B -m unittest discover -v
	$(PYTHON) retrieve.py "kafka consumer lag"
