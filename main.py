import matplotlib.pyplot as pyplot
import CSVConversion as conv
import pandas
import numpy
import csv

def main(xInput: str, yInput: str) -> None:
    cols = conv.toColumns("./input/bankdata.csv")
    headerRow = [cols[index].pop(0) for index in range(len(cols))]
    
    if xInput in headerRow and yInput in headerRow:
        try:
            dataFrame = pandas.DataFrame(rows, columns=headerRow)
            dataFrame.plot()
        except Exception as e:
            print(f"Exception raised: {e}")
    else:
        raise ValueError("Either the x-value or y-value was not found within the header row, please double check capitalization/spelling.")

if __name__ == "__main__":
    xInput = input("What would you like the x-value to be? > ")
    yInput = input("What would you like the y-value to be? > ")

    main(xInput, yInput)