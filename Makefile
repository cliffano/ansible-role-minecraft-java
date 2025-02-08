ci: deps lint test

export PATH := .venv/bin:$(PATH)

deps:
	python3 -m venv .venv && . .venv/bin/activate && python3 -m pip install -r requirements.txt

lint:
	molecule lint

gen-vars-file:
	python3 scripts/gen-vars-file.py

test:
	molecule test

.PHONY: ci deps lint gen-vars-file test
