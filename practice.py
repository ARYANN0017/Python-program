# i=int(input("enter your num:"))
#
# if i<=5:
#     print(i,"your number is small")
# elif i<=10:
#     print(i,"your number is middle")
# else:
#     print(i,"your number is big")




# n=int(input("enter your number:"))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#              print("not prime")
#              break
#         else:
#              print("prime")
# else:
#     print("not prime")


def fact(n):
    if n == 0 or n == 1:   # base condition
        return 1
    else:
        return n * fact(n - 1)

# taking input
num = int(input("Enter a number: "))

print("Factorial =", fact(num))
