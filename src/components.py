"""
Module that contains all of the supported component models
"""

import abc

class Component(metaclass=abc.ABCMeta):
    # Search codes for shared componenet attributes
    TOLERANCE_SEARCH_CODE = 3
    PACKAGE_SEARCH_CODE = 16
    SIZE_SEARCH_CODE = 46
    TEMPERATURE_SEARCH_CODE = 252  
    HEIGHT_SEARCH_CODE = 1500
    STATUS_SEARCH_CODE = 1989
    
    """ Generic component model class
    
    Parameters:
        - part_name: The name of the component to be created

    Attributes:
        - name: The name of the component
        - parameters: The parameters describing the component in the format:
                      [Value, Package, Power, Tolerance, Size, Height, Temperature, Status]
    """
    def __init__(self, part_name):
        self._name = part_name
        # Dictionary to relate search codes to parameter values
        self._parameters = {self.TOLERANCE_SEARCH_CODE: None, self.PACKAGE_SEARCH_CODE: None,
                            self.SIZE_SEARCH_CODE: None, self.TEMPERATURE_SEARCH_CODE: None,
                            self.HEIGHT_SEARCH_CODE: None, self.STATUS_SEARCH_CODE: None}
        self._price = None

    def __eq__(self, component):
        """ Compares this component with the given component. Returns True if their parameters are
            the same, False otherwise.

            Paramterers:
                - component: The componenet to compare to the current component

            Returns: True if all parameters are equal, false otherwise
        """ 
        if len(self._parameters) != len(component._parameters):
            return False

        if self._name != component._name:
            return False 

        for key in self._parameters:
            if (self._parameters[key] != component._parameters[key]):
                return False
        return True

    def compare_functionality(self, component, parameters):
        """ Compares the functionality of this component and the given component. The functionality
        is determined by the parameters variable passed to the function.

        Parameters:
            - component: The component to compare to the current componenet
            - parameters: The list of parameter codes to be compared to determine functionality

        Returns: True if all functionality is equal, False otherwise
        """
        for parameter_code in parameters:
            if (self._parameters[parameter_code] != component._parameters[parameter_code]):
                print(self._name + " and " + component._name + ": Part specfications don't match.")
                return False
        return True

    def compare_temperature(self, component):
        """ Compares the temperature range of this component and the given component.
        
        Parameters:
            - component: The componenet to compare to the current component

        Returns: True if the temperature of the alternative fufills the original range, false otherwise
        """
        original_temperatures = []
        alternative_temperatures = []
        for word in self._parameters[self.TEMPERATURE_SEARCH_CODE].split():
            if word[-2:] == "°C":
                word = word[0:-2]

            if word.isdigit() or word[1:].isdigit():    
                original_temperatures.append(int(word))

        for word in component._parameters[self.TEMPERATURE_SEARCH_CODE].split():
            if word[-2:] == "°C":
                word = word[0:-2]

            if word.isdigit() or word[1:].isdigit():
                alternative_temperatures.append(int(word))

        if (alternative_temperatures[0] > original_temperatures[0] or
            alternative_temperatures[1] < original_temperatures[1]):
            print(self._name + " and " + component._name + ": Temperature specfications aren't sufficient.")
            return False
        return True

    @abc.abstractmethod
    def is_alternative(self, component):
        """ Determines if the given component can be substituted as an alternative
        for this component
        """
        

class Resistor(Component):
    # Search code for power and resistance values
    POWER_SEARCH_CODE = 2
    RESISTANCE_SEARCH_CODE = 2085
    
    """ Resistor model class, inherits from generic component class
    
    Parameters:
        - part_name: The name of the component to be created
    """
    def __init__(self, part_name):
        Component.__init__(self, part_name)
        self._parameters[self.POWER_SEARCH_CODE] = None
        self._parameters[self.RESISTANCE_SEARCH_CODE] = None

    def is_alternative(self, component):
        """ Determines if the given component can be used as an alternative for this resistor.
        It can be used as an alternative if all parameters are the same except the part name. 
        
        Parameters:
            - component: The component to check with this resistor

        Returns: True if it is a valid alternative, false otherwise
        """
        if len(self._parameters) != len(component._parameters):
            return False

        functionality_parameters = [self.RESISTANCE_SEARCH_CODE, self.PACKAGE_SEARCH_CODE]
        status = self.compare_functionality(component, functionality_parameters)
        if not status:
            return False

        status = self.compare_temperature(component)
        if not status:
            return False

        # Compares power rating
        if (float(component._parameters[self.POWER_SEARCH_CODE][0:5]) <
            float(self._parameters[self.POWER_SEARCH_CODE][0:5])):
                print(self._name + " and " + component._name + ": Power specfications aren't sufficient.")
                return False
        return True


class Capacitor(Component):
    # Indexes to access data fields within search results array
    VOLTAGE_SEARCH_CODE = 14
    CAPACITANCE_SEARCH_CODE = 2049
    
    """ Capacitor model class, inherits from generic component class
    
    Parameters:
        - part_name: The name of the component to be created
    """
    def __init__(self, part_name):
        Component.__init__(self, part_name)
        self._parameters[self.VOLTAGE_SEARCH_CODE] = None
        self._parameters[self.CAPACITANCE_SEARCH_CODE] = None

    def is_alternative(self, component):
        """ Determines if the given component can be used as an alternative for this capacitor.
        It can be used as a alternative if all parameters are the same except the part name. 
            
        Parameters:
            - component: The component to check with this capacitor

        Returns: True if it is a valid alternative, false otherwise
        """
        if len(self._parameters) != len(component._parameters):
            return False

        functionality_parameters = [self.CAPACITANCE_SEARCH_CODE, self.PACKAGE_SEARCH_CODE]
        status = self.compare_functionality(component, functionality_parameters)
        if not status:
            return False

        status = self.compare_temperature(component)
        if not status:
            return False

        # Compares voltage rating
        if (int(component._parameters[self.VOLTAGE_SEARCH_CODE][0:-1]) <
            int(self._parameters[self.VOLTAGE_SEARCH_CODE][0:-1])):
                print(self._name + " and " + component._name + ": Voltage specfications aren't sufficient.")
                return False
        return True
    