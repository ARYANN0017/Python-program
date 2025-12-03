def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

while True:
    time = int(input("How many times calculation do you want perform? "))

    for x in range(time):
        print(f"\nCalculator {x + 1}")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter your choice number: "))

        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == 2:
                print(f"{num1} - {num2} = {sub(num1, num2)}")
            elif choice == 3:
                print(f"{num1} * {num2} = {mul(num1, num2)}")
            elif choice == 4:
                print(f"{num1} / {num2} = {div(num1, num2)}")
        else:
            print("E R R O R: Invalid choice!")

    again = input("Do you want to perform another set of calculations? (y/n): ")
    if again != 'y':
        break
