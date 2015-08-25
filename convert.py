#convert.py
# This program will convert celsius to fahrenheit

def main():
    print ("This program will convert a Celsius temprature to Fahrenheit.")
    print ("It will create a table of every 10oC from 0 - 100")

    print ("   oC     |    oF    ")
    print ("----------|----------")
    for i in range(11):
        celsius = i * 10.0
        fahrenheit = 9.0/5.0 * celsius +32.0

        if celsius < 10.0:
            spacer1 = "  "
        elif celsius < 100.0:
            spacer1 = " "
        else:
            spacer1 = ""

        if fahrenheit < 10.0:
            spacer2 = "  "
        elif fahrenheit < 100.0:
            spacer2 = " "
        else:
            spacer2 = ""


        print("  " + spacer1 + str(celsius) + "   |  " + spacer2 + str(fahrenheit))

main()
