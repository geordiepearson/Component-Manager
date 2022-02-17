"""
Module containing all top level functionality for the component manager
"""
import logging
import argparse
import os
import sys

from component_manager.src import *

class ComponentManager():
    """ Class that handles all top level functionality for the application
    
    Parameters:
        component_converter: The component_converter object responsible for handling all
                             data passing
    """
    def __init__(self, filename):
        self._component_converter = ComponentConverter()

        if filename[-3:] == "csv":
            self._component_converter.read_csv_file(filename)
            self._component_converter.create_component_list()
            self._component_converter.save_component_list(filename[:-4])
        else:
            self._component_converter = self._component_converter.read_component_list(filename)
        
    def check_alternative(self):
        """ Checks the component list as a list of alternatives and determines if the components
        are valid alternatives.
        """
        i = 0
        while i < len(self._component_converter._components):
            original_component_valid = not isinstance(self._component_converter._components[i], str)
            alternate_component_valid = not isinstance(self._component_converter._components[i + 1], str)
            
            if (original_component_valid and not alternate_component_valid):
                print("Can't compare parts " + self._component_converter._components[i]._name +
                      " and " + self._component_converter._components[i + 1] + ".")
            elif (not original_component_valid and alternate_component_valid):
                print("Can't compare parts " + self._component_converter._components[i] +
                      " and " + self._component_converter._components[i + 1]._name + ".")
            elif (not original_component_valid and not alternate_component_valid):
                print("Can't compare parts " + self._component_converter._components[i] +
                      " and " + self._component_converter._components[i + 1] + ".")
            else:
                self._component_converter._components[i].is_alternative(
                    self._component_converter._components[i + 1])
            i += 2

    def check_bom_cost(self):
        """ Checks the price of components in the component list for 1 of and 100 of
        the BoM products.
        """
        one_of_cost = 0
        hundred_of_cost = 0

        for component in self._component_converter._components:
            if not isinstance(component, str):
                one_of_cost += component._price[0]
                hundred_of_cost += component._price[1]

        print("Price of 1 BoM: " + str(round(one_of_cost, 2)) + " $AUD per BoM.")
        print("Price of 100 BoMs: " + str(round(hundred_of_cost / 100, 2)) + " $AUD per BoM.")

    def check_lead_time(self):
        """ Checks the list of components list for a estimated lead time on each product.
        """
        for component in self._component_converter._components:
            if not isinstance(component, str) and component._lead_time != 0:
                if component._lead_time == "No lead time information available":
                    print(component._name + " is not available.")
                else:
                    print("Leads time of " + component._name + " is " + component._lead_time + ".")

def main():
    digikey_logger = logging.getLogger('digikey')
    digikey_logger.setLevel(logging.NOTSET)
    parser = argparse.ArgumentParser(description=("An application to manage and handle various "
                                                   "electronic component related tasks."))
    parser.add_argument('filename', help="The name of the file storing component data")
    parser.add_argument('-a', action='store_true', help="Check if given components are valid alternatives")
    parser.add_argument('-l', action='store_true', help="Check lead times of given components")
    parser.add_argument('-p', action='store_true', help="Calculate price of given components")
    args = parser.parse_args()

    manager = ComponentManager(args.filename)
    if args.a:
        manager.check_alternative()
    if args.l:
        manager.check_lead_time()
    if args.p:
        manager.check_bom_cost()
    
if __name__ == "__main__":
    main()

