#-*- coding: utf-8 -*-

import unittest
from unittest.mock import patch
import logging
import os
from io import StringIO
from component_manager.src import *

class ConverterTesting(unittest.TestCase):
    PATH_TO_TESTS = os.getcwd()
    def test_read_csv_file(self):
        """ Tests reading of CSV files.
        """
        test_converter = ComponentConverter()
        test_converter.read_csv_file(self.PATH_TO_TESTS + "/test.csv")
        expected_value = [["Resistor", "CRCW080510K0FKEA"], ["Resistor", "CRCW080510K0FKEA"],
                          ["Capacitor", "CL05A104KA5NNNC"]]
        self.assertTrue(test_converter._data, expected_value)

    def test_data_to_component(self):
        """ Tests of conversion between CSV to component model.
        """
        test_converter = ComponentConverter()
        test_converter.read_csv_file(self.PATH_TO_TESTS + "/test.csv")
        test_component = test_converter.data_to_component(test_converter._data[0])

        self.assertEqual(test_component._parameters[test_component.RESISTANCE_SEARCH_CODE], "10 kOhms")
        self.assertEqual(test_component._parameters[test_component.POWER_SEARCH_CODE], "0.125W, 1/8W")
        self.assertEqual(test_component._parameters[test_component.TOLERANCE_SEARCH_CODE], "±1%")
        self.assertEqual(test_component._parameters[test_component.PACKAGE_SEARCH_CODE],
                         "0805 (2012 Metric)")
        self.assertEqual(test_component._parameters[test_component.SIZE_SEARCH_CODE],
                         "0.079\" L x 0.049\" W (2.00mm x 1.25mm)")
        self.assertEqual(test_component._parameters[test_component.TEMPERATURE_SEARCH_CODE], 
                         "-55°C ~ 155°C")
        self.assertEqual(test_component._parameters[test_component.HEIGHT_SEARCH_CODE],
                         "0.024\" (0.60mm)")
        self.assertEqual(test_component._parameters[test_component.STATUS_SEARCH_CODE], "Active")

    def test_component_list(self):
        """ Tests the creation of a component list from a CSV file.
        """
        test_converter = ComponentConverter()
        test_converter.read_csv_file(self.PATH_TO_TESTS + "/test.csv")
        test_converter.create_component_list()

        self.assertEqual(test_converter._components[0]._parameters[test_converter._components[1].
                         RESISTANCE_SEARCH_CODE], "10 kOhms")
        self.assertEqual(test_converter._components[0]._parameters[test_converter._components[0].
                         POWER_SEARCH_CODE], "0.125W, 1/8W")
        self.assertEqual(test_converter._components[0]._parameters[test_converter._components[0].
                         TOLERANCE_SEARCH_CODE], "±1%")
        self.assertEqual(test_converter._components[0]._parameters[test_converter._components[0].
                         PACKAGE_SEARCH_CODE], "0805 (2012 Metric)")
        self.assertEqual(test_converter._components[0]._parameters[test_converter._components[0].
                         SIZE_SEARCH_CODE], "0.079\" L x 0.049\" W (2.00mm x 1.25mm)")
        self.assertEqual(test_converter._components[0]._parameters[test_converter._components[0].
                         TEMPERATURE_SEARCH_CODE], "-55°C ~ 155°C")
        self.assertEqual(test_converter._components[0]._parameters[test_converter._components[0].
                         HEIGHT_SEARCH_CODE], "0.024\" (0.60mm)")
        self.assertEqual(test_converter._components[0]._parameters[test_converter._components[0].
                         STATUS_SEARCH_CODE], "Active")

        self.assertEqual(test_converter._components[1]._parameters[test_converter._components[1].
                         RESISTANCE_SEARCH_CODE], "10 kOhms")
        self.assertEqual(test_converter._components[1]._parameters[test_converter._components[1].
                         POWER_SEARCH_CODE], "0.125W, 1/8W")
        self.assertEqual(test_converter._components[1]._parameters[test_converter._components[1].
                         TOLERANCE_SEARCH_CODE], "±1%")
        self.assertEqual(test_converter._components[1]._parameters[test_converter._components[1].
                         PACKAGE_SEARCH_CODE],
                         "0805 (2012 Metric)")
        self.assertEqual(test_converter._components[1]._parameters[test_converter._components[1].
                         SIZE_SEARCH_CODE], "0.079\" L x 0.049\" W (2.00mm x 1.25mm)")
        self.assertEqual(test_converter._components[1]._parameters[test_converter._components[1].
                         TEMPERATURE_SEARCH_CODE], "-55°C ~ 155°C")
        self.assertEqual(test_converter._components[1]._parameters[test_converter._components[1].
                         HEIGHT_SEARCH_CODE], "0.024\" (0.60mm)")
        self.assertEqual(test_converter._components[1]._parameters[test_converter._components[1].
                         STATUS_SEARCH_CODE], "Active")

        self.assertEqual(test_converter._components[2]._parameters[test_converter._components[2].
                         CAPACITANCE_SEARCH_CODE], "0.1 µF")
        self.assertEqual(test_converter._components[2]._parameters[test_converter._components[2].
                         VOLTAGE_SEARCH_CODE], "25V")
        self.assertEqual(test_converter._components[2]._parameters[test_converter._components[2].
                         TOLERANCE_SEARCH_CODE], "±10%")
        self.assertEqual(test_converter._components[2]._parameters[test_converter._components[2].
                         PACKAGE_SEARCH_CODE], "0402 (1005 Metric)")
        self.assertEqual(test_converter._components[2]._parameters[test_converter._components[2].
                         SIZE_SEARCH_CODE], "0.039\" L x 0.020\" W (1.00mm x 0.50mm)")
        self.assertEqual(test_converter._components[2]._parameters[test_converter._components[2].
                         TEMPERATURE_SEARCH_CODE], "-55°C ~ 85°C")
        self.assertEqual(test_converter._components[2]._parameters[test_converter._components[2].
                         HEIGHT_SEARCH_CODE], "-")
        self.assertEqual(test_converter._components[2]._parameters[test_converter._components[2].
                         STATUS_SEARCH_CODE], "Active")

    def test_read_write_list(self):
        """ Tests read and write functionality of component list to file.
        """
        test_converter = ComponentConverter()
        test_converter.read_csv_file(self.PATH_TO_TESTS + "/test.csv")
        test_converter.create_component_list()
        test_converter.save_component_list(self.PATH_TO_TESTS + "/test")

        read_converter = test_converter.read_component_list(self.PATH_TO_TESTS + "/test")
        self.assertEqual(test_converter._components, read_converter._components)

    @patch('sys.stdout', new_callable = StringIO)
    def test_check_alternative(self, stdout):
        """ Tests alternative checking for a given component list.
        """
        test_manager = ComponentManager(self.PATH_TO_TESTS + "/toplevel_test")
        test_manager.check_alternative()
        expected_output = ("Can't compare parts PRL1632-R016-F-T1 and STE1206M1W0R016F.\n"
                           "Can't compare parts PRL1632-R006-F-T1 and STE1206M1W0R006FS.\n"
                           "RC0402FR-07715KL and WR04X7152FTL: Part specfications don't match.\n"
                           "Can't compare parts ERT-J1VS104HA and EWTF03-104G4H-N.\n"
                           "Can't compare parts ERJ-1TYJ2R7U and WR25X2R7 JTL.\n"
                           "Can't compare parts RC0402JR-0739KL and WR04X3902FTL.\n"
                           "Can't compare parts ERPI0412E-2R2M and IHLP1616ABER2R2M11.\n"
                           "Can't compare parts DLP11TB800UL2L and DLM0NSN500HY2.\n"
                           "Can't compare parts APT1608CGCK and KP1608CGCK.\n")
        self.assertEqual(stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable = StringIO)
    def test_check_bom_cost(self, stdout):
        """ Tests bom cost checking for a given component list.
        """
        test_manager = ComponentManager(self.PATH_TO_TESTS + "/toplevel_test")
        test_manager.check_bom_cost()
        expected_output = ("Price of 1 BoM: 9.36 $AUD per BoM.\n"
                           "Price of 100 BoMs: 3.81 $AUD per BoM.\n")
        self.assertEqual(stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable = StringIO)
    def test_check_lead_time(self, stdout):
        """ Tests lead time checking for a given component list.
        """
        test_manager = ComponentManager(self.PATH_TO_TESTS + "/toplevel_test")
        test_manager.check_lead_time()
        expected_output = ("Leads time of C2012X5R1C226K125AC is 28 week(s).\n"
                           "Leads time of 0805X225K250CT is 33 week(s).\n"
                           "Leads time of C1608X5R1C475K080AC is 20 week(s).\n"
                           "Leads time of CL31A476MPHNNNE is 28 week(s).\n"
                           "Leads time of WR04X4702FTL is 29 week(s).\n"
                           "Leads time of RC0402FR-07715KL is 20 week(s).\n")
        self.assertEqual(stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()