# String formatting in Python

name = "Bob"
greeting = f"Hello, {name}"
print(greeting)

name = "Rolf"
print(f"Hello, {name}")

greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)

print(greeting.format("Jane"))

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Lucy", "Tuesday")
print(formatted)