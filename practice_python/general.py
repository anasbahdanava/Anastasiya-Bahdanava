
my_string = "Hello, world"

my_string = """  long text

"""

first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
length = len(full_name)
print(length)
print(full_name)

my_integer = 100
my_string = str(my_integer)
print(type(my_string))

my_string = input("Enter a number: ")
print(type(my_string))

big_integer = 2 ** 1000
print(len(str(big_integer)))

my_string = "Hello, world"
print("Hello" in my_string)

my_string = "Alice"
print(my_string.upper())
print(my_string.lower())

my_string = "      Hello, world    "
print(len(my_string))
print(len(my_string.strip()))

my_string = "Hello, world"
print(my_string.replace("world", "Python"))

my_string = "Hello, world"
print(my_string.count("l"))

my_string = "10"
print(my_string.isdigit())

name = "Alice"
age = 25
print(f"Hello, my namme is {name} and I'm {age} years old")