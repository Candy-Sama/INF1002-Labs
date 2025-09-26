r'''
Task Description:
     In this task you will write a program that reads two sequences of numbers. 
     The first sequence of numbers is called candidate, and the second sequence of 
     numbers is called pattern. Your program will determine if the pa􀆩ern is found 
     entirely in the candidate. To be considered found entirely, all elements of 
     pattern must be in the candidate sequence a consecu􀆟ve positions. You must 
     output the number of found patterns, or 0 if the pattern is not found in 
     the candidate.

     Input: 
          Allow the users to input two sequences, the first sequence is the candidate, 
          and the second sequence is the pattern.
     Output: 
          The number of pattern sequence appearing in the candidate sequence (in ONE line).

     Running Example:
     C:\INF1002\Lab3\PatternSearching>python SearchPattern.py 1,2,3,1,2 1,2
     Pattern appears 2 time!
'''

import sys
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def SearchPattern():
     candidate = []
     pattern = []
     for arg in sys.argv[1:3]: #get the first two input arguments
          if len(candidate) == 0: #if candidate is empty, it means we are reading the first argument
               candidate = [int(num) for num in arg.split(',')] #split the string by comma and convert each element to integer
          else:
               pattern = [int(num) for num in arg.split(',')] #split the string by comma and convert each element to integer
     count = 0
     pattern_length = len(pattern) #get the length of the pattern
     for i in range(len(candidate) - pattern_length + 1): #iterate through the candidate
          if candidate[i:i+pattern_length] == pattern: #check if the sublist of candidate matches the pattern
               count += 1 #if it matches, increment the count
     if count == 0:
          print("Pattern not found!")
     elif count == 1:
          print("Pattern appears 1 time!")
     else:
          print(f"Pattern appears {count} time!")

if __name__=='__main__':
     SearchPattern()
      
