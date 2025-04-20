.PHONY: requirements sca lint format

# Generate requirements.txt from requirements.in
requirements:
	pip-compile requirements.in --output-file=requirements.txt

# Run ruff to format and check code
sca: format lint

# Linting with ruff
lint:
	ruff check .

# Format code with ruff
format:
	ruff format .
