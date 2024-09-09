ci: deps lint test

deps:
	pip3 install -r requirements.txt

lint:
	molecule lint

gen-vars-file:
	python3 scripts/gen-vars-file.py

test:
	molecule test

.PHONY: ci deps lint gen-vars-file test