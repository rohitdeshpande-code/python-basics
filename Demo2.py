
values = [1, 2, "rohit", "qa", 3, 4, 5]
#List is data type that allows multiple values and can be different data types, mutable/updatble
#represent in square brackets

print(values)
print(values[0]) #1
print(values[3]) #qa

print(values[-1]) #5 End value
print(values[1:3]) #substring [2, 'rohit']

values.insert(3, "deshpande")
print(values) #[1, 2, 'rohit', 'deshpande', 'qa', 3, 4, 5]

values.append(("End"))
print(values) #[1, 2, 'rohit', 'deshpande', 'qa', 3, 4, 5, 'End']

values[2] = "ROHIT" # lowercase to uppercase
print(values) #[1, 2, 'ROHIT', 'deshpande', 'qa', 3, 4, 5, 'End']

del values[0] # deletes the 0th value completely
print(values) #[2, 'ROHIT', 'deshpande', 'qa', 3, 4, 5, 'End']

print("----------------------------------------------------------")

# Tuple same as list data type but immutable where updation is not possible
#represents in circular brackets
val = (1, 2, "rohit", 4.5)

print(val[1]) #2

#val[2] = "ROHIT"  Error - 'tuple' object does not support item assignment

print(val) #(1, 2, 'rohit', 4.5)

# Dictionary - Key value pair based

print("----------------------------------------------------------")

dic = {"a":2, 4:"bcd", "c":"hello world"}

print(dic[4]) #bcd
print(dic["c"]) #hello world

# Empty dictionary

dict = {}

dict["firstname"] = "Rohit"

dict["lastname"] = "Deshpande"

dict["age"] = 40

dict["gender"] = "Male"

print(dict) #{'firstname': 'Rohit', 'lastname': 'Deshpande', 'age': 40, 'gender': 'Male'}
print(dict["firstname"]) #Rohit

print("----------------------------------------------------------")