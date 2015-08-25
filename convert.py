#convert.py
# This program will convert celsius to fahrenheit

def main():
    print ("This program will convert measurements")
    print ("1) Celsius to Fahrenheit")
    print ("2) Fahrenheit to Celsius")
    conversion_type = input("Enter conversion type: ")

    if conversion_type == 1:
        celsius = input("What is the temprature (celsius)? ")
        fahrenheit = 9.0/5.0 * celsius + 32.0
        print("The temprature is " + str(fahrenheit) + "oF")

    if conversion_type == 2:
        fahrenheit = input("What is the temprature (fahrenheit)? ")
        celsius = 5.0 * (fahrenheit - 32.0) / 9.0
        print("The temprature is " + str(celsius) + "oFC")

main()
