def bubbleSort(newlist=[]):
    for i in range(0,len(newlist)-1):
        for j in range(0,len(newlist)-1): 
            if newlist[j] > newlist[j+1]:
                newlist[j], newlist[j+1] = newlist[j+1], newlist[j]
    return newlist

bubbleSort([5,6,7,11,34,4,56,87,1,2343,4,657686878,3,3,5,7,8,9,0,0,6,2,1])



def selectionSort(newlist = []):
    min = 0
    count = 0
    for i in range(0,len(newlist)-1):
        for j in range(i,len(newlist)-1):
            if min > newlist[j]: 
                min = newlist[j]
                count = j
            newlist[count], newlist[i] = newlist[i],newlist[count]
    return newlist
        
selectionSort([5,6,7,11,34,4,56,87,1,2343,4,657686878,3,3,5,7,8,9,0,0,6,2,1])

        