
def bubbleSort(list):
    for i in range(0,len(list),+2):
        temp = list[i]
        list[i] = list[i+1]
        list[i+1] = temp
    return list
bubbleSort([5,6,7,6,87,86,8,8,7,64,5,25,46547326,24,656,56,7,6853,45,234,245,43])




def bubbleSort2(list):
    max = len(list)
    for i in range(0,max,+1):
        if i > (i+1):
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
    

    return list

bubbleSort2([5,6,7,25,46547326,24,656,55,234,245,43])