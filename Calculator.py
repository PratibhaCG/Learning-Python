# Options to choose from
print("Choose an option from the following:")
print("(1) Add(+)")
print("(2) Subtract(-)")
print("(3) Multiply(*)")
print("(4) Divide(/)")
print("(5) Find Remainder(%)")
print("(6) Find Quotient(//)")
print("(7) Find Square of a number(**)")

# Enter an option for calculation
c = int(input("Option selected from 1 to 7: "))

# Enter first number
a = int(input("Enter 1st number: "))

# Enter second number
b = int(input("Enter 2nd number: "))

# If elif else condition to create the calculator
# Addition
if c == 1:
    print("Output is: ")
    d = a+b
    print(d)

# Subtraction
elif c == 2:
    print("Output is: ")
    d = a-b
    print(d)

# Multiplication
elif c == 3:
    print("Output is: ")
    d = a*b
    print(d)

# Division
elif c == 4:
    print("Output is: ")
    d = a/b
    print(d)

# Find the remainder
elif c == 5:
    print("Output is: ")
    d = a%b
    print(d)

# Find the quotient
elif c == 6:
    print("Output is: ")
    d = a//b
    print(d)

# Find the square root
elif c == 7:
    d = a**b
    print(d)

# If wrong option selected
elif c == 0
    print("Wrong option selected")

else c > 7
    print("Wrong option selected")
