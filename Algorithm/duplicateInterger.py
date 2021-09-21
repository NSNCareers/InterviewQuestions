

def DuplicateInterger(array):
    l = len(array)
    N = []
    for j in array:
        if j not in N:
            N.append(j)
        else:
            print(j)
            
DuplicateInterger([6,10,28,98,10,6])
    