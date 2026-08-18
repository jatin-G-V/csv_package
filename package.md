# csvstat

A simple Python package for analyzing CSV files and generating basic statistics.

## Installation

Install the package using pip:

```bash
pip install -i https://pypi.org/simple/ csvstat-jg

```
# Usage

```python
from csvstat import numeric_stats

result = numeric_stats("test.csv", "age")
print(result)
```
# Available Functions


#### number_Of_Rows(path) 
Returns the number of rows in the CSV file

#### number_Of_Columns(path)	
Returns the number of columns in the CSV file

#### value_type(value)	
Identifies the type of a value
#### columns(path)	
Returns the column names
#### column_values(path, column_name)
Returns values from a specific column
#### numeric_column_values(path, column_name)	
Returns numeric values from a specific column
#### column_type(path, column_name)	
Returns the type of a specific column
#### table_info(path)	
Returns column names and their types
#### numeric_stats(path, column_name)	
Returns min, max, and mean for a numeric column
#### numeric_columns_stats(path)	
Returns statistics for all numeric columns
#### most_frequent_values(path, column_name, limit)	
Returns the most frequent values of a column
#### frequent_values_all_columns(path, limit)	
Returns frequent values for all columns
#### missing_values(path)	
Returns missing value count and percentage for each column


# Example
```python
from csvstat import (
    number_Of_Rows,
    number_Of_Columns,
    table_info,
    numeric_stats,
    missing_values
)

path = "test.csv"

print(number_Of_Rows(path))
print(number_Of_Columns(path))
print(table_info(path))
print(numeric_stats(path, "age"))
print(missing_values(path))
```

# Requirements

#### Python 3.8+
#### No external dependencies
