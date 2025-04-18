import pandas as pd
from multiMap_data import Food_Data


def Parse_data(filePath, labelFilePath, offset, idColumn):
    """
    Takes a csv sheet of the data and filters the data we want from every food item. Lastly it inserts the data into the
    Food_Data data structure. Warning does not take into account missing values.
    :param str filePath: A string containing the file path for the data.
    :param str labelFilePath: A string containing the file path for the columns we which to include. Assuming the column
        named are listed in a one-dimensional csv.
    :param int offset: The number of columns that should not be included in the interface but should be in the data.
    :param int idColumn: The index of the column where a unique id is held in the data csv file.
    :rtype: Food_Data
    :returns: A Food_Data instance containing all the data in the filePath csv with the columns being the data in
        labelFilePath csv.
    """
    # Reads the csv files but only grabs the columns from the label file.
    df = pd.read_csv(filePath)
    labels = pd.read_csv(labelFilePath).columns
    # Initializes our return value. It assumes that the non-interface columns are at the beginning of the csv file for
    # both file paths.
    data = Food_Data(len(labels)-offset)
    # Takes the value of the data at a specific row with columns specified by label file and adds them to the instance '
    # of food data.
    for index in df.index:
        row = df.loc[index]
        temp = []
        for label in labels:
            temp.append(row[label])
        data.add_data(temp)
    # Sorts the interface.
    data.sort_interface()
    return data

