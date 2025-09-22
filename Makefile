PY := python
PIP := $(PY) -m pip

.PHONY: help venv deps dev test clean

help:
	@echo "Available targets:"
	@echo "  venv   - create virtual environment (./venv)"
	@echo "  deps   - install runtime deps (requirements.txt)"
	@echo "  dev    - install dev deps (requirements-dev.txt)"
	@echo "  test   - run pytest quietly"
	@echo "  clean  - remove caches and build artifacts"

venv:
	$(PY) -m venv venv
	@echo "Run: source venv/bin/activate  # Windows: venv\\Scripts\\activate"

deps:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

dev: deps
	$(PIP) install -r requirements-dev.txt

test:
	$(PY) -m pytest -q

clean:
	rm -rf .pytest_cache htmlcov .coverage __pycache__ */__pycache__

