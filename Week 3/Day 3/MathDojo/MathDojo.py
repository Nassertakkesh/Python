
class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        total =0
        total +=num
        print(total)
        return self

    def subtract(self, num, *nums):
        total1 =0
        total1 +=num
        print(total1)
        return self

md = MathDojo()
x = md.add(2).add(2,10,1).subtract(1)
print(x)	

# create an instance:

# to test:
# should print 5
# run each of the methods a few more times and check the result!