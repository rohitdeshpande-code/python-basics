
file = open("test.txt")
#Read all the contents of file

#Read n number of characters by passing parameter
#print(file.read())
#print(file.read(4))

#Read one single line at a time
# print(file.readline())
# print(file.readline())

#Print line by line using readline method

# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

#values = ["apple", "bat", "cat", "dog", "elephant"]
for line in file.readlines():  # all the line contents are store in list so we can iterate it using for loop
    print(line)
    # elephant
    # dog
    # cat
    # bat
    # apple

file.close()