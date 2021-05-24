
def findMaximumValue():
    array = [7,2,98,1,666,56,9]
    temp = array[0]
    for j in array:
        if j > temp :
            temp = j
        
    print(temp)
findMaximumValue()

 