# Data Types

# Numbers
x = 5
y = 10.1
print(x) # int = integer 
print(y) # float = floating point 
print(type(x))
print(type(y))

# string
first_name = 'Mohamed' # str = string 
second_name = "Gbreel" # str = string 
print(first_name)
print(second_name)
print(type(first_name))
print(type(second_name))


# boolean
fr = 5
fb = 8
print(type(fb > fr)) # bool = boolean

cars = ["BMW", "Ford", "Lambourghini"]
print(type(cars))

colors = ("Red", "Blue", "Syan") # Tuple 
print(type(colors))

student = {"name": "Ali", "age": 35}
print(type(student)) # dict = dictionary

fruits = {"orange", "banana", "charry"}
print(fruits)
print(type(fruits)) # set = set 

fruits2 = frozenset({"orange", "banana", "charry"})
print(type(fruits2)) # frozenset = frozenset

x = b"hello"
print(type(x)) # bytes = bytes

b = bytearray(10)
print(type(b)) # bytearray = bytearray

c = memoryview(bytes(5))
print(type(c)) # memoryview = memoryview

d = 1j
print(type(d)) # complex = complex