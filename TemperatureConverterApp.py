# Define a Temperature class to encapsulate the conversions
class Temperature:

# Constructor to initialize the three tempaerature methods
    def __init__(self, temp):
        self.temp = temp

# Methods to perform operation
#Celsius (°C) Conversions
    def celsius_to_fahrenheit(self): # start editing from here
        return (self.temp * 9/5) + 32
    def celsius_to_kelvin(self):
        return (self.temp + 273.15)

#Kelvin(°K) Conversions
    def kelvin_to_celsius(self):
        return (self.temp - 273.15) 
    def kelvin_to_fahrenheit(self):
        return (self.temp - 273.15)* 9/5 +32
    
#Fahrenheit(°F) Conversions
    def fahrenheit_to_celsius(self):
        return (self.temp - 32) * 5/9 
    def fahrenheit_to_kelvin(self):
        return (self.temp - 32) * 5/9 + 273.15

# Display the menu of conversion units for the user to select
print("Kindly choose the conversion method")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Kelvin to Celsius")
print("4. Kelvin to Fahrenheit")
print("5. Fahrenheit to Celsius")
print("6. Fahrenheit to Kelvin")

try:
    temp_unit = input("Kindly enter the corresponding value from the above menu: \n").strip()
    temp = int(temp_unit)
    if temp not in range(1,7):
        print("Invalid menu option. Please select a number between 1 and 6")
        exit()

except ValueError:
    print("Please enter the menu numbers only from the above list of 1 to 6")
    exit()

# Get user input for the two numbers    
try:
    temperature_value = input("Enter the temperature in the unit chosen previously to ensure accurate results: ")
    temp_v = float(temperature_value)

except ValueError:
    print("Please enter a valid numberic temperature value")
    exit()

#creating an object called tempconv in order to call the same later
tempconv = Temperature(temp_v)
unit = None

# If user chooses the unit to be Celsius
if temp == 1: # meaning the input was in Celsius
    temp_v = tempconv.celsius_to_fahrenheit() # call the obj func to convert
    unit = "°F"
elif temp == 2:
    temp_v = tempconv.celsius_to_kelvin()
    unit = "°K"
elif temp == 3:
    temp_v = tempconv.kelvin_to_celsius()
    unit = "°C"
elif temp == 4:
    temp_v = tempconv.kelvin_to_fahrenheit()
    unit = "°F"
elif temp == 5:
    temp_v = tempconv.fahrenheit_to_celsius()
    unit = "°C"
elif temp == 6:
    temp_v = tempconv.fahrenheit_to_kelvin()
    unit = "°K"

else:
    temp_v = "Invalid Input"

if unit:
    print(f"Converted temperature is: {temp_v:.2f}{unit}")
else:
    print("Invalid Input")
    


