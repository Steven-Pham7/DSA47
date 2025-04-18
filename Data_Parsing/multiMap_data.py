from sortedcontainers import sorteddict


class Food_Data:
    """
    The class that will function as the data structure for our data.
    """
    def __init__(self, length, offset, idColumn):
        """
        Initializes the multiMap_Data class with the initial arrays and dictionaries empty.
        :param int length: The number of nutrients that the interface would have.
        :param int offset: The number of columns in the data but not the interface.
        :param int idColumn: The index of the column where a unique id is held.
        """
        # This is the dictionary that will store the food data. It will be a dictionary of lists where the key is the ID
        # of the food item and the value would be food data as a list. The dictionary is not sorted. This Data cannot be
        # accessed directly.
        self._data = dict()
        # This array will hold a list of dictionaries which each correspond to a specific nutrient. The keys in the
        # dictionaries would be the value for that nutrition and the value in the pair would be a list of the id's of
        # the food items that correspond to the nutritional value. The outer array is not sorted but the dictionaries
        # are sorted by their keys. The list of IDs are not sorted.
        self.interface = list()
        # Initializes all the inner arrays.
        self._initialize_interface(length-offset)
        # The offset representing how many columns are in the data and not in the interface. Will assume that these
        # columns are all towards the start of the data.
        self._offset = offset
        # Initialize the index of the id column.
        self._idColumn = idColumn

    def add_data(self, Data):
        """
        Adds the list of nutrients of the food specified in Data to the base dictionary and the interface. Warning: does
        not check if the nutrients in the input match the ones currently in the dataset. It also does not check if they
        are in the correct order either.
        :param list Data: A list of data corresponding to a specific food item.
        :rtype: None
        :raises ValueError: Will throw an exception if the data has more or less nutrients than what the class was
            initialized with.
        """
        # Throws and exception if there is more or less nutrients in the data then in the interface.
        if len(Data) - 3 != len(self.interface):
            raise ValueError("The number of nutrients in the data is not the same as what the interface was initialized"
                             + "with.")
        # Since each food item has a unique ID it creates a new key-value pair for the food item.
        self._data[Data[2]] = Data
        # Adds the ID to the nutrient list otherwise adds a new key value pair that is nutrient value for the key and
        # a list of food ids.
        for i in range(len(self.interface)):
            if Data[i+3] in self.interface[i].keys():
                self.interface[i][Data[i+self._offset]].append(Data[self._idColumn])
            else:
                self.interface[i][Data[i+self._offset]] = [Data[self._idColumn]]

    def _initialize_interface(self, length):
        """
        Initializes all the inner dictionaries to empty.
        :param int length: The number of dictionaries needed.
        """
        for i in range(length):
            self.interface.append(dict())

    def get_data(self, ID):
        """
        Return the food item of the specified ID.
        :param int ID: ID of the item.
        :return: Returns the data as a List.
        :rtype: list
        :raises KeyError: If the ID does not exist in the data.
        """
        return self._data[ID]

    def sort_interface(self):
        """
        Sorts the interface using the sortedcontainers library. Link: https://pypi.org/project/sortedcontainers/
        """
        for i in range(len(self.interface)):
            self.interface[i] = sorteddict.SortedDict(self.interface[i])

    def get_Max_Interface(self):
        answer = []
        for nutrient in self.interface:
            answer.append(nutrient.keys()[-1])
        return answer
