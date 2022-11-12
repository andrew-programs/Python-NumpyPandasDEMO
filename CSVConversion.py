from dataclasses import dataclass
import csv

def toRows(filePath: str) -> list[list]:
    """Converts CSV file to rows in a list."""
    with open(filePath, "r") as csvFile:
        rows = list(csv.reader(csvFile))

    return rows

def toColumns(filePath: str) -> list[list]:
    """Converts CSV file to columns in a list."""
    with open(filePath, "r") as csvFile:
        rows = list(csv.reader(csvFile))
    
    columns = []
    for index in range(len(rows[0])):
        columns.append([row[index] for row in rows])
    
    return columns

def selectRow(csvData: list[list], index) -> list:
    """Allows you to pass in a list of rows and select a row."""
    return csvData[index]

def selectColumn(csvData: list[list], index: int) -> list:
    """Allows you to pass in a list of rows and select a row."""
    return [list[index] for list in csvData]