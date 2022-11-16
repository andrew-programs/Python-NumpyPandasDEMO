import matplotlib.pyplot as pyplot
import CSVConversion as conv
import pandas
import numpy

def main() -> None:
    rows = conv.toRows("./input/bankdata.csv")
    headerRow = rows.pop(0)
    
    try:
        dataFrame = pandas.DataFrame(rows, columns=headerRow)
    except Exception as e:
        print(f"Exception raised: {e}")
    
    x = numpy.array(list(range(len(dataFrame["Posting Date"]))))
    y = numpy.array(list(map(float, dataFrame["Balance"])))

    pyplot.plot(x, y)
    print(y.mean())
    pyplot.show() 

if __name__ == "__main__":
    main()