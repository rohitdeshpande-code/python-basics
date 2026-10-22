
with open("file1.txt", "r") as reader:
    content = reader.readlines()
    for i in content:
        print(i)