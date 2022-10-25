# Enter a numeric value
#a = int(input("Enter a positive integer: "))

# Check if a is a positive integer


#print(f"The fibonacci sequence will start from <{a}>")

# Check if a is a fibonacci number else pick first fibonacci number after that - first loop and then once done, print the first number after a

# Ask for the number of times to be printed
b = int(input("How many fibonacci numbers you wish to print?\n"))

# Print statement
print(f"Printing {b} fibonacci numbers")

# Printing the output
n0 = 0
n1 = 1
if b < 0:
    print("Incorrect input")

elif b == 0:
    print("Input should be at least 1")

elif b == 1:
    print(n0)

elif b == 2:
    print(n0,n1)

#elif a > 1 and a <= 2
 #   print (2)

#elif a > 2 and a <= 3
 #   print (3)



else:
    print(f"{n0} \n{n1}")
    for i in range(b-2):
       n = n0 + n1
       n0 = n1
       n1 = n
       i += 1
       print (n)
