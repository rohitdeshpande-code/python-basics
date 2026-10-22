from OopsDemo1 import Calculator


class ChildImpl(Calculator):
    num2 = 200

#    def __init__(self):
#       Calculator.__init__(self, 10, 10) #420 => 200+100+120

    def __init__(self, a, b):
      Calculator.__init__(self, 10, 10) #420 => 200+100+120

#    def __init__(self, a, b):
#       Calculator.__init__(self, a, b) #402 => 200+100+102

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()

#obj = ChildImpl()
obj = ChildImpl(1, 1)
print(obj.getCompleteData())

# I am called automatically when object is created
# I am now executing as a method in class
# 105 (3+2+100)

# I am called automatically when object is created
# I am now executing as a method in class
# 110 (5+5+100)

# I am called automatically when object is created
# 420 (200+100+10+10)


#    def __init__(self, a, b):
#       Calculator.__init__(self, a, b)


# I am called automatically when object is created
# I am now executing as a method in class
# 105

# I am called automatically when object is created
# I am now executing as a method in class
# 110

# I am called automatically when object is created
# 402