# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(newlist = []):
    for i in range(0,len(newlist)):
        if newlist[i] > 0:
            newlist[i] = "big"
    return newlist

biggie_size([-1, 3, 5, -5])
    

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it


def count_positives(newlist = []):
    count = 0
    for i in range(0,len(newlist)):
        if newlist[i]>0:
            count+=1
    newlist[len(newlist)-1] = count
    return newlist

count_positives([1,6,-4,-2,-7,-2])



# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(newlist=[]):
    sum = 0
    for i in newlist:
        sum += i
    return sum
sum_total([1,2,3,4])    

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5


def average(newlist=[]):
    sum = 0
    length = len(newlist)
    for i in newlist:
        sum += i
    avg =sum / length
    return avg

average([1,2,3,4])


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(newlist=[]):
    length = len(newlist)

    return length

length([37,2,1,-9])


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(newlist=[]):
    min = 0
    for i in newlist:
        if i < min:
            min = i 
    return min

minimum([37,2,1,-9])

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(newlist=[]):
    max = 0
    for i in newlist:
        if i > max:
            max = i 
    return max

maximum([37,2,1,-9])


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(newlist = []):
    dict ={}
    max = 0
    min =0
    sum= 0
    length =len(newlist)

    for i in newlist:
        if i > max:
            max = i
        if i < min:
            min = i 
        sum += i  
    avg =  sum/length
    
    dict['maximum'] = max
    dict['minimum'] = min
    dict['average'] = avg
    dict['sumTotal'] = sum

    return dict

ultimate_analysis([37,2,1,-9])


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(newlist = []):
    for i in range(0,int(len(newlist)/2),1 ):
        newlist[i],newlist[len(newlist)-1-i] = newlist[len(newlist)-1-i], newlist[i]
    return newlist
reverse_list([37,2,1,-9])