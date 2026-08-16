# csvstat

A simple Python package for analyzing CSV files and generating basic statistics.

## Overview

`csvstat` provides reusable functions for analyzing CSV files without requiring external dependencies.

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
├── .gitignore
├── README.md
└── pyproject.toml
```

### `core.py`

Contains the main CSV analysis functions.

### `__init__.py`

Exports the functions from `core.py`, allowing them to be imported directly from the package.

Example:

```python
from csvstat import numeric_stats
```

### `pyproject.toml`

Contains the package metadata and build configuration.

### `.gitignore`

Excludes virtual environments, build files, cache files, package metadata, and local test files from the Git repository.

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

### 1. Create the Package Structure

The project was organized using a standard Python package structure.

```text
csvstat/
├── csvstat/
│   ├── __init__.py
│   └── core.py
├── README.md
└── pyproject.toml
```

### 2. Add Functions to `core.py`

The CSV analysis functions were placed inside `core.py`.

The reusable functions are kept separate from the command-line interface code so that they can be imported and used by other Python programs.

### 3. Configure `__init__.py`

The functions from `core.py` were exported through `__init__.py`.

```python
from .core import (
    number_Of_Rows,
    number_Of_Columns,
    value_type,
    columns,
    column_values,
    numeric_column_values,
    column_type,
    table_info,
    numeric_stats,
    numeric_columns_stats,
    most_frequent_values,
    frequent_values_all_columns,
    missing_values
)
```

This allows direct imports such as:

```python
from csvstat import numeric_stats
```

### 4. Configure `pyproject.toml`

The package metadata and build configuration were defined in `pyproject.toml`.

```toml
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "csvstat"
version = "0.1.1"
description = "A Python package for analyzing CSV files"
readme = "README.md"
requires-python = ">=3.8"
authors = [
    {name = "Jatin Garg"}
]

[tool.setuptools.packages.find]
where = ["."]
```

### 5. Create a Virtual Environment

A virtual environment was created for package development.

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

### 6. Install the Package for Development

The package was installed in editable mode:

```bash
pip install -e .
```

### 7. Build the Package

The Python build tool was installed:

```bash
pip install build
```

The package was then built:

```bash
python -m build
```

This generated:

```text
dist/
├── csvstat-0.1.1-py3-none-any.whl
└── csvstat-0.1.1.tar.gz
```

### 8. Validate the Package

Twine was installed for package distribution:

```bash
python -m pip install twine
```

The generated package was checked using:

```bash
python -m twine check dist/*
```

### 9. Publish to TestPyPI

The package was published to TestPyPI using Twine.

```bash
python -m twine upload --repository testpypi dist/*
```

For authentication:

```text
Username: __token__
Password: <TestPyPI API token>
```

The package is available on TestPyPI for distribution and further testing.

## Installing from TestPyPI

Because the package is currently published on **TestPyPI**, it can be installed using:

```bash
python -m pip install --index-url https://test.pypi.org/simple/ csvstat==0.1.1
```

## Usage

After installation:

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
* No external dependencies

## Current Distribution

The package is currently published on **TestPyPI**.

Production PyPI publishing is not included in the current setup.

## Author

Jatin Garg
