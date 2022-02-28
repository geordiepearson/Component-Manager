#-*- coding: utf-8 -*-

import unittest

from component_manager.src import *

class ComponentTesting(unittest.TestCase):
    def test_resistor_equality(self):
        """ Tests the resistor equality functionality.
        """
        resistor_one = Resistor("RC0402FR-0747KL")
        resistor_two = Resistor("CRCW040256K2FKED")
        resistor_three = Resistor("RC0402FR-0747KL")
        test_converter = ComponentConverter()

        test_converter.component_search(resistor_one)
        test_converter.component_search(resistor_two)
        test_converter.component_search(resistor_three)

        self.assertFalse(resistor_one.__eq__(resistor_two))
        self.assertTrue(resistor_one.__eq__(resistor_three))

    def test_resistor_search(self):
        """ Tests resistor search functionality.
        """
        test_converter = ComponentConverter()
        test_resistor = Resistor('CRCW080510K0FKEA')
        test_converter.component_search(test_resistor)
        
        self.assertEqual(test_resistor._parameters[test_resistor.RESISTANCE_SEARCH_CODE], "10 kOhms")
        self.assertEqual(test_resistor._parameters[test_resistor.PACKAGE_SEARCH_CODE], "0805 (2012 Metric)")
        self.assertEqual(test_resistor._parameters[test_resistor.POWER_SEARCH_CODE], "0.125W, 1/8W")
        self.assertEqual(test_resistor._parameters[test_resistor.TOLERANCE_SEARCH_CODE], "±1%")
        self.assertEqual(test_resistor._parameters[test_resistor.SIZE_SEARCH_CODE], "0.079\" L x 0.049\" W (2.00mm x 1.25mm)")
        self.assertEqual(test_resistor._parameters[test_resistor.HEIGHT_SEARCH_CODE], "0.024\" (0.60mm)")
        self.assertEqual(test_resistor._parameters[test_resistor.TEMPERATURE_SEARCH_CODE], "-55°C ~ 155°C")
        self.assertEqual(test_resistor._parameters[test_resistor.STATUS_SEARCH_CODE], "Active")

    def test_resistor_alternative(self):
        """ Tests resistor alternative functionality.
        """
        resistor_one = Resistor("CRCW040256K2FKED")
        resistor_two = Resistor("WR04X5622FTL")
        resistor_three = Resistor("RC0402JR-0739KL")
        test_converter = ComponentConverter()

        test_converter.component_search(resistor_one)
        test_converter.component_search(resistor_two)
        test_converter.component_search(resistor_three)

        self.assertTrue(resistor_one.is_alternative(resistor_two))
        self.assertFalse(resistor_one.is_alternative(resistor_three))

    def test_capacitor_equality(self):
        """ Tests capacitor equality functionality.
        """
        capacitor_one = Capacitor("C1608X5R1H105K080AB")
        capacitor_two = Capacitor("CL31A476MPHNNNE")
        capacitor_three = Capacitor("C1608X5R1H105K080AB")
        test_converter = ComponentConverter()

        test_converter.component_search(capacitor_one)
        test_converter.component_search(capacitor_two)
        test_converter.component_search(capacitor_three)

        self.assertFalse(capacitor_one.__eq__(capacitor_two))
        self.assertTrue(capacitor_one.__eq__(capacitor_three))
    
    def test_capacitor_search(self):
        """ Tests capacitor search functionality.
        """
        test_converter = ComponentConverter()
        test_capacitor = Capacitor('CL05A104KA5NNNC')
        test_converter.component_search(test_capacitor)
        
        self.assertEqual(test_capacitor._parameters[test_capacitor.CAPACITANCE_SEARCH_CODE], "0.1 µF")
        self.assertEqual(test_capacitor._parameters[test_capacitor.PACKAGE_SEARCH_CODE], "0402 (1005 Metric)")
        self.assertEqual(test_capacitor._parameters[test_capacitor.VOLTAGE_SEARCH_CODE], "25V")
        self.assertEqual(test_capacitor._parameters[test_capacitor.TOLERANCE_SEARCH_CODE], "±10%")
        self.assertEqual(test_capacitor._parameters[test_capacitor.SIZE_SEARCH_CODE], "0.039\" L x 0.020\" W (1.00mm x 0.50mm)")
        self.assertEqual(test_capacitor._parameters[test_capacitor.HEIGHT_SEARCH_CODE], "-")
        self.assertEqual(test_capacitor._parameters[test_capacitor.TEMPERATURE_SEARCH_CODE], "-55°C ~ 85°C")
        self.assertEqual(test_capacitor._parameters[test_capacitor.STATUS_SEARCH_CODE], "Active")
    
    def test_capacitor_alternative(self):
        """ Tests capacitor alternative functionality
        """
        capacitor_one = Capacitor('C3225X5R1C226M250AA')
        capacitor_two = Capacitor('GRM32ER61C226KE20L')
        capacitor_three = Capacitor('UMK325B7475KMHP')
        test_converter = ComponentConverter()

        test_converter.component_search(capacitor_one)
        test_converter.component_search(capacitor_two)
        test_converter.component_search(capacitor_three)

        self.assertTrue(capacitor_one.is_alternative(capacitor_two))
        self.assertFalse(capacitor_one.is_alternative(capacitor_three))
    
    def test_inductor_equality(self):
        """ Tests inductor equality functionality.
        """
        inductor_one = Inductor("B82464G4682M00")
        inductor_two = Inductor("VLC5045T-100M")
        inductor_three = Inductor("B82464G4682M00")
        test_converter = ComponentConverter()

        test_converter.component_search(inductor_one)
        test_converter.component_search(inductor_two)
        test_converter.component_search(inductor_three)

        self.assertFalse(inductor_one.__eq__(inductor_two))
        self.assertTrue(inductor_one.__eq__(inductor_three))

    def test_inductor_search(self):
        """ Tests inductor search functionality.
        """
        test_converter = ComponentConverter()
        test_inductor = Inductor('74437368047')
        test_converter.component_search(test_inductor)

        self.assertEqual(test_inductor._parameters[test_inductor.INDUCTANCE_SEARCH_CODE], "4.7 µH")
        self.assertEqual(test_inductor._parameters[test_inductor.SATURATION_SEARCH_CODE], "19A")
        self.assertEqual(test_inductor._parameters[test_inductor.CURRENT_SEARCH_CODE], "7 A")
        self.assertEqual(test_inductor._parameters[test_inductor.PACKAGE_SEARCH_CODE], "Nonstandard")
        self.assertEqual(test_inductor._parameters[test_inductor.TOLERANCE_SEARCH_CODE], "±20%")
        self.assertEqual(test_inductor._parameters[test_inductor.SIZE_SEARCH_CODE], "0.433\" L x 0.394\" W (11.00mm x 10.00mm)")
        self.assertEqual(test_inductor._parameters[test_inductor.HEIGHT_SEARCH_CODE], "0.157\" (4.00mm)")
        self.assertEqual(test_inductor._parameters[test_inductor.TEMPERATURE_SEARCH_CODE], "-40°C ~ 125°C")
        self.assertEqual(test_inductor._parameters[test_inductor.STATUS_SEARCH_CODE], "Active")

    def test_inductor_alternative(self):
        """ Tests inductor alternative functionality
        """
        inductor_one = Inductor('74476410')
        inductor_two = Inductor('NLV32T-100J-PF')
        inductor_three = Inductor('LQM2HPN2R2MG0L')
        test_converter = ComponentConverter()

        test_converter.component_search(inductor_one)
        test_converter.component_search(inductor_two)
        test_converter.component_search(inductor_three)

        self.assertTrue(inductor_one.is_alternative(inductor_two))
        self.assertFalse(inductor_one.is_alternative(inductor_three))
    
    def test_ferrite_equality(self):
        """ Tests ferrite equality functionality
        """
        ferrite_one = Ferrite("QT1608RL120HC-2A")
        ferrite_two = Ferrite("BLM15AX601SN1D")
        ferrite_three = Ferrite("QT1608RL120HC-2A")
        test_converter = ComponentConverter()

        test_converter.component_search(ferrite_one)
        test_converter.component_search(ferrite_two)
        test_converter.component_search(ferrite_three)

        self.assertFalse(ferrite_one.__eq__(ferrite_two))
        self.assertTrue(ferrite_one.__eq__(ferrite_three))

    def test_ferrite_search(self):
        """ Tests ferrite search functionality
        """
        test_converter = ComponentConverter()
        test_ferrite = Ferrite('BLM15AX601SN1D')
        test_converter.component_search(test_ferrite)

        self.assertEqual(test_ferrite._parameters[test_ferrite.RATING_SEARCH_CODE], "500mA")
        self.assertEqual(test_ferrite._parameters[test_ferrite.FILTER_SEARCH_CODE], "-")
        self.assertEqual(test_ferrite._parameters[test_ferrite.PACKAGE_SEARCH_CODE], "0402 (1005 Metric)")
        self.assertEqual(test_ferrite._parameters[test_ferrite.SIZE_SEARCH_CODE], "0.039\" L x 0.022\" W (1.00mm x 0.55mm)")
        self.assertEqual(test_ferrite._parameters[test_ferrite.TEMPERATURE_SEARCH_CODE], "-55°C ~ 125°C")
        self.assertEqual(test_ferrite._parameters[test_ferrite.STATUS_SEARCH_CODE], "Active")

    def test_ferrite_alternative(self):
        """ Tests ferrite alternative functionality
        """
        ferrite_one = Ferrite("BLM15AX601SN1D")
        ferrite_two = Ferrite("BLM18PG121SN1")
        ferrite_three = Ferrite('BLM15AX601SN1D')
        test_converter = ComponentConverter()

        test_converter.component_search(ferrite_one)
        test_converter.component_search(ferrite_two)
        test_converter.component_search(ferrite_three)

        self.assertFalse(ferrite_one.is_alternative(ferrite_two))
        self.assertTrue(ferrite_one.is_alternative(ferrite_three))
    
    def test_choke_equality(self):
        """ Tests choke equality functionality.
        """
        choke_one = Choke("DLP11TB800UL2L")
        choke_two = Choke("DLW21HN900SQ2L")
        choke_three = Choke("DLP11TB800UL2L")
        test_converter = ComponentConverter()

        test_converter.component_search(choke_one)
        test_converter.component_search(choke_two)
        test_converter.component_search(choke_three)

        self.assertFalse(choke_one.__eq__(choke_two))
        self.assertTrue(choke_one.__eq__(choke_three))
    
    def test_choke_search(self):
        """ Tests choke search functionality.
        """
        test_converter = ComponentConverter()
        test_choke = Choke("DLP11TB800UL2L")
        test_converter.component_search(test_choke)

        self.assertEqual(test_choke._parameters[test_choke.RATING_SEARCH_CODE], "100mA")
        self.assertEqual(test_choke._parameters[test_choke.PACKAGE_SEARCH_CODE], "0504 (1210 Metric), 4 Lead")
        self.assertEqual(test_choke._parameters[test_choke.SIZE_SEARCH_CODE], "0.049\" L x 0.039\" W (1.25mm x 1.00mm)")
        self.assertEqual(test_choke._parameters[test_choke.TEMPERATURE_SEARCH_CODE], "-40°C ~ 85°C")
        self.assertEqual(test_choke._parameters[test_choke.STATUS_SEARCH_CODE], "Not For New Designs")
    
    def test_choke_alternative(self):
        """ Tests chokes alternative functionality.
        """
        choke_one = Choke("DLW21HN900SQ2L")
        choke_two = Choke("ACM2012-900-2P-T002")
        choke_three = Choke('DLP11TB800UL2L')
        test_converter = ComponentConverter()

        test_converter.component_search(choke_one)
        test_converter.component_search(choke_two)
        test_converter.component_search(choke_three)

        self.assertFalse(choke_one.is_alternative(choke_two))
        self.assertFalse(choke_one.is_alternative(choke_three))


if __name__ == '__main__':
    digikey_logger = logging.getLogger('digikey')
    digikey_logger.setLevel(logging.INFO)
    unittest.main()