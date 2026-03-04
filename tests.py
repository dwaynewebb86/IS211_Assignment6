from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit
import unittest

class TestConversions(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):

        print("Test1: 0°C should equal 273.15 K")
        self.assertAlmostEqual(convertCelsiusToKelvin(0), 273.15, places=2)
        print("passed")

        print("Test2: 100°C should equal 373.15 K")
        self.assertAlmostEqual(convertCelsiusToKelvin(100), 373.15, places=2)
        print("passed")

        print("Test3: 300°C should equal 573.15 K")
        self.assertAlmostEqual(convertCelsiusToKelvin(300.0), 573.15, places=2)
        print("passed")

        print("Test4: -40°C should equal 233.15 K")
        self.assertAlmostEqual(convertCelsiusToKelvin(-40.0), 233.15, places=2)
        print("passed")

        print("Test5: -273.15°C should equal 0 K")
        self.assertAlmostEqual(convertCelsiusToKelvin(-273.15), 0, places=2)
        print("passed")

    def test_convertCelsiusToFahrenheit(self):

        print("Test 1: 0°C should equal 32.0°F")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(0), 32, places=2)
        print("passed")

        print("Test 2: 100°C should equal 212.0°F")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(100), 212, places=2)
        print("passed")

        print("Test 3: 300°C should equal 572.0°F")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(300), 572.0, places=2)
        print("passed")

        print("Test 4: -40°C should equal -40.0°F")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(-40), -40, places=2)
        print("passed")

        print("Test 5: 37°C should equal 98.6°F")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(37), 98.6, places=2)
        print("passed")

if __name__ == '__main__':
    unittest.main(verbosity=2)
