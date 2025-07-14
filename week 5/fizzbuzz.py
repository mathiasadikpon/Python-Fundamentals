""" """

def fizzbuzz(num):
    """"Print 'Fizz' if num is divisible by 3, print 'Buzz' if num is divisible by 5, and print 'FizzBuzz' if num is divisible by both."""

    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

""" driver code """
fizzbuzz(0)