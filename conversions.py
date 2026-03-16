def convertCelsiusToKelvin(celsius):
    return celsius + 273.15


def convertCelsiusToFahrenheit(celsius):
    return (celsius * 9/5) + 32

def convertFahrenheitToCelsius(f):
    return (f - 32) * 5/9


def convertFahrenheitToKelvin(f):
    return (f - 32) * 5/9 + 273.15


def convertKelvinToCelsius(k):
    return k - 273.15


def convertKelvinToFahrenheit(k):
    return (k - 273.15) * 9/5 + 32