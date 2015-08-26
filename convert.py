#convert.py
# This program will convert tempratures.

def main():
    print ("This program will convert measurements")
    print ("1) Temprature Conversion")
    print ("2) Length Conversion")
    conversion_type = input("Enter conversion type: ")

    if conversion_type == 1:
        print ("1) Celsius to Fahrenheit")
        print ("2) Fahrenheit to Celsius")
        conversion_type = 10 + input("Enter conversion type: ")

        if conversion_type == 11:
            celsius = input("What is the temprature (celsius)? ")
            fahrenheit = 9.0/5.0 * celsius + 32.0
            print("The temprature is " + str(fahrenheit) + "oF")
        if conversion_type == 12:
            fahrenheit = input("What is the temprature (fahrenheit)? ")
            celsius = 5.0 * (fahrenheit - 32.0) / 9.0
            print("The temprature is " + str(celsius) + "oFC")

    if conversion_type == 2:
        original_length = input("Please input length: ")
        print ("What type of units?")
        print ("m - meters, cm - centermeters, km - kilometers, mm - millimeter")
        print ("mi - miles, yd - yards, ft - feet, in - inches")
        print ("na - Nautical Mile, ly - light year")
        original_unit = raw_input("Enter original units: ")
        new_unit = raw_input("Enter units to convert to: ")
        new_length = original_length * length_factor(original_unit) / length_factor(new_unit)
        print (str(original_length) + original_unit + " = " + str(new_length) + new_unit)


def length_factor(unit):
    factor = 0
    unit = unit.lower()

    if unit == "m":
        factor = 1.0
    if unit == "cm":
        factor = 0.01
    if unit == "km":
        factor = 1000
    if unit == "mm":
        factor = 0.001
    if unit == "mi":
        factor = 1609.34
    if unit == "yd":
        factor = 0.9144
    if unit == "in":
        factor = 0.0254
    if unit == "ft":
        factor = 0.3048
    if unit == "na":
        factor = 1852
    if unit == "ly":
        factor = 9.4605284 * 10**15

    return factor


main()
