# csvstat-jatin

A simple Python package for analyzing CSV files and generating basic statistics.

## Overview

`csvstat-jatin` provides reusable functions for analyzing CSV files without requiring external runtime dependencies.

The package supports:

* Row and column counting
* Column and value extraction
* Data type detection
* Numeric statistics
* Frequently occurring values
* Missing value analysis

## Project Structure

```text
csvstat/
│
├── csvstat/
│   ├── __init__.py
│   └── core.py
│
├── tests/
│   ├── test.csv
│   └── test_core.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── pyproject.toml
```

## Available Functions

| Function                                         | Description                                |
| ------------------------------------------------ | ------------------------------------------ |
| `number_Of_Rows(path)`                           | Returns the number of rows                 |
| `number_Of_Columns(path)`                        | Returns the number of columns              |
| `value_type(value)`                              | Identifies the type of a value             |
| `columns(path)`                                  | Returns column names                       |
| `column_values(path, column_name)`               | Returns values from a specific column      |
| `numeric_column_values(path, column_name)`       | Returns numeric values from a column       |
| `column_type(path, column_name)`                 | Returns the type of a column               |
| `table_info(path)`                               | Returns column names and their types       |
| `numeric_stats(path, column_name)`               | Returns minimum, maximum, and mean         |
| `numeric_columns_stats(path)`                    | Returns statistics for all numeric columns |
| `most_frequent_values(path, column_name, limit)` | Returns the most frequent values           |
| `frequent_values_all_columns(path, limit)`       | Returns frequent values for all columns    |
| `missing_values(path)`                           | Returns missing count and percentage       |

## Package Creation

The project follows a standard Python package structure with reusable CSV analysis functions separated from the test suite.

The functions are implemented in `core.py` and exported through `__init__.py`, allowing direct imports such as:

```python
from csvstat import numeric_stats
```

## Development Setup

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the package in editable mode:

```bash
pip install -e .
```

## Unit Testing

The package uses `pytest` for unit testing.

Run the complete test suite using:

```bash
pytest
```

The test suite contains 15 test cases covering:

* Row counting
* Column counting
* Value type detection
* Column extraction
* Numeric value extraction
* Column type detection
* Table information
* Numeric statistics
* Frequent values
* Missing value analysis
* Invalid column handling

All 15 tests passed successfully:

```text
15 passed
```

## Building the Package

Install the build tool:

```bash
pip install build
```

Build the package:

```bash
python -m build
```

The build generates source and wheel distributions inside the `dist/` directory.

## Package Validation

Twine is used to validate the generated distributions:

```bash
python -m pip install twine
python -m twine check dist/*
```

Both generated distributions passed validation successfully.

## Publishing to PyPI

The package was published to PyPI using Twine and a PyPI API token:

```bash
python -m twine upload dist/*
```

PyPI API-token authentication uses:

```text
Username: __token__
Password: <PyPI API token>
```

The original upload issue was caused by using a package name that was already registered on PyPI. The package was renamed to a unique name and the issue was resolved.

## Installation

After publication, the package can be installed directly from PyPI using:

```bash
python -m pip install csvstat-jatin
```

## Usage

```python
from csvstat import numeric_stats

result = numeric_stats("test.csv", "age")
print(result)
```

Other functions can also be imported directly:

```python
from csvstat import table_info
from csvstat import missing_values
from csvstat import frequent_values_all_columns
```

## Requirements

* Python 3.8+
* No external runtime dependencies
* `pytest` is used for unit testing

## Author

Jatin Garg
