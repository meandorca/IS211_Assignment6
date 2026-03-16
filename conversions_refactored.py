
class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):

    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    distance_units = ["Miles", "Yards", "Meters"]

    if fromUnit in temp_units and toUnit in temp_units:
        if fromUnit == toUnit:
            return value

        if fromUnit == "Celsius":
            c = value
        elif fromUnit == "Fahrenheit":
            c = (value - 32) * 5/9
        elif fromUnit == "Kelvin":
            c = value - 273.15

        if toUnit == "Celsius":
            return c
        elif toUnit == "Fahrenheit":
            return (c * 9/5) + 32
        elif toUnit == "Kelvin":
            return c + 273.15

    elif fromUnit in distance_units and toUnit in distance_units:

        meters = {
            "Meters": 1,
            "Yards": 0.9144,
            "Miles": 1609.34
        }

        value_in_meters = value * meters[fromUnit]
        return value_in_meters / meters[toUnit]

    else:
        raise ConversionNotPossible