

def burbleSort():

    numbers = [65,28,200,12,35,43,37,85,99,1,65,3,76,59,62,5]
    # lenght of array
    n = len(numbers)
    # We want to loop through the list may times
    # We getting the length of the list 
    for j in range(n):
        for i in range(n-1):
            if numbers[i] > numbers[i+1]:
                temp = numbers[i+1]
                numbers[i+1] =numbers[i]
                numbers[i] = temp
    print(numbers)


def burbleSort1():

    numbers = [65,28,200,12,35,43,37,85,99,1,65,3,76,59,62,5]
    # lenght of array
    n = len(numbers)
    x = 0
    # Compare outer loop to inner loop
    for i in range(0,n):
        x += 1
        for j in range(i+1,n):
            if numbers[i] > numbers[j]:
                temp = numbers[j]
                numbers[j] =numbers[i]
                numbers[i] = temp
    print(numbers)
    print(x)
            
        

burbleSort1()