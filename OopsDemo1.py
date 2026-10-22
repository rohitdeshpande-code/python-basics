#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object


class Calculator:
    num = 100 #class variables

    #default constructor, a and b instance variables pass in constructor
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")


    def getData(self):
        print("I am now executing as a method in class")

    # instance variables always declare with self, for class variables option like either self. or classname.(Calculator)
    def summation(self):
        return self.firstNumber + self.secondNumber + self.num

obj = Calculator(2, 3) #Syntax to create object in python
obj.getData()
#print(obj.num)
print(obj.summation())
# I am called automatically when object is created
# I am now executing as a method in class
# 105

obj1 = Calculator(5, 5) #Syntax to create object in python
obj1.getData()
#print(obj.num)
print(obj1.summation())
# I am called automatically when object is created
# I am now executing as a method in class
# 110