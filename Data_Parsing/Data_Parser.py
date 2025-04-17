import pandas
import numpy
from multiMap_data import Food_Data


def Parse_data():
    test = Food_Data(1)
    testData = ["t", "u", 8, 2]
    testData2 = ["t", "u", 4, 3]
    testData3 = ["t", "u", 2, 1]
    test.add_data(testData)
    test.add_data(testData2)
    test.add_data(testData3)
    test.sort_interface()
    print(test.interface)


Parse_data()

