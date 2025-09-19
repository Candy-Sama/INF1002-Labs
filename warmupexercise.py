List1 = ['abc', 'bcd', ['123', 567], 789];
Tuple1 = ('23', 15, 8, 100);
Dic = {'A01':'xiaoming', 'A02':['mie', 3]};

print(List1[1])        # → 'bcd' (element at index 1)
print(List1[2])        # → ['123', 567] (element at index 2 - a nested list)

range(10)       # → range(0, 10) (represents numbers 0-9)
range(2, 10, 2) # → range(2, 10, 2) (represents 2,4,6,8)

try:
    print(List1[2][2])     # → ERROR! List1[2] is ['123', 567], but index 2 doesn't exist (only 0,1)
except IndexError:
    print("ERROR! List1[2] is ['123', 567], but index 2 doesn't exist (only 0,1)");

print(List1[4])        # → ERROR! Index 4 doesn't exist (List1 has indices 0,1,2,3)
print(List1[-3])       # → 'bcd' (3rd from the end)
print(List1[2:])       # → [['123', 567], 789] (from index 2 to end)

print(Tuple1[0])       # → '23' (first element)
print(Tuple1[1:])      # → (15, 8, 100) (from index 1 to end)
print(Tuple1[:2])      # → ('23', 15) (from start to index 2, exclusive)
try:
    Tuple1[2] = 23  # → ERROR! Tuples are immutable (can't change values)
except TypeError:
    print("ERROR! Tuples are immutable (can't change values)")

h_letters = [ letter for letter in 'human' ]  
print( h_letters)  
number_list = [ x for x in range(20) if x % 2 == 0]  
print(number_list)  
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]  
print(num_list)  
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]  
print(obj) 

# Question 2 - Create one tuple and one list to store five of your favourite fruits (e.g. pear, apple, strawberry, banana, orange ) separately 
fruit_list = ['pear', 'apple', 'strawberry', 'banana', 'orange']
fruit_tuple = ('pear', 'apple', 'strawberry', 'banana', 'orange')

# Question 3 - Print both the list and the tuple to the console
print(fruit_list)
print(fruit_tuple)

#Question 4 - Update one of the items from the list or tuple, e.g. change the ‘apple’ into ‘papaya’
fruit_list[1] = 'papaya'
print(fruit_list)

# Question 5 - Delete one of the items from the list or tuple, e.g. delete pear
del fruit_list[0]
print(fruit_list)

# Question 6 - Sort all the remaining fruits and print the ordered fruits out using for and while loops
fruit_list.sort()
print("Using for loop:")
for fruit in fruit_list:
    print(fruit)

print("Using while loop:")
i = 0
while i < len(fruit_list):
    print(fruit_list[i])
    i += 1

# Question 7 - Use the list comprehension to generate the lists according to below requirements:  
# Find all the numbers from 1-1000 that are divisible by 7  
divisible_by_7 = [x for x in range(1, 1001) if x % 7 == 0]
print(divisible_by_7)

# Find all the numbers from 1-1000 that have a 3 in them  
has_3 = [x for x in range(1, 1001) if '3' in str(x)]
print(has_3)

# Count the number of spaces in a string
test_string = "Count the number of spaces in this string"
space_count = sum(1 for char in test_string if char == ' ')
print(space_count)

# Create one dictionary to store 12 months and its corresponding number of days. Use for and 
# while loops to print out all the months and all the number of days.
months_days = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

# Using for loop
for month, days in months_days.items():
    print(f"{month}: {days} days")

# Using while loop
months = list(months_days.keys())
i = 0
while i < len(months):
    month = months[i]
    print(f"{month}: {months_days[month]} days")
    i += 1

""" 
You are going to design one program to check the popular words in a document. Please 
download the Lab2_testData.txt from LMS. Note that the given data has a fixed scheme 
where each line is one long string and each string contains multiple keywords that are 
separated by “,”. You need to write one program to read this file and calculate the top 5 
most frequent keywords and write out these 5 keywords in the end of the file. The following 
are some hints which may help you design this program.  
• String has a cool function that you can use to split a string separated by a ‘,’. For 
instance, given one string str1 = “apple, pear, peach”, to get all the keywords in str1, 
str1.split(‘,’) will return a list of keywords. You can use list1=str1.split(‘,’) to obtain all the 
keywords and put them into one list.  
• To get the top 5 most frequent keywords, you need to extract all the keywords first and 
figure out one way to calculate the frequency of each keyword. Then select the top 5 
keywords.  
 
Input: The given text file “Lab2_testData.txt”  
Output: Print out the top 5 keywords both on the screen and to a new txt file “top_5.txt”. 
"""

from collections import Counter
with open('Lab2_testData.txt', 'r') as file: # Open the file
    lines = file.readlines() # Read all lines
all_keywords = []

for line in lines: # Read each line
    keywords = line.strip().split(',')
    all_keywords.extend(keywords)

keyword_counts = Counter(all_keywords)
top_5_keywords = keyword_counts.most_common(5)

with open('top_5.txt', 'w') as output_file:
    for keyword, count in top_5_keywords:
        output_file.write(f"{keyword}: {count}\n")

for keyword, count in top_5_keywords:
    print(f"{keyword}: {count}")
# Examples illustrating tuple immutability vs list mutability
example_list = [1, 2, 3]
example_tuple = (1, 2, 3)

# Modifying the list
example_list[0] = 10
print("Modified list:", example_list)

# Attempting to modify the tuple (will raise an error)
try:
    example_tuple[0] = 10
except TypeError as e:
    print("Error:", e)