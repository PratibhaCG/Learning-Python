#Enter a string value
a = input("Enter a string value: ")

#Print out the string value
print(f"You've entered the string <{a}>")

#Apply method lower to the string value
b = str.lower(a)

#Print the output
print(f"applying method lower() on string <{a}>")
print(f"Result is: {b}")

#Apply method upper to the string value
c = str.upper(a)

#Print the output
print(f"applying method upper() on string <{a}>")
print(f"Result is: {c}")

#Apply method title to the string value
d = str.title(a)

#Print the output
print(f"applying method title() on string <{a}>")
print(f"Result is: {d}")

#Apply method swapcase to the string value
e = str.swapcase(a)

#Print the output
print(f"applying method swapcase() on string <{a}>")
print(f"Result is: {e}")