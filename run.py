thon programming topics:

Python Functions
Python Function Arguments
Python User-defined Functions
Example: Simple Calculator by Using Functions
import
# Program make a simple calculator

# This function adds two numbers
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

def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def bann_text():
    clr()
    logo = """
   _____      _            _       _             
  / ____|    | |          | |     | |            
 | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |___| (_| | | (__| |_| | | (_| | || (_) | |   
  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                 
                                         """        


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
