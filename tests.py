import conversions
import unittest

class TestConversions(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):

        print("Test1: 0°C should equal 273.15 K")
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(0), 273.15, places=2)
        print("passed: 0°C correctly converted to 273.15 K")

        print("Test2: 100°C should equal 373.15 K")
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(100), 373.15, places=2)
        print("passed: 100°C correctly converted to 3733.15 K")

        print("Test3: 300°C should equal 573.15 K")
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(300.0), 573.15, places=2)
        print("passed: 300°C correctly converted to 573.15 K")

        print("Test4: -40°C should equal 233.15 K")
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(-40.0), 233.15, places=2)
        print("passed: -40°C correctly converted to 273.15 K")

        print("Test5: -273.15°C should equal 0 K")
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(-273.15), 0, places=2)
        print("passed: -273.15°C correctly converted to 0 K")

    def test_convertCelsiusToFahrenheit(self):

        print("Test1: 0°C should equal 32.0°F")
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(0), 32, places=2)
        print("passed: 0°C correctly converted to 32.0°F")

        print("Test2: 100°C should equal 212.0°F")
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(100), 212, places=2)
        print("passed: 100°C correctly converted to 212.0°F")

        print("Test3: 300°C should equal 572.0°F")
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(300), 572.0, places=2)
        print("passed: 300°C correctly converted to 572.0°F")

        print("Test4: -40°C should equal -40.0°F")
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(-40), -40, places=2)
        print("passed: -40°C correctly converted to -40.0°F")

        print("Test5: 37°C should equal 98.6°F")
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(37), 98.6, places=2)
        print("passed:: 37.0°C correctly converted to 98.6°F")

class TestConversions(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):
        # call your function and check the result
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(celsius), 300, places=2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
