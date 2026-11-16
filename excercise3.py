
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[0])
print(fruits[-1])

print("{} {}".format("Fruits from index 1 to 2:",  fruits[1:3]))

print("-------------------------------------------")

cars = ["maruti", "jaguar", "henry", "camry"]
print(cars[1])
print(cars[-1])
print(cars[1:3])
cars.insert(2, "Jazz")
print(cars)
cars.append("WagonR")
print(cars)
print("{}{}".format("cars from index 1 to 3: ", cars[1:3]))

cars[4] = "CAMRY"
print(cars)
del cars[2]
print(cars)