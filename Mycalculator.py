# Get user inputs for numbers
fnumber1 = input("Enter first number: ")
fnumber2 = input("Enter second number: ")

# Converting the number inputted to integer as the "input func" always returns a string
a = int(fnumber1)
b = int(fnumber2)

# Menu for selecting operation
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")
print("5. Power")
print("6. Modulus")

# Get user's operation choice
operation = input("Enter the number corresponding to the operation that you wish to perform:\n")

# Convert to int as input returns a string
operation = int(operation)

# Perform calculation as per the user's choice
if operation == 1:
    result = a+b
elif operation == 2:
    result = a-b
elif operation == 3:
    if b == 0:
        result = "Please enter a digit > 0"
    else:
        result = a/b
elif operation == 4:
    result = a*b
elif operation == 5:
    result = a**b
elif operation == 6:
    result = a%b
else:
    result = "Invalid Input"

# Print output of the result
print("Result is: ", result)
