# Lists, tuples, and sets

"""
## Lists
 * You can modify a list
 * It keeps it's order
"""

l = ["Jane", "Stacy", "Anna"]
print(l[0]) # Subscript notation
l[1] = "Laura"
l.append("Amanda")
l.remove("Anna")


"""
## Tuples
 * You can't modify a tuple
 * It keeps it's order
"""
t = ("Jane", "Stacy", "Anna")
print(t[0]) # Subscript notation
# t[1] = "Laura" # Errors
# t.append("Amanda") # Errors
# t.remove("Anna") # Errors

"""
## Sets
 * You can modify a set
 * Duplicates are not allowed
 * The order isn't guaranteed
 * You cannot use subscript notation to access items
"""
s = {"Jane", "Stacy", "Anna"}
print()
s.add("Anna") # Append adds at the end, since order isn't guaranteed you can't append
s.add("Anna") # Ignored as duplicates aren't allowed
