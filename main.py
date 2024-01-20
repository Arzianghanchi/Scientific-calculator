import math

def tk():
    print(f"Thanks for using it")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)



# Main program loop
while True:
    print("Scientific Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '0':
        print("Exiting...")
        break

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            print("Result:", result)
            tk()
        elif choice == '2':
            result = subtract(num1, num2)
            print("Result:", result)
            tk()
        elif choice == '3':
            result = multiply(num1, num2)
            print("Result:", result)
            tk()
        elif choice == '4':
            result = divide(num1, num2)
            print("Result:", result)
            tk()

    elif choice == '5':
        num = float(input("Enter a number: "))
        result = square_root(num)
        print("Result:", result)
        tk()

    elif choice == '6':
        num1 = float(input("Enter base number: "))
        num2 = float(input("Enter exponent number: "))
        result = power(num1, num2)
        print("Result:", result)
        tk()

    else:
        print("Invalid choice. Please try again.")
