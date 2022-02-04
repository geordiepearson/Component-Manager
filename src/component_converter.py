"""
Module containing all functionality to convert data into component models
"""
import os
import csv
import json
import digikey
from digikey.v3.productinformation import KeywordSearchRequest

from components import *

# Indexes for CSV data in list format
CSV_DESCRIPTION_INDEX = 0
CSV_PART_NUMBER_INDEX = 1

# Indexes for description data access
DESCRIPTION_TYPE_INDEX = 0
DESCRIPTION_VALUE_INDEX = 1

class ComponentConverter():
    """ Utility class to handle all creation of component models from CSV data

    Parameters:
        - file_name: The name of the CSV file to convert

    Attributes:
        - components: The list of components converted from the given CSV data
        - data: The data stored in the CSV file, stored as a 2D list
        - current_row: The index of the row currently being manipulated
    """
    def __init__(self, file_name):
        self._current_row = 0
        self._data = None
        self._components = []
        self.read_file(file_name)

    def read_file(self, file_name):
        """ Reads the given file and stores the resulting data in a 2D list

        Parameters
          - file_name: The name of the CSV file to convert
        """
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for i in range(0): next(reader)
            self._data = list(csv.reader(file))
            self._current_row = 0

    def component_search(self, component):
        """ Searches for component information and if the component is found, updates the given
            component with the search results

        Parameters:
            - component: The component to update with the search results

        Returns: True if the part is found, otherwise False
        """
        if component is None:
            return False

        search_request = KeywordSearchRequest(keywords=component._name, record_count=1)
        result = digikey.keyword_search(body=search_request) 
        if result.products == []:
            return False
        else:
            for parameter in result.products[0]._parameters:
                if parameter.parameter_id in component._parameters:
                    component._parameters[parameter.parameter_id] = parameter.value
            return True

    def data_to_component(self, component_data):
        """ Converts data retrieved from a CSV file to a component object.

        Returns: The created component object
        """
        component = None

        if component_data[CSV_DESCRIPTION_INDEX].split(", ")[DESCRIPTION_TYPE_INDEX] == "Resistor":
            component = Resistor(component_data[CSV_PART_NUMBER_INDEX])        
        elif component_data[CSV_DESCRIPTION_INDEX].split(", ")[DESCRIPTION_TYPE_INDEX] == "Capacitor":
            component = Capacitor(component_data[CSV_PART_NUMBER_INDEX])
        else:
            return component_data[CSV_PART_NUMBER_INDEX]

        status = self.component_search(component)
        return component

    def create_component_list(self):
        """ Creates a list of component models based on the given CSV file. """
        i = 0
        while i < len(self._data):
            if (self._data[i][DESCRIPTION_TYPE_INDEX] == "Alternative"):
                self._data[i][DESCRIPTION_TYPE_INDEX] = self._data[i - 1][DESCRIPTION_TYPE_INDEX]

            component = self.data_to_component(self._data[i])
            self._components.append(component)
            i += 1



        
"""
def main():
    test_searcher = ComponentConverter("test.csv")
    test_searcher.create_component_list()
    for i in test_searcher._components:
        print(i)

if __name__ == "__main__":
    main()


def alternative_check(self, data):
        Checks each component in the given data with the suppplied alternative and checks if it
        is a valid alternative based on the component type. Displays to the console if a componenet
        is not an alternative part.

        Parameters:
            - Alternative component data as a 2D list of componenets
        
        i = 0
        while i < len(data):
            original_component = self.data_to_component(data[i])
            data[i + 1][DESCRIPTION_TYPE_INDEX] = data[i][DESCRIPTION_TYPE_INDEX] 
            alternative_component = self.data_to_component(data[i + 1])

            if (original_component is None or alternative_component is None):
                i += 2
                continue

            if not original_component.is_alternative(alternative_component):
                self._print_queue.append("Component " + alternative_component._name +
                                        " is not an alternative for " +
                                        original_component._name + ".")
            i += 2
"""