from excercise7 import NumberCalculator


class ChildBasicCal(NumberCalculator):

    def __init__(self):
        NumberCalculator.__init__(self, 1,2,3,4 )
        # self.firstNum = num1
        # self.secondNum = num2
        # self.thirdNum = num3
        # self.fourthNum = num4

    def addCalculate(self):
        return self.firstNum + self.secondNum + self.thirdNum + self.fourthNum + self.additionOfNumbers()

obj1 = ChildBasicCal()
print(obj1.addCalculate())
