from csvstat.core import (
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
    missing_values,
)


CSV_PATH = "tests/test.csv"


def test_number_of_rows():
    assert number_Of_Rows(CSV_PATH) == 9


def test_number_of_columns():
    assert number_Of_Columns(CSV_PATH) == 6


def test_value_type():
    assert value_type("21") == "int"
    assert value_type("50000") == "int"
    assert value_type("50.5") == "float"
    assert value_type("2024-01-15") == "date"
    assert value_type("Jatin") == "str"


def test_columns():
    assert columns(CSV_PATH) == [
        "Name",
        "Age",
        "Salary",
        "Department",
        "Joining_Date",
        "City",
    ]


def test_column_values():
    assert column_values(CSV_PATH, "Name") == [
        "Jatin",
        "Rahul",
        "Priya",
        "Aman",
        "Neha",
        "Rohan",
        "Simran",
        "Karan",
    ]


def test_numeric_column_values():
    assert numeric_column_values(CSV_PATH, "Age") == [
        21.0,
        22.0,
        21.0,
        24.0,
        23.0,
        22.0,
        25.0,
    ]


def test_invalid_column_values():
    result = column_values(CSV_PATH, "Invalid")

    assert result == "Error: Column 'Invalid' not found in the CSV file."


def test_column_type():
    assert column_type(CSV_PATH, "Name") == "str"
    assert column_type(CSV_PATH, "Age") == "int"
    assert column_type(CSV_PATH, "Salary") == "int"
    assert column_type(CSV_PATH, "Department") == "str"
    assert column_type(CSV_PATH, "Joining_Date") == "date"
    assert column_type(CSV_PATH, "City") == "str"


def test_table_info():
    assert table_info(CSV_PATH) == {
        "Name": "str",
        "Age": "int",
        "Salary": "int",
        "Department": "str",
        "Joining_Date": "date",
        "City": "str",
    }


def test_numeric_stats_age():
    result = numeric_stats(CSV_PATH, "Age")

    assert result["min"] == 21.0
    assert result["max"] == 25.0
    assert result["mean"] == 22.571428571428573


def test_numeric_stats_salary():
    result = numeric_stats(CSV_PATH, "Salary")

    assert result["min"] == 45000.0
    assert result["max"] == 70000.0
    assert result["mean"] == 56428.57142857143

def test_numeric_columns_stats():
    result = numeric_columns_stats(CSV_PATH)

    assert result == {
        "Age": {
            "min": 21.0,
            "max": 25.0,
            "mean": 22.571428571428573,
        },
        "Salary": {
            "min": 45000.0,
            "max": 70000.0,
            "mean": 56428.57142857143,
        },
    }


def test_most_frequent_values():
    assert most_frequent_values(CSV_PATH, "Department", 2) == {
        "IT": 4,
        "HR": 2,
    }


def test_frequent_values_all_columns():
    result = frequent_values_all_columns(CSV_PATH, 2)

    assert result["Department"] == {
        "IT": 4,
        "HR": 2,
    }

    assert result["City"] == {
        "Pune": 4,
        "Delhi": 2,
    }

    assert result["Age"] == {
        "21": 2,
        "22": 2,
    }


def test_missing_values():
    result = missing_values(CSV_PATH)

    assert result["Age"] == {
        "missing_count": 1,
        "missing_percentage": 12.5,
    }

    assert result["Salary"] == {
        "missing_count": 1,
        "missing_percentage": 12.5,
    }

    assert result["Name"] == {
        "missing_count": 0,
        "missing_percentage": 0.0,
    }