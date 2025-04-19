fnumber1 = input("Enter first number: ")
fnumber2 = input("Enter second number: ")
a = int(fnumber1)
b = int(fnumber2)
operation = input("Choose the operation you want to perform from the below: Enter + for addition \n Enter - for subtraction")
if operation == "+":
    result = a+b
elif operation == "-":
    result = a-b
else:
    result = "Invalid Input"
print("Result is: ", result)

