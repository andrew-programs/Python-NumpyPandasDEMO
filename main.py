import pandas
import numpy
from matplotlib import pyplot

def main() -> None:
    x = numpy.array([1, 2, 3, 4, 5, 6, 7])
    y = numpy.array([13, 52, 10, 0 , 1, 41, 97])

    dataFrame = pandas.DataFrame(y, x)
    pyplot.plot(dataFrame)
    pyplot.show()

if __name__ == "__main__":
    main()