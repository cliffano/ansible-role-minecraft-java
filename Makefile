ci: deps lint test

define python_venv
	python3 -m venv .venv && . .venv/bin/activate && $(1)
endef

deps:
	$(call python_venv,python3 -m pip install -r requirements.txt)

lint:
	$(call python_venv,molecule lint)

gen-vars-file:
	$(call python_venv,python3 scripts/gen-vars-file.py)

test:
	$(call python_venv,molecule test)

.PHONY: ci deps lint gen-vars-file test
