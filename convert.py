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
        print ("1) Kilometers to Miles")
        print ("2) Miles to Kilometers")
        conversion_type = 20 + input("Enter conversion type: ")

        if conversion_type == 21:
            km = input("What is the length (kilometers)? ")
            miles = 0.621371 * km
            print("The length is " + str(miles) + " miles")
        if conversion_type == 22:
            miles = input("What is the length (miles)? ")
            km = 1.60934 * miles
            print("The length is " + str(km) + "km")






main()
