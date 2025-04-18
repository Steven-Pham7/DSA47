import pandas as pd
import numpy
from multiMap_data import Food_Data


def Parse_data(filePath):
    df = pd.read_csv(filePath)
    data = Food_Data(1)
    names = ["Category","Description","Nutrient Data Bank Number","Data.Alpha Carotene"]
    for index in df.index:
        row = df.loc[index]
        temp = []
        for lable in names:
            temp.append(row[lable])
        data.add_data(temp)
    data.sort_interface()
    print(data.interface)


Parse_data("../Data/food.csv")
