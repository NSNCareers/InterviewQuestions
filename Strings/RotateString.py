

def RotateString(stringToRotate):
    originalSring = stringToRotate
    L = len(stringToRotate)
    reverseString = ""
    while L > 0:
        reverseString += originalSring[L-1]
        L -= 1
    print(f'Reverse string : {reverseString}')
    print(f'Original string : {originalSring}')

RotateString("Elvis")
            

            
    