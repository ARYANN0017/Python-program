import random

letters = "ABCDEFGHIJJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()?"

while True:

    length = int(input("Enter length of password: "))

    if length < 10:
        print("Your password is Weak")
    else:
        print("Your password is too Strong")

    password = ""

    for i in range(length):
        password += random.choice(letters)

        # password just a variable name and then += assignment operator and after random.choice this part of call random libraries.
    print(" your Generated password is --- \033[4m",password)

    # \033[4m is code to under-line

    again = input("Do you agree to continue? (y/n): ")
    if again == 'n':
        print("Thank you for using this program")
    if again == 'y':
        print("Re-start Your program")