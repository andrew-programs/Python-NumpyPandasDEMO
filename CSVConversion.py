from dataclasses import dataclass
import csv

# A method that converts csv to a list of rows.
def toRows(filePath: str) -> list[list]:
    """Converts CSV file to rows in a list."""
    with open(filePath, "r") as csvFile:
        rows = list(csv.reader(csvFile))

    return rows

# A method that converts csv to a list of columns.
def toColumns(filePath: str) -> list[list]:
    """Converts CSV file to columns in a list."""
    with open(filePath, "r") as csvFile:
        rows = list(csv.reader(csvFile))
    
    columns = []
    for index in range(len(rows[0])):
        columns.append([row[index] for row in rows])
    
    return columns

# A method that selects a row from a list.
def selectRow(csvData: list[list], index: int) -> list:
    """Allows you to pass in a list of rows and select a row."""
    return csvData[index]

# A method that selects a column from a list
def selectColumn(csvData: list[list], index: int) -> list:
    """Allows you to pass in a list of rows and select a column."""
    return [list[index] for list in csvData]
