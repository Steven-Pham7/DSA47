class Food_Data:
    """
    The class that will function as the data structure for our data.
    """
    def __init__(self, length):
        """
        Initializes the multiMap_Data class with the initial arrays and dictionaries empty.
        :param int length: The number of nutrients that the interface would have.
        """
        # This is the dictionary that will store the food data. It will be a dictionary of lists where the key is the ID
        # of the food item and the value would be food data as a list. The dictionary is not sorted. This Data cannot be
        # accessed directly.
        self._data = dict()
        # This array will hold a list of arrays where each inner array is an array of tuples. The tuples will contain
        # two elements the value of the nutrient and the ID of the food item. While the value of the nutrient may not be
        # unique the ID will be. The inner arrays will be sorted based on the value of the nutrient selected. The outer
        # array will not be sorted.
        self.interface = list()
        # Initializes all the inner arrays.
        self._initialize_interface(length)
        # The file path of the raw data.
        self.filePath = "../Data/food.csv"

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
        # Add the nutrient-ID tuple to the respective inner array.
        for i in range(len(self.interface)):
            if Data[i+3] in self.interface[i].keys():
                self.interface[i][Data[i+3]].append(Data[i+3])
            else:
                self.interface[i][Data[i+3]] = [Data[i+3]]

    def _initialize_interface(self, length):
        """
        Initializes all the inner arrays to empty.
        :param int length: The number of inner arrays needed.
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





