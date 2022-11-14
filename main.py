from matplotlib import pyplot
import CSVConversion as conv
import pandas
import numpy
import csv

def main() -> None:
    rows = conv.toRows("./input/bankdata.csv")
    headerRow = [rows[0].pop(index) for index in range(len(rows[0]))]
    dataFrame = pandas.DataFrame(rows, columns=headerRow)

    print(dataFrame)
    

if __name__ == "__main__":
    main()