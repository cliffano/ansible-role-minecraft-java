ci: deps lint test

deps:
	python3 -m venv .venv && . .venv/bin/activate && python3 -m pip install -r requirements.txt

lint:
	.venv/bin/molecule lint

gen-vars-file:
	python3 -m venv .venv && . .venv/bin/activate && python3 scripts/gen-vars-file.py

test:
	.venv/bin/molecule test

.PHONY: ci deps lint gen-vars-file test
