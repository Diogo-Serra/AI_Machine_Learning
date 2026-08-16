ENV_PYTHON := .venv/bin/python3
ENV_PIP := .venv/bin/pip

install:
	@echo Preparing environment...
	python3 -m venv .venv
	$(ENV_PIP) install -r requirements.txt

clean:
	rm -rf .venv
