
str = "RahulShettyAcademy.com"
str1 = "Consulting Firm"
str2 = 3
str3 = "RahulShetty"

print(str[1]) #a

print(str[0:5]) #if you want substring in python - Rahul

print(str+ " " + str1) #RahulShettyAcademy.com Consulting Firm -> "Concatination"

print("{} {}".format(str, str2))

print(str3 in str) #substring check

var = str.split(".")
print(var) # ['RahulShettyAcademy', 'com']
print(var[0]) # RahulShettyAcademy

#strip is nothing like trim, however in python trim is not a keyword
str4 = " Great "
print(str4.strip())  # "Great"
print(str4.lstrip()) # "Great "
print(str4.rstrip()) # " Great"

print("---------------------------------------------------------------")

string1 = "Rohit.Deshpande@cybage.com"
string2 = 100
string3 = "Rohit"

print("{}{}{}".format("String1 and String2 is: ", string1, string2))
print(string1[1])
print(string1[-1])
print(string1[1:3])

print(string1 + "------------------------" + string3)

print(string3 in string1)

var1 = string1.split("@")
var2 = var1[0].split(".")
print(var2[1])

string4 = " Cybage "
print("Stripped string: " + string4.strip())
print("Left Stripped string: " + string4.lstrip())
print("Right Stripped string: " + string4.rstrip())

