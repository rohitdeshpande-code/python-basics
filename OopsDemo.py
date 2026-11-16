
class Calculator:
    num = 100

    def __init__(self):
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as a method in class")

obj = Calculator() #Syntax to create object in python
obj.getData() #I am called automatically when object is created
                #I am now executing as a method in class
print(obj.num) #100

print("-----------------------------------------------")

class DemoClass:

    def __init__(self, a,b):
        self.a = a
        self.b = b
        print("Inside constructor")

    def method1(self):
        print("Inside method1")

    def add(self):
        print(self.a + self.b)


demo = DemoClass(2,2)
#demo.method1()
demo.add()