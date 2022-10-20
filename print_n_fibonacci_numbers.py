# Enter a numeric value
a = int(input("Enter a number: "))
print(f"You've entered <{a}>")

# Ask for the number of times to be printed
b = int(input("How many fibonacci numbers you wish to print?\n"))

# Print statement
print(f"Printing {b} fibonacci numbers after {a}")

# Printing the output
n1, n2 = 0, 1
if b < 0:
    print("Incorrect input")

elif b == 0:
    print(0)

elif b == 1:
    print(1)

#elif a > 1 and a <= 2
 #   print (2)

#elif a > 2 and a <= 3
 #   print (3)



else:
   for i in range(0, b):
       c = a + n2
       a = n2
       n2 = c
       i += 1
       print (c)
