#Enter a string value
a = input("Enter a string value: ")

#Print the string
print(f"You entered the string <{a}>")

#Printing the characters one by one
print(f"Printing characters of <{a}>")

#Loop function to iterate and print each character
i = 0
while(i<len(a)):
    print(a[i])
    i=i+1

#Printing the characters in reverse
print(f"Printing characters of {a} in reverse")

#Loop function to iterate and print each character in reverse
#Loop function to iterate and print each character in reverse
i = len(a)-1
while(i>=0):
    print(a[i])
    i-=1


