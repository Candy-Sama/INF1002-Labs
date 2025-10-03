import myMath

"""Warm up exercise for lab 4"""

def factorial(n):
    if n < 0:
        raise ValueError("Negative values are not allowed")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) #makes a little loop that calls itself
print(factorial(4)) #should print 24
print(factorial(0)) #should print 1
print(factorial(5)) #should print 120
print(factorial(10)) #should print 3628800

def fac_iterative(n):
    if n < 0:
        raise ValueError("Negative values are not allowed")
    result = 1
    for i in range(2, n + 1): #starts at 2 because multiplying by 1 does nothing
        result *= i
    return result

help(myMath) #prints out the docstring for the myMath module