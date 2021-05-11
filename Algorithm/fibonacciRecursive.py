

def Fibonacci(number):

    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return Fibonacci(number-1) + Fibonacci(number-2)

def Iterrate(number):

    for i in range(number):
        print(Fibonacci(i))
        
    
        
Iterrate(10)