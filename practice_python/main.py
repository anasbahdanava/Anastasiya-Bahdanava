print ("Hello","world", sep=", ")
print ("first row")
print ("second row")

name = input("Enter your name: ")
print(name)

name = "Alice"
print(name)

age = 25
print(name,age)
other_name=name

x=3
y=4
x, y = y, x
print(x, y)

variable=1
print(type(variable))

my_integer = 10
my_float = 20.5

summary = x + y
print(summary)
z = x / y


x = 2
print(x ** 3)

x = 9
y = 4
print(x // y)
print(x/y)
print(x%y)

my_float = 1.49
my_integer = int(my_float)
print(my_integer)

my_integer = round(my_float)

flat_number = 2
entrance_number = flat_number // 20 + 1
flat_number = 20
entrance_number = (flat_number - 1) // 20 + 1
print (entrance_number)

flat_number = 20
floor_number = (flat_number - 1 ) % 20 // 4 + 1
print(floor_number)

is_student = True
print(is_student)
is_graduated = False
print(is_graduated)


x = 10
y = 10
print(x == y)
print(x != y)

x = 1 
print(x <5 and x > -2)

is_student = True
print(not is_student)

print(bool(1))

if True:
    print("Hello, world")

x = 10
if x > 0:
    print("x is positive")

x = 0
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

x = 10
y = 20
if x > 0 and y > 0:
    print("x and y are positive")

message = "Hello, world"
if message:
    print("message is not empty")

x = 0
if x: 
    print("x is not zero")

year = 2000
if year % 4 == 0 and year % 100 != 0:
    print("Year is leap")
elif year % 400 == 0:
    print("Year is leap")
else:
    print("Year is not leap")

my_string = "Hello, world"

my_string = """  long text

"""

first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name



