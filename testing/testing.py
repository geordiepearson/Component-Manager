import unittest

from components import *
from partsorter import *

class TestSearchMethods(unittest.TestCase):
    
    def test_equality(self):
        test_searcher = PartSearcher()
        test_resistor_one = Resistor('CRCW080510K0FKEA')
        test_searcher.component_search(test_resistor_one)

        test_resistor_two = Resistor('CRCW080510K0FKEA')
        test_searcher.component_search(test_resistor_two)

        test_capacitor = Capacitor('CL05A104KA5NNNC')
        test_searcher.component_search(test_capacitor)
        
        self.assertTrue(test_resistor_one.__eq__(test_resistor_two))
        self.assertFalse(test_resistor_one.__eq__(test_capacitor))
    
    def test_resistor_search(self):
        test_searcher = PartSearcher()
        test_resistor = Resistor('CRCW080510K0FKEA')
        test_searcher.component_search(test_resistor)
        
        self.assertEqual(test_resistor._parameters[test_resistor.RESISTANCE_SEARCH_CODE], "10 kOhms")
        self.assertEqual(test_resistor._parameters[test_resistor.PACKAGE_SEARCH_CODE], "0805 (2012 Metric)")
        self.assertEqual(test_resistor._parameters[test_resistor.POWER_SEARCH_CODE], "0.125W, 1/8W")
        self.assertEqual(test_resistor._parameters[test_resistor.TOLERANCE_SEARCH_CODE], "±1%")
        self.assertEqual(test_resistor._parameters[test_resistor.SIZE_SEARCH_CODE], "0.079\" L x 0.049\" W (2.00mm x 1.25mm)")
        self.assertEqual(test_resistor._parameters[test_resistor.HEIGHT_SEARCH_CODE], "0.020\" (0.50mm)")
        self.assertEqual(test_resistor._parameters[test_resistor.TEMPERATURE_SEARCH_CODE], "-55°C ~ 155°C")
        self.assertEqual(test_resistor._parameters[test_resistor.STATUS_SEARCH_CODE], "Active")

    def test_resistor_alternative(self):
        test_searcher = PartSearcher()
        test_resistor_original = Resistor('RC0402FR-0747KL')
        test_searcher.component_search(test_resistor_original)
        test_resistor_alternate = Resistor('WR04X4702FTL')
        test_searcher.component_search(test_resistor_alternate)        

        self.assertTrue(test_resistor_original.is_alternative(test_resistor_alternate))

    def test_capacitor_search(self):
        test_searcher = PartSearcher()
        test_capacitor = Capacitor('CL05A104KA5NNNC')
        test_searcher.component_search(test_capacitor)
        
        self.assertEqual(test_capacitor._parameters[test_capacitor.CAPACITANCE_SEARCH_CODE], "0.1 µF")
        self.assertEqual(test_capacitor._parameters[test_capacitor.PACKAGE_SEARCH_CODE], "0402 (1005 Metric)")
        self.assertEqual(test_capacitor._parameters[test_capacitor.VOLTAGE_SEARCH_CODE], "25V")
        self.assertEqual(test_capacitor._parameters[test_capacitor.TOLERANCE_SEARCH_CODE], "±10%")
        self.assertEqual(test_capacitor._parameters[test_capacitor.SIZE_SEARCH_CODE], "0.039\" L x 0.020\" W (1.00mm x 0.50mm)")
        self.assertEqual(test_capacitor._parameters[test_capacitor.HEIGHT_SEARCH_CODE], "-")
        self.assertEqual(test_capacitor._parameters[test_capacitor.TEMPERATURE_SEARCH_CODE], "-55°C ~ 85°C")
        self.assertEqual(test_capacitor._parameters[test_capacitor.STATUS_SEARCH_CODE], "Active")
    
    def test_capacitor_alternative(self):
        test_searcher = PartSearcher()
        test_capacitor_original = Capacitor('C3225X5R1C226M250AA')
        test_searcher.component_search(test_capacitor_original)
        test_capacitor_alternate = Capacitor('GRM32ER61C226KE20L')
        test_searcher.component_search(test_capacitor_alternate)

        self.assertTrue(test_capacitor_original.is_alternative(test_capacitor_alternate))

if __name__ == '__main__':
    unittest.main()