# Enter string value
a = input("Enter a string value:")

# Confirm the entry
print (f"You've entered: {a}")

#Find length of string
n = len(a)

# Slice after removing first and last character
b = a[1:n-1]
print(f"Slice of '{a}' after removing first and last characters is '{b}'")

#Slice after removing the first 2 characters
c = a[2:n]
print(f"Slice of '{a}' after removing first 2 characters is '{c}'")

#Slice after removing the last 2 characters
d = a[:n-2]
print(f"Slice of '{a}' after removing last 2 characters is '{d}'")

#mid index
e = int(n/2)
print(f"mid index is {e}")

#Print the first half & second half of a string
f = a[:e]
print(f"First half slice of '{a}' is '{f}'")

g = a[e:]
print(f"Second half slice of '{a}' is '{g}'")


