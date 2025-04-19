class Calculator:
    def __init__(self, a,b):
        self.a = a
        self.b = b

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
    
fnumber1 = input("Enter the first number: ")
fnumber2 = input("Enter the second number: ")

a = int(fnumber1)
b = int(fnumber2)

print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")
print("5. Power")
print("6. Modulus")

operation = input("Enter the number corresponding to the operation that you wish to perform:\n")
operation = int(operation)

calci = Calculator(a,b)

if operation == 1:
    result = calci.add()
elif operation == 2:
    result = calci.subtract()
elif operation == 3:
    if b == 0:
        result = "Please enter a digit > 0"
    else:
        result = calci.divide()
elif operation == 4:
    result = calci.multiplication()
elif operation == 5:
    result = calci.power()
elif operation == 6:
    result = calci.modulus()
else:
    result = "Invalid Input"

print("Result is:", result)