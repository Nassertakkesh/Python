Basic - Print all integers from 0 to 150.
# for i in range(151):
#     print(i)

# # Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for m in range(5,1001,5):
    print(m)


# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for y in range(1,100):
    if y%5== 0 and  y%10 != 0:
        print("coding")
    elif y%10 == 0:
        print("coding dojo") 
    else:
        print(y)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0
for y in range(1,500001):
    if y%2== 1:
        print(y)
        sum +=y
 
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for z in range(2018,0,-4):
    print(z)

Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 10
mult = 3
jake = 'test'
for b in range(lowNum,highNum):
    if b%mult == 0:
        print(b)