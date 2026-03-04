import conversions
import unittest

class TestConversions(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):

        print("Test1: 0°C should equal 273.15 K")
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(0), 273.15, places=2)
        print("passed: 0°C correctly converted to 273.15 K")

        print("Test2: 100°C should equal 373.15 K")
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(100), 373.15, places=2)
        print("passed: 100°C correctly converted to 373.15 K")

        print("Test3: 300°C should equal 573.15 K")
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(300.0), 573.15, places=2)
        print("passed: 300°C correctly converted to 573.15 K")

        print("Test4: -40°C should equal 233.15 K")
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(-40.0), 233.15, places=2)
        print("passed: -40°C correctly converted to 233.15 K")

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

    def test_convertFahrenheitToCelsius(self):

        print("Test1: 32°F should equal 0°C")
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(32), 0, places=2)
        print("passed: 32°F correctly converted to 0°C")

        print("Test2: 98.6°F should equal 37°C")
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(98.6), 37, places=2)
        print("passed: 98.6°F correctly converted to 37°C")

        print("Test3: 212°F should equal 100°C")
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(212), 100, places=2)
        print("passed: 212°F correctly converted to 100°C")

        print("Test4: -40°F should equal -40°C")
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(-40), -40, places=2)
        print("passed: -40°F correctly converted to -40°C")

        print("Test5: 572°F should equal 300 C")
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(572), 300, places=2)
        print("passed: 572°F correctly converted to 300 C")

    def test_convertFahrenheitToKelvin(self):

        print("Test1: 32°F should equal 273.15°K")
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(32), 273.15, places=2)
        print("passed: 32°F correctly converted to 273.15°K")

        print("Test2: 98.6°F should equal 310.15°K")
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(98.6), 310.15, places=2)
        print("passed: 98.6°F correctly converted to 310.15°K")

        print("Test3: 212°F should equal 373.15°K")
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(212), 373.15, places=2)
        print("passed: 212°F correctly converted to 373.15°K")

        print("Test4: -40°F should equal 233.15°K")
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(-40), 233.15, places=2)
        print("passed: -40°F correctly converted to 233.15°K")

        print("Test5: 572°F should equal 573.15°K")
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(572), 573.15, places=2)
        print("passed: 572°F correctly converted to 573.15°K")

    def test_convertKelvinToCelsius(self):

        print("Test1: 273.15 K should equal 0°C")
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(273.15), 0, places=2)
        print("passed: 273.15 K correctly converted to 0°C")

        print("Test2: 310.15 K should equal 37°C")
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(310.15), 37, places=2)
        print("passed: 310.15 K correctly converted to 37°C")

        print("Test3: 373.15 K should equal 100°C")
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(373.15), 100, places=2)
        print("passed: 373.15 K correctly converted to 100°C")

        print("Test4: 233.15 K should equal -40°C")
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(233.15), -40, places=2)
        print("passed: 233.15 K correctly converted to -40°C")

        print("Test5: 573.15 K should equal 300°C")
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(573.15), 300, places=2)
        print("passed: 573.15 K correctly converted to 300°C")

    def test_convertKelvinToFahrenheit(self):

        print("Test1: 273.15 K should equal 32°F")
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(273.15), 32, places=2)
        print("passed: 273.15 K correctly converted to 32°F")

        print("Test2: 310.15 K should equal 98.6°F")
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(310.15), 98.6, places=2)
        print("passed: 310.15 K correctly converted to 98.6°F")

        print("Test3: 373.15 K should equal 212°F")
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(373.15), 212, places=2)
        print("passed: 373.15 K correctly converted to 212°F")

        print("Test4: 233.15 K should equal -40°F")
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(233.15), -40, places=2)
        print("passed: 233.15 K correctly converted to -40°F")

        print("Test5: 573.15 K should equal 572°F")
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(573.15), 572, places=2)
        print("passed: 573.15 K correctly converted to 572°F")

if __name__ == '__main__':
    unittest.main(verbosity=2)
