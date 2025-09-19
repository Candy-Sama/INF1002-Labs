r'''
Task Description:
In this task, you are assigned to develop one program to help users calculate 
different information based a series of user provided numbers (integers). 
Detailed requirement is provided as follows: 

Input: A series of numbers 
Output: (Your output should be in one line)
	. The summation of the even numbers and summation of the odd numbers in 
       the input list 
	. The difference between the biggest and smallest numbers in the input list
	. The count of even numbers and odd numbers in the input list
	. The "centered" average of the list of integers. The centered average can be 
       calculated as the mean average of the values, after removing the largest and 
       smallest values in the array. If there are multiple copies of the smallest 
       value, ignore all but keep just one copy, and likewise for the largest value. 
       For instance, [12,2,8,7,100] -> 9; [2,2,8,11,100] -> 7

To have a better understanding of the loops, please try to implement 
two programs: one uses "for" and another uses "while" loop.

Running Examples:

C:\INF1002\Lab2\EvenOddCalculator> python EvenOddCalculator.py 12,2,8,7,100
The sum of all even numbers is 122, the sum of all odd numbers is 7, the difference between the biggest and smallest number is 98, the total number of even numbers is 4, the total number of odd numbers is 1, the centered average is 9.

C:\INF1002\Lab2\EvenOddCalculator> python EvenOddCalculator.py 1,2,abcd,8,11,200,301
Please enter valid integers.
'''
import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def EvenOddCalculator():
     #find the input string
     input_string = sys.argv[1];

     #split the string into a list of strings
     input_list = input_string.split(','); #split the string by comma (the comma is not included in the list)

     #convert the list of strings into a list of integers
     try:
          input_list = [int(x) for x in input_list]; #convert each string in the list to an integer
     except ValueError:
          print("Please enter valid integers.");
          return

     #initialize variables
     even_sum = 0;
     odd_sum = 0;
     even_count = 0;
     odd_count = 0;
     max_num = input_list[0];
     min_num = input_list[0];

     #calculate the sum and count of even and odd numbers, and find the max and min numbers
     for num in input_list: #for each number in the list
          if num % 2 == 0: #if the number is even
               even_sum += num; #add it to the even sum
               even_count += 1; #increment the even count
          else: #if the number is odd
               odd_sum += num; #add it to the odd sum
               odd_count += 1; #increment the odd count

          if num > max_num: #if the number is greater than the current max, update max
               max_num = num;
          if num < min_num: #if the number is less than the current min, update min
               min_num = num;

     #calculate the difference between the biggest and smallest numbers
     diff = max_num - min_num;

     #calculate the centered average
     centered_list = input_list.copy(); #make a copy of the input list
     centered_list.remove(max_num); #remove one instance of the max number
     centered_list.remove(min_num); #remove one instance of the min number
     centered_average = sum(centered_list) / len(centered_list) #calculate the average

     #print the results
     print(f"The sum of all even numbers is {even_sum}, the sum of all odd numbers is {odd_sum}, the difference between the biggest and smallest number is {diff}, the total number of even numbers is {even_count}, the total number of odd numbers is {odd_count}, the centered average is {int(centered_average)}.");

if __name__=='__main__':
      EvenOddCalculator();
      
