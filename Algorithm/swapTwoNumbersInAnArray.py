
# We have to remove the index we want to swarp and store in a temp variable

def swarpTwoNumbers(lastIndex,firstIndex):

    arrayOfNumbers = [76,23,21,34,54,1,4,22,60]
    temp = arrayOfNumbers[lastIndex]
    arrayOfNumbers[lastIndex] = arrayOfNumbers[firstIndex]
    arrayOfNumbers[firstIndex] = temp
    print(arrayOfNumbers)

swarpTwoNumbers(7,2)

