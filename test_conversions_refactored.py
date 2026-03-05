import conversions_refactored
import unittest

class Test_Refactored_Conversions(unittest.TestCase):
    def test_distance_conversions(self):
        print("Test: 1 Mile should equal 1760 Yards")
        self.assertAlmostEqual(conversions_refactored.convert("Miles", "Yards", 1), 1760, places=2)
        print("passed: 1 Mile correctly converted to 1760 Yards")

        print("Test: 1760 Yards should equal 1 Mile")
        self.assertAlmostEqual(conversions_refactored.convert("Yards", "Miles", 1760), 1, places=2)
        print("passed: 1760 Yards correctly converted to 1 Mile")

        print("Test: 1 Mile should equal 1609.34 Meters")
        self.assertAlmostEqual(conversions_refactored.convert("Miles", "Meters", 1), 1609.34, places=2)
        print("passed: 1 Mile correctly converted to 1609.34 Meters")

        print("Test: 1 Meter should equal 1.09361 Yards")
        self.assertAlmostEqual(conversions_refactored.convert("Meters", "Yards", 1), 1.09361, places=2)
        print("passed: 1 Meter correctly converted to 1.09361 Yards")

        print("Test: 1 Yard should equal 0.9144 Meters")
        self.assertAlmostEqual(conversions_refactored.convert("Yards", "Meters", 1), 0.9144, places=2)
        print("passed: 1 Yard correctly converted to 0.9144 Meters")

        print("Test: 1609.34 Meters should equal 1 Mile")
        self.assertAlmostEqual(conversions_refactored.convert("Meters", "Miles", 1609.34), 1, places=2)
        print("passed: 1609.34 Meters correctly converted to 1 Mile")
    
    def test_temperature_conversions(self):
        print("Test: 0 Celsius should equal 273.15 Kelvin")
        self.assertAlmostEqual(conversions_refactored.convert("Celsius", "Kelvin", 0), 273.15, places=2)
        print("passed: 0 Celsius correctly converted to 273.15 Kelvin")

        print("Test: 100 Celsius should equal 212.0 Fahrenheit")
        self.assertAlmostEqual(conversions_refactored.convert("Celsius", "Fahrenheit", 100), 212.0, places=2)
        print("passed: 100 Celsius correctly converted to 212.0 Fahrenheit")

        print("Test: 32 Fahrenheit should equal 0 Celsius")
        self.assertAlmostEqual(conversions_refactored.convert("Fahrenheit", "Celsius", 32), 0, places=2)
        print("passed: 32 Fahrenheit correctly converted to 0 Celsius")

        print("Test: 32 Fahrenheit should equal 273.15 Kelvin")
        self.assertAlmostEqual(conversions_refactored.convert("Fahrenheit", "Kelvin", 32), 273.15, places=2)
        print("passed: 32 Fahrenheit correctly converted to 273.15 Kelvin")

        print("Test: 273.15 Kelvin should equal 0 Celsius")
        self.assertAlmostEqual(conversions_refactored.convert("Kelvin", "Celsius", 273.15), 0, places=2)
        print("passed: 273.15 Kelvin correctly converted to 0 Celsius")

        print("Test: 273.15 Kelvin should equal 32 Fahrenheit")
        self.assertAlmostEqual(conversions_refactored.convert("Kelvin", "Fahrenheit", 273.15), 32, places=2)
        print("passed: 273.15 Kelvin correctly converted to 32 Fahrenheit")

    def test_same_unit(self):
        print("Test: Celsius to Celsius should return same value")
        self.assertEqual(conversions_refactored.convert("Celsius", "Celsius", 100), 100)
        print("passed: Celsius to Celsius returned 100")

        print("Test: Fahrenheit to Fahrenheit should return same value")
        self.assertEqual(conversions_refactored.convert("Fahrenheit", "Fahrenheit", 100), 100)
        print("passed: Fahrenheit to Fahrenheit returned 100")

        print("Test: Kelvin to Kelvin should return same value")
        self.assertEqual(conversions_refactored.convert("Kelvin", "Kelvin", 100), 100)
        print("passed: Kelvin to Kelvin returned 100")

        print("Test: Miles to Miles should return same value")
        self.assertEqual(conversions_refactored.convert("Miles", "Miles", 100), 100)
        print("passed: Miles to Miles returned 100")

        print("Test: Yards to Yards should return same value")
        self.assertEqual(conversions_refactored.convert("Yards", "Yards", 100), 100)
        print("passed: Yards to Yards returned 100")

        print("Test: Meters to Meters should return same value")
        self.assertEqual(conversions_refactored.convert("Meters", "Meters", 100), 100)
        print("passed: Meters to Meters returned 100")

    def test_incompatible_units(self):
        print("Test: Celsius to Miles should raise ConversionNotPossible")
        self.assertRaises(conversions_refactored.ConversionNotPossible,conversions_refactored.convert,"Celsius", "Miles", 100)
        print("passed: Celsius to Miles correctly raised ConversionNotPossible")

        print("Test: Kelvin to Yards should raise ConversionNotPossible")
        self.assertRaises(conversions_refactored.ConversionNotPossible,conversions_refactored.convert,"Kelvin", "Yards", 100)
        print("passed: Kelvin to Yards correctly raised ConversionNotPossible")

        print("Test: Meters to Fahrenheit should raise ConversionNotPossible")
        self.assertRaises(conversions_refactored.ConversionNotPossible,conversions_refactored.convert,"Meters", "Fahrenheit", 100)
        print("passed: Meters to Fahrenheit correctly raised ConversionNotPossible")

        print("Test: Miles to Celsius should raise ConversionNotPossible")
        self.assertRaises(conversions_refactored.ConversionNotPossible,conversions_refactored.convert,"Miles", "Celsius", 100)
        print("passed: Miles to Celsius correctly raised ConversionNotPossible")

if __name__ == '__main__':
    unittest.main(verbosity=2)