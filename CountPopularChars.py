r'''
Task Description:
In this task, you are going to design one program to check the popular characters
in a given string. You need to write one program to calculate the top 5 most 
frequent characters. The following are some hints that may help you design this program. 
	. String has a cool function that you can use to return a copy of the string 
     in which all case-based characters have been lowercased. 
	. To get the top 5 most frequent characters after sorting them, you need to 
     extract all the characters first and figure out one way to calculate the frequency 
     of each character. Then select the top 5 characters. 
	. The output must in the descending order of character frequency. If there are 
     characters with the same frequency, they must be printed in ascending ASCII order.
	. Print out the top 5 characters and their counts in the screen. (Your output should be in one line)

Running Examples:
C:\INF1002\Lab2\CountPopularChars>python CountPopularChars.py sdsERwweYxcxeewHJesddsdskjjkjrFGe21DS2145o9003gDDS
d:7,s:7,e:6,j:4,w:3
'''
import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def CountPopularChars():
     #find the input string
     input_string = sys.argv[1];
     #convert the string to lower case
     input_string = input_string.lower();
     #create a dictionary to store the frequency of each character
     char_freq = {};

     #iterate through the string and count the frequency of each character
     for char in input_string: #for each character in the string
          if char in char_freq: #if the character is already in the dictionary, increment its count
               char_freq[char] += 1; #increment the count
          else:
               char_freq[char] = 1; #if the character is not in the dictionary, add it with count 1

     #sort the dictionary by frequency and then by ASCII value
     sorted_char_freq = sorted(char_freq.items(), key=lambda x: (-x[1], ord(x[0])));

     #get the top 5 characters
     top_5_chars = sorted_char_freq[:5];

     #print the top 5 characters and their counts
     output = ','.join([f"{char}:{count}" for char, count in top_5_chars]);
     print(output);

if __name__=='__main__':
      CountPopularChars();

