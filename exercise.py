"""Exercise.py"""

# Question 1
def exercise(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

# Question 2
def printAll(list1):
    for item in list1:
        print(item)

# Question 3
def printMax(a,b):
    if (a > b):
        print(a, 'is the maximum')
    elif (b == a):
        print(a, 'is equal to', b)
    else:
        print(b, 'is the maximum') 
        """hello is the maximum here because 
            it didn't fulfill the if conditions 
            and went to else"""

# Answers for the Question 3 part 2:
# printMax(3, 4) -> 4 is the maximum
# printMax(3, 3) -> 3 is equal to 3
# printMax(4, 4) -> 4 is equal to 4
# printMax(3) -> TypeError: printMax() missing 1 required positional argument: 'b'
# printMax(3, 4, 5) -> TypeError: printMax() takes 2 positional arguments but 3 were given
# printMax('charlie', 'hello') -> hello is the maximum

# Question 4
def say(message, times = 2):
        print(message * times) # prints the message 'times' times
        #why? because of the multiplication operator *

say('Hello') # prints 'Hello' 2 times
say('Hello', 5) # prints 'Hello' 5 times

""" The Reason why the output of say('Hello') is different from say('Hello', 5)
    is because in the function definition, the parameter 'times' has a default value of 2.
    When we call say('Hello'), we only provide one argument, which is assigned to the 'message' parameter.
    Since we did not provide a value for 'times', it takes the default value of 2."""

# Question 5
def func(a, b-5, c-10):
    print('a is', a, ', b is', b, 'and c is', c)
#this function will give error because of the invalid syntax in the parameter list

func(3, 7) #a is 3 , b is 7 and c is 10
func(25, c=24) #This works because we are using a keyword argument to specify the value of 'c' but not b.
func(c = 50, a = 100) #This works because we are using keyword arguments to specify the values of 'c' and 'a'.

#Question 6
def func(a,b, names):
    a += 10
    b += 20
    names[0] = 17
    names[1] = 18
    return a, b

x,y = 10,30
fruits = ['apple', 'orange', 'banana']
num1, num2 = func(x,y,fruits)
print(num1, num2) #20 50
for fruit in fruits:
    print(fruit) #17 18 banana


#As fruits is a list which is mutable, the changes made to it inside the function are reflected outside the function as well.
#x and y are integers which are immutable, so the changes made to them inside the function do not affect their values outside the function.
#So, the output will be: 20 50, and the list fruits will be modified to ['17', '18', 'banana'].

# Question 7
# To decide the leap year
def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Question 8
# Part a)
def printWelcome():
    return 'Welcome: '
def messager(func,str1):
    print(func() + str1)

messager(printWelcome, 'Python') # Welcome: Python

# Part b)
def increment(x):
    return x + 100
def double(x):
    return x * 2
def getBonus(func, salary):
    bonus = 1000;
    if func(salary) > 5000:
        return func(salary) + bonus*2
    else:
        return func(salary) + bonus
    
print(getBonus(increment, 3000))    # 4100 (3000 + 100 + 1000)
print(getBonus(double, 3000))       # 7000 (3000 * 2 + 1000)
print(getBonus(increment, 6000))    # 7100 (6000 + 100 + 1000*2)
print(getBonus(double, 6000))       # 13000 (6000 * 2 + 1000*2)
