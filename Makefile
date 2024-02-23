.PHONY: unit_test, manual_test, run

unit_test:
	PYTHONPATH=src pytest tests/unit_tests

run:
	PYTHONPATH=src python3 src/main.py

manual_test:
	PYTHONPATH=src python3 tests/manual_tests/test_api_flow.py
