def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#chalenge 2: implement a calculator class
class calculator():
    def __init__(self):
        self.x = x
        self.y = y

    def add(self):
        print(self.x + self.y)

    def substract(self):
        print(self.y - self.x)

    def multiply(self):
        print(self.x*self.y)

    def divide(self):
        print(self.y /self.x)

x = float(input("enter your number:"))
y = float(input("enter your number:"))

calculator_obj=calculator()
calculator_obj.add()
calculator_obj.substract()
calculator_obj.multiply()
calculator_obj.divide()