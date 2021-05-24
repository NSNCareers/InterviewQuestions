
def findMaximumValue():
    array = [7,2,98,1,56,9]
    for j in range(len(array)):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
            
        
    print(array[-1])


findMaximumValue()

    