# Write a program to request a temperature in Celsius and covert it to
# Fahrenheit.  Perform conversions until the value -999 is entered.

print("This program will convert a temperature in Celsius to Fahrenheit.")

stop_value = -999
celsius = 0

while celsius != stop_value:
    celsius = input("Enter a temperature in Celsius> ")
    celsius = float(celsius)

    if (celsius != stop_value):
        fahrenheit = (celsius * 9.0) / 5.0 + 32.0
        print(f"{celsius} Celsius is {fahrenheit} Fahrenheit")
