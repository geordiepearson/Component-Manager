"""
Module containing all functionality to convert data into component models
"""
import os
import csv
import pickle
import digikey
from digikey.v3.productinformation import KeywordSearchRequest

from component_manager.src.components import *

# Indexes for CSV data in list format
CSV_DESCRIPTION_INDEX = 0
CSV_PART_NUMBER_INDEX = 1

# Indexes for description data access
DESCRIPTION_TYPE_INDEX = 0
DESCRIPTION_VALUE_INDEX = 1

class ComponentConverter():
    """ Utility class to handle all creation of component models from CSV data

    Attributes:
        - components: The list of components converted from the given CSV data
        - data: The data stored in the CSV file, stored as a 2D list
        - current_row: The index of the row currently being manipulated
    """
    def __init__(self):
        self._current_row = 0
        self._data = None
        self._components = []

    def read_csv_file(self, filename):
        """ Reads the given file and stores the resulting data in a 2D list

        Parameters
          - file_name: The name of the CSV file to convert
        """
        with open(filename, "r") as file:
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

        # Handles all component parameters
        search_request = KeywordSearchRequest(keywords=component._name, record_count=1)
        result = digikey.keyword_search(body=search_request) 
        if result.products == []:
            return False
        else:
            for parameter in result.products[0]._parameters:
                if parameter.parameter_id in component._parameters:
                    component._parameters[parameter.parameter_id] = parameter.value
        
            # Handles pricing breakpoints
            for product in result.products:
                for price in product.standard_pricing:
                    if price.break_quantity == 1:
                        if component._price[0] == 0 or price.total_price < component._price[0]:
                            component._price[0] = price.total_price 
                    
                        # Handles lead time
                        if product.quantity_available == 0:
                            component._lead_time = result.products[0].manufacturer_lead_weeks
                    
                    if price.break_quantity == 100:
                        if component._price[1] == 0 or price.total_price < component._price[1]:
                            component._price[1] = price.total_price 
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
        elif component_data[CSV_DESCRIPTION_INDEX].split(", ")[DESCRIPTION_TYPE_INDEX] == "Inductor":
            component = Inductor(component_data[CSV_PART_NUMBER_INDEX])
        elif component_data[CSV_DESCRIPTION_INDEX].split(", ")[DESCRIPTION_TYPE_INDEX] == "Ferrite Bead":
            component = Ferrite(component_data[CSV_PART_NUMBER_INDEX])
        elif component_data[CSV_DESCRIPTION_INDEX].split(", ")[DESCRIPTION_TYPE_INDEX] == "Choke":
            component = Choke(component_data[CSV_PART_NUMBER_INDEX])
        elif component_data[CSV_DESCRIPTION_INDEX].split(", ")[DESCRIPTION_TYPE_INDEX] == "Diode":
            component = Diode(component_data[CSV_PART_NUMBER_INDEX])
        else: 
            component = IC(component_data[CSV_PART_NUMBER_INDEX])

        status = self.component_search(component)
        if not status:
            return component._name
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

    def save_component_list(self, filename):
        """ Saves the current component converter using the pickel serialization module. """
        with open(filename, 'wb') as component_file:
            pickle.dump(self, component_file)

    def read_component_list(self, filename):
        """ Reads the component converter information using the pickel serialization module from the
            given file. 

            Returns: The component converter information stored in the given file
        """
        with open(filename, 'rb') as component_file:
            return pickle.load(component_file)
