# Tuple data type
fruit = ("banana", "ornge", "mango", "melon", "banana")
print(fruit)

# Access tuple 
print(fruit[2])
print(fruit[2:5])

# fruit[1] = "cherry"
x = list(fruit)
print(type(x))
print(x)
x[1] = "charry"
print(x)

fruit = tuple(x)
print(type(fruit))
print(fruit)

names = ("Mohamed")
names2 = ("Mohamed",)
print(type(names))
print(type(names2))

# Loop through tuples
for i in fruit:
    print(i)


# Check 
if "mango" in fruit:
    print("Mango is good")
else:
    print("You shoud test it")

num1 = (1,2,3)
num2 = (4,5,6)
num3 = num1 + num2
print(num3)