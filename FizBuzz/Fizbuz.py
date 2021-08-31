

def FizzBuzz(number):

    if (number % 3 == 0) & (number % 5 == 0) :
        print("Fizz Buzz")
    if number % 3 == 0 :
        print("Fizz")
    if number % 5 == 0 :
        print("Buzz")
    else:
        print("Not divisible by 3 or 5")


FizzBuzz(30)
    