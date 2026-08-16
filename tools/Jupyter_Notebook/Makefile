PYTHON := /usr/bin/python3
ENV_PYTHON := .venv/bin/python3
ENV_PIP := .venv/bin/pip

install:
	@echo Opening a local Jupyter Notebook ...
	$(PYTHON) -m venv .venv
	$(ENV_PIP) install notebook
	$(ENV_PYTHON) -m notebook

run: 
	$(ENV_PYTHON) -m notebook

clean:
	rm -rf .venv