
class BasicCalculator:

    def __init__(self, num1, num2):
        self.firstNumber = num1
        self.secondNumber = num2

    def addition(self):
        return self.firstNumber + self.secondNumber

    def subtraction(self):
        return self.firstNumber - self.secondNumber

    def multiplication(self):
        return self.firstNumber * self.secondNumber

    def division(self):
        return self.firstNumber / self.secondNumber

obj = BasicCalculator(10, 5)
print("{} {} {} {} {} {}".format("Addition:", obj.firstNumber, "+", obj.secondNumber, "=", obj.addition()))

print("{} {} {} {} {} {}".format("Subtraction:", obj.firstNumber, "-", obj.secondNumber, "=", obj.subtraction()))

print("{} {} {} {} {} {}".format("Multiplication:", obj.firstNumber, "*", obj.secondNumber, "=", obj.multiplication()))

print("{} {} {} {} {} {}".format("Division:", obj.firstNumber, "/", obj.secondNumber, "=", obj.division()))