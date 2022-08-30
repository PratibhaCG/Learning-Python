#Enter a numeric value
a = int(input("Enter a numeric value: "))
print(f"You've entered the value: {a}")

#Enter the number of values to be returned
n = int(input("Enter number of values to be returned: "))
print(f"You've entered the number of values to be returned: {n}")

#Use a loop function to find the even numbers
if a %2 == 0:
    a = a+1
i = 0
print(f"Printing {n} even numbers after {a}")
while i<=n:
    a = a+2
    print(a)
    i += 1