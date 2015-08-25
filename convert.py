#convert.py
# This program will convert celsius to fahrenheit

def main():
    print ("This program will convert a Celsius temprature to Fahrenheit.")
    print ("The program will loop 5 times.")

    for i in range(5):
        celsius = input("What is the temprature (celsius)? ")
        fahrenheit = 9.0/5.0 * celsius +32.0
        print("The temprature is " + str(fahrenheit) + "oF")

main()
