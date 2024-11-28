# String
g = "Hello"
g2 = 'Hello'

print(g)
print(g2)

# String Methods
a = "Hello World again"
b = "Hello-World-Twice"

print(a.strip()) 
print(a.lower())
print(a.upper())
print(a.capitalize())
print(a.title())
print(a.replace("W", "M"))
print(a.split())
print(b.split("-"))

x = "hello" in b
print(x)

age = 30
name = " My name is Ahamed and my age is {}"

print(name.format(age))

first_anme = "Abdallah"
print(f"Welcome to you mr. {first_anme}")


#Escape character 
print("Hello\
    world")
aa = """ 
oen 
tow 
three
"""

print(aa)

bb = "Good\nday"
pp = "Good\tday"
print(bb)
print(pp)

dx = "1234567\rABCD"
print(dx)