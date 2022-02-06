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
        pass

    def check_lead_time(self):
        pass

def main():
    digikey_logger = logging.getLogger('digikey')
    digikey_logger.setLevel(logging.NOTSET)

    manager = ComponentManager()
    manager.check_alternative()

if __name__ == "__main__":
    main()

