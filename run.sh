#!/bin/bash

source venv/Scripts/activate

echo "Running test suite..."
pytest test_app.py

TEST_EXIT_CODE=$?

if [ $TEST_EXIT_CODE -eq 0 ]; then
  echo "Success: All tests passed!"
  exit 0
else
  echo "Error: Test suite failed."
  exit 1
fi