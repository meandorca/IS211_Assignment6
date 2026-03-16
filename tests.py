import conversions


def test_celsius_to_kelvin():
    print("Testing Celsius to Kelvin")

    tests = [
        (0, 273.15),
        (100, 373.15),
        (-273.15, 0),
        (25, 298.15),
        (300, 573.15)
    ]

    for c, expected in tests:
        result = conversions.convertCelsiusToKelvin(c)
        print(f"{c}C -> expected {expected}K, got {result}")


def test_celsius_to_fahrenheit():
    print("Testing Celsius to Fahrenheit")

    tests = [
        (0, 32),
        (100, 212),
        (-40, -40),
        (25, 77),
        (300, 572)
    ]

    for c, expected in tests:
        result = conversions.convertCelsiusToFahrenheit(c)
        print(f"{c}C -> expected {expected}F, got {result}")

test_celsius_to_kelvin()
test_celsius_to_fahrenheit()


import conversions_refactored as cr

print("\nRefactored Temperature Tests")

print("0 Celsius -> Kelvin:", cr.convert("Celsius", "Kelvin", 0))
print("100 Celsius -> Fahrenheit:", cr.convert("Celsius", "Fahrenheit", 100))
print("32 Fahrenheit -> Celsius:", cr.convert("Fahrenheit", "Celsius", 32))
print("300 Kelvin -> Celsius:", cr.convert("Kelvin", "Celsius", 300))


print("\nDistance Tests")

print("1 Mile -> Meters:", cr.convert("Miles", "Meters", 1))
print("10 Yards -> Meters:", cr.convert("Yards", "Meters", 10))
print("1000 Meters -> Miles:", cr.convert("Meters", "Miles", 1000))


print("\nSame Unit Tests")

print("10 Celsius -> Celsius:", cr.convert("Celsius", "Celsius", 10))
print("5 Miles -> Miles:", cr.convert("Miles", "Miles", 5))


print("\nException Test")

try:
    cr.convert("Celsius", "Meters", 10)
except cr.ConversionNotPossible:
    print("Exception worked correctly")