# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(list1=[]):
    for i in range(0,len(list1)):
        if list1[i]>0:
            list1[i] = 'big'
    return list1

biggie_size([-1, 3, 5, -5])

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(list2 = []):
    sum = 0
    for i in range(0,len(list2)):
        if list2[i]>0:
            sum += 1
    list2[len(list2)-1] = sum          
    return list2
    
count_positives([1,6,-4,-2,-7,-2])


# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(list3 = []):
    sum = 0
    for i in range(0,len(list3)):
            sum += list3[i]      
    return sum

sum_total([1,2,3,4])

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def average(list4 = []):
    sum = 0
    avg = float
    for i in range(0,len(list4)):
            sum += list4[i] 
    avg = sum/(len(list4))
    print(sum)
    print(avg)
    return avg

average([1,2,3,4])

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(list5 = []):
    length = len(list5)
    return length

length([])


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(list6 = []):
    min = 0
    for i in range(0,len(list6)):
         if list6[i]<min:
            min = list6[i]
         
    return min

minimum([37,2,1,-9])

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(list7 = []):
    max = 0
    for i in range(0,len(list7)):
         if list7[i]>max:
            max = list7[i]
         
    return max

maximum([37,2,1,-9])

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(list8 = []):
    max = 0
    min =0
    sum = 0 
    length =0
    for i in range(0,len(list8)):
         if list8[i]>max:
            max = list8[i]      
         elif list8[i]<min:
            min = list8[i]

         sum += list8[i]
         avg = sum/(len(list8))
         length = len(list8)

    print(sum)
    print(avg)
    print(min)  
    print(max)
    print(length)
    myList = ["sum", sum,avg,min,max,length]
    return myList

ultimate_analysis([37,2,1,-9])
#i dont know how to return both key value pairs

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(list9 = []):
    temp = 0
    for i in range(0,len(list9)/2, 1):
         temp = list9[(len(list9)-1)-i]
         list9[(len(list9)-1)-i]= list9[i]
         list9[i] = temp
         
    return list9

reverse_list([37,2,1,-9])
