"""
Module containing all top level functionality for the component manager
"""
import logging

from components import *
from component_converter import *

class ComponentManager():
    """ Class that handles all top level functionality for the application
    
    Parameters:
        component_converter: The component_converter object responsible for handling all data passing
        component_list: The active list of components being managed by the component converter
    """

    def __init__(self):
        self._component_converter = ComponentConverter("components.csv")
        self._component_converter.create_component_list()
        self._components = self._component_converter._components
        
    def check_alternative(self):
        """ Checks the component list as a list of alternatives and determines if the components
        are valid alternatives
        """
        i = 0
        while i < len(self._components):
            original_component_valid = not isinstance(self._components[i], str)
            alternate_component_valid = not isinstance(self._components[i + 1], str)
            
            if (original_component_valid and not alternate_component_valid):
                print("Can't compare parts " + self._components[i]._name + " and " + self._components[i + 1] + ".")
            elif (not original_component_valid and alternate_component_valid):
                print("Can't compare parts " + self._components[i] + " and " + self._components[i + 1]._name + ".")
            elif (not original_component_valid and not alternate_component_valid):
                print("Can't compare parts " + self._components[i] + " and " + self._components[i + 1] + ".")
            else:
                self._components[i].is_alternative(self._components[i + 1])
            i += 2

    def check_bom_cost(self):
        """ Checks the price of components in the component list for 1 of and 100 of
        the BoM products.
        """
        one_of_cost = 0
        hundred_of_cost = 0

        for component in self._components:
            one_of_cost += component._price[0]
            hundred_of_cost += component._price[1]

        print("Price of 1 BoM: " + str(round(one_of_cost, 2)) + " $AUD per BoM.")
        print("Price of 100 BoMs: " + str(round(hundred_of_cost / 100, 2)) + " $AUD per BoM.")

    def check_lead_time(self):
        """ Checks the list of components list for a estimated lead time on each product.
        """
        for component in self._components:
            if component._lead_time != 0:
                print("Leads time of " + component._name + " is " + component._lead_time + ".")

def main():
    digikey_logger = logging.getLogger('digikey')
    digikey_logger.setLevel(logging.NOTSET)

    manager = ComponentManager()
    manager._component_converter.save_component_list("Test")
    #manager.check_bom_cost()

if __name__ == "__main__":
    main()

