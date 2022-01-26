"""
Module containing all utility object for part searchin and handling
"""
import os
import json
import csv
import digikey
from digikey.v3.productinformation import KeywordSearchRequest

from components import *

""" Compares this component with the given component. Returns True if their parameters are
            the same, False otherwise.

            Paramterers:
                - component: The componenet to compare to the current component

            Returns: True if all parameters are equal, false otherwise
        """ 

class PartSearcher():
    """ Utility class to handle all searching functions of the application

    Attributes:
        - print_queue: List of information strings to print at the end of the current operation
    """
    def __init__(self):
        self._print_queue = []
                    
    def search_to_component(self, result, component):
        """ Converts data retrieved from a search to a component object.

        Parameters:
            - result: The results received from a search
            - component: The component to update with the search results
        """
        for parameter in result.exact_manufacturer_products[0]._parameters:
            if parameter.parameter_id in component._parameters:
                component._parameters[parameter.parameter_id] = parameter.value

    def component_search(self, component):
        """ Searches for component information and if the componenet is found, updates the given
            component with the search results

        Parameters:
            - component: The component to update with the search results

        Returns: True if the part is found, otherwise False
        """
        search_request = KeywordSearchRequest(keywords=component._name, record_count=1)
        result = digikey.keyword_search(body=search_request) 
        
        if result.exact_manufacturer_products == []:
            self._print_queue.append("Component " + component._name + " was not found.")
            return False
        else:
            self.search_to_component(result, component)
            return True

    def data_to_component(self, data):
        """ Converts data retrieved from a CSV file to a component object.

        Parameters:
            - data: The component data retrieved from a CSV file

        Returns: The created component if the data is valid, otherwise None
        """
        component = None

        if data[3].split(", ")[0] == "Resistor":
            component = Resistor(data[5])        
        elif data[3].split(", ")[0] == "Capacitor":
            component = Capacitor(data[5])
        else:
            return None

        status = self.component_search(component)
        if not status:
            return None  
        else:
            return component

    def alternative_check(self, data):
        """ Checks each component in the given data with the suppplied alternative and checks if it
        is a valid alternative based on the component type. Displays to the console if a componenet
        is not an alternative part.

        Parameters:
            - Alternative componenet data as a 2D list of componenets
        """
        i = 0
        while i < len(data):
            original_component = self.data_to_component(data[i])
            data[i + 1][3] = data[i][3] 
            alternative_component = self.data_to_component(data[i + 1])

            if (original_component is None or alternative_component is None):
                i += 2
                continue

            if not original_component.is_alternative(alternative_component):
                self._print_queue.append("Component " + alternative_component._name +
                                        " is not an alternative for " +
                                        original_component._name + ".")
            i += 2

class CsvConverter():
    """ Utility class to convert CSV data to componeent objects
    
    Parameters:
        - file_name: The name of the CSV file to convert

    Attributes:
        - data: The data stored in the CSV file, stored as a 2D list
        - current_row: The index of the row currently being manipulated
    """
    def __init__(self, file_name):
        self._current_row = 0
        self._data = None
        self.read_file(file_name)

    def read_file(self, file_name):
        """ Reads the given file and stores the resulting data in a 2D list

        Parameters
          - file_name: The name of the CSV file to convert
        """

        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for i in range(2): next(reader)
            self._data = list(csv.reader(file))
            self._current_row = 0


def main():
    csvReader = CsvConverter("test.csv")
    partSearcher = PartSearcher()
    partSearcher.alternative_check(csvReader._data)
    for i in partSearcher._print_queue:
        print(i)

if __name__ == "__main__":
    main()