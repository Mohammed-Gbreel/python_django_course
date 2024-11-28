# Lists
# List is a collection whitch is ordered and changeable and allows duplicate members.

cars = ["BMW", "Ford", "Lambourghini", "Marcides", "Poghati"]
print(cars)

# Print one value depends on index
print(cars[2]) # Lambourghini
print(cars[0]) # BMW

# Slicing 
print(cars[2:4]) # 4 is not included
print(cars[0:]) # print all values inside list
print(cars[:])

print(cars[-4:-1]) # Start from the last member into the list

# Change the item value 
cars[4] = "Orange"
print(cars)

# Loop Through the list
for car in cars:
    print("My Car is : " + car)


# Check values in 
if "BMW" in cars:
    print("Purches the BMW")
else:
    print("My favorit car is not in your cars")


if "Kia" in cars:
    print("Purches the Kia")
else:
    print("My favorit car is not in your cars")


# List Length = count all members into the list
print(len(cars))

# Adding item to the list (append) = add item in the last
cars.append("Kia")
print(cars)

# Adding with insert = add item in spacific place
cars.insert(0, "BYD")
print(cars)
print(cars[0])

# Remove item from the list (remove)
cars.remove("Marcides")
print(cars)

# Remove item with (pop) = spacific index
cars.pop(4) # you will rempove last item if don't given index
print(cars)

# Delete remove specified index
del cars[3]
print(cars)

# Remove all the list
# del cars
# print(cars)

# Copy list (copy)
car = ["BMW", "Ford", "Lambourghini", "Marcides", "Poghati"]

y = car.copy()
print(y)

# copy with list 
x = list(car)
print(x)



# Join to list
a = [1,2,3,4]
b = [5,6,7,8]

c = a + b
print(c)

for c in a:
    a.append(b)
print(b)

# extend 
a.extend(b)
print(a)