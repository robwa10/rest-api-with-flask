# Getting user input

name = input("Enter your name: ")
print(name)

# Input always gives back a string.
# You can't do maths on strings.
size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8

print(f"Your house is {round(square_metres, 2)} square meters.")
print(f"Your house is {square_metres:.2f} square meters.")