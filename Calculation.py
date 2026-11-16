from Addition import Addition


class Calculation(Addition):

    def __init__(self, a, b):
        super().__init__(a,b)

    def showCalculate(self):
        display = self.add()
        return display

obj = Calculation(10,10)
print("{}{}".format("Addition of two numbers: ", obj.showCalculate()))
