

def DuplicateInterger(array):
    L = len(array)
    N = []
    for j in array:
        if j in N:
            print(j)
            break
        else:
            N.append(j)
            
DuplicateInterger([6,10,28,98,10])
    