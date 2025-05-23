import pandas as pd
from Data_Parsing.multiMap_data import Food_Data

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
    data = Food_Data(len(labels), offset, idColumn)
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


def pretitfyLabels(labelFilePath, offset):
    """
    Takes the file path of the labels and return a list of variables \"prettified\" .
    :param string labelFilePath: The file path of the labels cvs file.
    :param int offset: The number of labels not included in the interface.
    :rtype: list[string]
    :returns: A list of the labels of the nutrients.
    """
    # Read the label csv.
    labels = pd.read_csv(labelFilePath).columns
    prettyLabels = []
    # "Prettify" the labels by removing the classification from the nutrient names.
    for label in labels[offset:]:
        temp = label.replace("Data.",'')
        temp = temp.replace("Fat.", '')
        temp = temp.replace("Major Minerals.", '')
        temp = temp.replace("Vitamins.", '')
        prettyLabels.append(temp)
    return prettyLabels


def getMaxValues(FoodData, labels, offset):
    """
    Get the max values of the specified data and combine it in a dictionary with their respective labels.
    :param Food_Data FoodData: The data that contains the nutrients.
    :param list[string] labels: The list of labels.
    :param int offset: If non-interface nutrients are in the list then the offset is the number of these nutrients else
        0.
    :rtype: dict[string, float]
    :return: A dictionary of max values with the label as the key and the maximum values as the value.
    """
    # Gets all the max values.
    maxValues = FoodData.get_Max_Interface()
    answer = dict()
    # Packages the max values and the labels together.
    for maxValue, label in zip(maxValues, labels[offset:]):
        answer[label] = maxValue
    return answer
