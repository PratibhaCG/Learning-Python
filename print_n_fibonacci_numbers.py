# Enter a numeric value
#a = int(input("Enter a number: "))
#print(f"You've entered <{a}>")

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
    print(0)

elif b == 1:
    print(1)

#elif a > 1 and a <= 2
 #   print (2)

#elif a > 2 and a <= 3
 #   print (3)



else:
   for i in range(b-1):
       n = n0 + n1
       n0 = n1
       n1 = n
       i += 1
       print (n)
