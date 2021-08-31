

from typing_extensions import Concatenate


def RotateString(stringToRotate):
    originalSring = stringToRotate
    L = len(stringToRotate)
    reverseString = ""
    while L > 0:
        reverseString += originalSring[L-1]
        L -= 1
    print(f'Reverse string : {reverseString}')
    print(f'Original string : {originalSring}')


def RotateString1(stringToRotate):
    originalSring = stringToRotate
    L = len(stringToRotate)
    reverseString = ""
    while L > 0:
        #reverseString += originalSring[L-1]
        reverseString + originalSring[L-1]
        L -= 1
    print(f'Reverse string : {reverseString}')
    print(f'Original string : {originalSring}')


RotateString("Elvis")
            

            
    