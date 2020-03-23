# Advanced set operations

friends = {"Jane", "Stacy", "Anna"}
local = {"Stacy"}
abroad = {"Jane", "Anna"}


# difference() takes one set and removes elements of another set from it
local_friends = friends.difference(abroad)
abroad_friends = abroad.difference(friends)
print(local_friends)
print(abroad_friends) # Returns an empty set as all items are removed


# union() unites two sets, remember duplicates are ignored
print(local.union(abroad))


# intersection() returns items that appear in both sets
art = {"Jane", "Stacy", "Amanda", "Laura"}
science = {"Jane", "Stacy", "Anna", "Lucy"}
print(art.intersection(science))
