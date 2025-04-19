# Define a Calculator class to encapsulate the operations
class Calculator:
# Constructor to initialize the two numbers
    def __init__(self, a,b):
        self.a = a
        self.b = b
        
# Methods to perform operation
    def add(self):
        return self.a+self.b
    def subtract(self):
        return self.a-self.b
    def divide(self):
        return self.a/self.b
    def multiplication(self):
        return self.a*self.b
    def power(self):
        return self.a**self.b
    def modulus(self):
        return self.a%self.b
        
# Get user input for the two numbers    
fnumber1 = input("Enter the first number: ")
fnumber2 = input("Enter the second number: ")

# Convert input strings to integers
a = int(fnumber1)
b = int(fnumber2)

# Display the menu of operations for the user to select
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")
print("5. Power")
print("6. Modulus")

# Get the operation choice from the user and convert to int as the input fun returns a string
operation = input("Enter the number corresponding to the operation that you wish to perform:\n")
operation = int(operation)

# Create an instance of the Calculator class with the user-provided numbers
calci = Calculator(a,b)

# Perform the selected operation based on user's choice
if operation == 1:
    result = calci.add()  # Call the add method
elif operation == 2:
    result = calci.subtract() # Call the subtract method
elif operation == 3:
# Check for division by zero
    if b == 0:
        result = "Please enter a digit > 0" # Handle division by zero error
    else:
        result = calci.divide()  # Call the divide method
elif operation == 4:
    result = calci.multiplication()
elif operation == 5:
    result = calci.power()
elif operation == 6:
    result = calci.modulus()
else:
    result = "Invalid Input" # Handle invalid operation inpu

print("Result is:", result)
