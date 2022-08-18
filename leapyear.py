# Enter an Year for calculation
a = int(input("Enter an Year: "))
print("Checking if", a, "is a Leap Year")

# Conditions to check if Leap Year
if a%400 == 0:
    print(a, "is a Leap Year as it is divisible by 400.")

elif a%100 == 0:
    print(a, "is not a Leap Year as it is divisible by 100 but not by 400.")

elif a%4 == 0:
    print (a, "is a Leap Year as it is divisible by 4 but not by 100 or 400.")





