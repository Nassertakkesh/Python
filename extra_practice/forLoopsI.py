# Basic - Print all integers from 0 to 150.


def basic():
    for i in range(0,151,1):
        print(i)
basic()
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
def mult5():
    for i in range(5,1001,5):
        print(i)
mult5()
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

def counting():
    for i in range(1,100):
        if i %10 == 0:
            print('Coding Dojo')
        elif i %5 == 0:
            print('Coding')  
        else:
            print(i)
counting()

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def sucker():
    sum = 0
    for i in range(0,500001,1):
        if i %2 == 1:
            sum += i
    return sum
sucker()
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

def fours():
    for i in range(2018,0,-4):
        print(i)
fours()

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def flexible():
    lowNum = 2
    highNum=9
    mult =3
    for i in range(lowNum,highNum+1,1):
        if i %mult == 0:
            print (i)
    
flexible()


