# Define a Temperature class to encapsulate the conversions
import sys
class Temperature:
    def __init__(self, temp):
        self.temp = temp

    # Celsius (°C) Conversions
    def celsius_to_fahrenheit(self):
        return (self.temp * 9/5) + 32

    def celsius_to_kelvin(self):
        return self.temp + 273.15

    # Kelvin (K) Conversions
    def kelvin_to_celsius(self):
        return self.temp - 273.15

    def kelvin_to_fahrenheit(self):
        return (self.temp - 273.15) * 9/5 + 32

    # Fahrenheit (°F) Conversions
    def fahrenheit_to_celsius(self):
        return (self.temp - 32) * 5/9

    def fahrenheit_to_kelvin(self):
        return (self.temp - 32) * 5/9 + 273.15


while True:
    print("\nKindly choose the conversion method")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Kelvin to Celsius")
    print("4. Kelvin to Fahrenheit")
    print("5. Fahrenheit to Celsius")
    print("6. Fahrenheit to Kelvin\n")

    try:
        temp = int(input("Kindly enter the corresponding value from the above menu: ").strip())
        if temp not in range(1, 7):
            print("Invalid menu option. Please select a number between 1 and 6")
            continue
    except ValueError:
        print("Please enter a valid number from 1 to 6.")
        continue

    try:
        temp_val = float(input("Enter the temperature in the selected unit: ").strip())
    except ValueError:
        print("Please enter a valid numeric temperature.")
        continue

    tempconv = Temperature(temp_val)
    unit = ""

    if temp == 1:
        result = tempconv.celsius_to_fahrenheit()
        unit = "°F"
    elif temp == 2:
        result = tempconv.celsius_to_kelvin()
        unit = "K"
    elif temp == 3:
        result = tempconv.kelvin_to_celsius()
        unit = "°C"
    elif temp == 4:
        result = tempconv.kelvin_to_fahrenheit()
        unit = "°F"
    elif temp == 5:
        result = tempconv.fahrenheit_to_celsius()
        unit = "°C"
    elif temp == 6:
        result = tempconv.fahrenheit_to_kelvin()
        unit = "K"

    print(f"Converted temperature is: {result:.2f}{unit}")

    while True:
        final_inp = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
        if final_inp == "yes":
            break  # Go back to the main loop
        elif final_inp == "no":
            print("Thank you for using the temperature converter. Goodbye!")
            exit()
        else:
            print("Please enter only 'yes' or 'no'.")
