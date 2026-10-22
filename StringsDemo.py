
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
