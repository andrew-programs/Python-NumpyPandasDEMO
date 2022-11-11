from dataclasses import dataclass
import csv

@dataclass(frozen=True)
class CSVData:
    # Class representing csv data
    def toRows(self, filePath: str) -> list[list]:
        with open(filePath, "r") as csvFile:
            rows = list(csv.reader(csvFile))

        return rows

    def toColumns(self, filePath) -> list[list]:
        with open(filePath, "r") as csvFile:
            rows = list(csv.reader(csvFile))
        
        raise NotImplementedError("Not Finished")

    def selectRow(self, rows: list[list], index) -> list:
        return rows[index]
    
    def selectColumn(self, rows: list[list], index: int) -> list:
        return [row[index] for row in rows]

def main() -> None:
    csvData = CSVData()
    csvRows = csvData.toRows("./input/bankdata.csv")
    csvColumns = csvData.selectColumn(csvRows, 3)
    
    print(csvColumns)

if __name__ == "__main__":
    main()