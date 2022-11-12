from matplotlib import pyplot
import CSVConversion as conv
import pandas
import numpy
import csv

def main() -> None:
    rows = numpy.array(conv.toRows("./input/bankdata.csv"))
    dataFrame = pandas.DataFrame(rows)
    
    print(dataFrame)
    

if __name__ == "__main__":
    main()