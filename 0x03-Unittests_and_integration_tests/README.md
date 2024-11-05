# Unittests and Integration Tests Project

## Overview
This project demonstrates how to write unit and integration tests using Python's `unittest` framework. It includes multiple tests that mock external API calls, use parameterization, and ensure that key functionalities in the code are correctly validated.

## Requirements
- Python 3.7
- pytest, unittest, parameterized

## Files
- `utils.py`: Contains utility functions for accessing nested maps, HTTP requests, and memoization.
- `test_utils.py`: Contains unit tests for the utility functions in `utils.py`.
- `test_client.py`: Contains tests for the `GithubOrgClient` class.
- `fixtures.py`: Mock data used in integration tests.
