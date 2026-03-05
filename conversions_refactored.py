# conversions_refactored

class ConversionNotPossible(Exception):
    pass

conversion_map = {
    ("Celsius", "Kelvin"): (1, 273.15),
    ("Miles", "Yards"): (1760, 0),
    ("Miles", "Meters"): (1609.34, 0),
    ("Fahrenheit", "Celsius"): (5/9, -32 * 5/9),
    ("Celsius", "Fahrenheit"): (9/5, 32),
    ("Fahrenheit", "Kelvin"): (5/9, 255.372),
    ("Kelvin", "Celsius"): (1, -273.15),
    ("Kelvin", "Fahrenheit"): (9/5, -459.67),
    ("Yards", "Miles"): (1/1760, 0),
    ("Yards", "Meters"): (0.9144, 0),
    ("Meters", "Miles"): (1/1609.34, 0),
    ("Meters", "Yards"): (1.09361, 0),
}

def convert(fromUnit, toUnit, value):
    if fromUnit == toUnit:
        return float(value)
    if (fromUnit, toUnit) not in conversion_map:
        raise ConversionNotPossible((f"Conversion from {fromUnit} to {toUnit} is not possible."))
    factor, offset = conversion_map[(fromUnit, toUnit)]
    return float(value * factor + offset)

       