# The Fibonacci Sequence is the series of numbers:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...0,1,1,2,3,5,8,13,21,34,...
# The series starts with 00 and 11 as the first two numbers in the series. 
# The next number in the series is found by summing the two numbers before it.

def fib(number):
       counter = 0
       first = 0
       second = 1
       temp = 0

       while counter <= number:
           print(first)
           temp = first + second
           first = second
           second = temp
           counter += 1


# Driver Code
fib(20)

# In the above implementation, The code prints the first value on each iteration of the loop. 
# Each iteration calculates the next value by summing the previous two values and then updates 
# the values of first and second.