#Enter a string value
a = input("Enter a string value: ")

#Print the string
print(f"You entered the string <{a}>")

#Printing the characters one by one
print(f"Printing characters of <{a}>")

#Loop function to iterate and print each character
for i in a:
    print(i)

#Printing the characters in reverse
print(f"Printing characters of {a} in reverse")

#Loop function to iterate and print each character in reverse
for i in range(len(a)-1, -1, -1):
    print(a[i])