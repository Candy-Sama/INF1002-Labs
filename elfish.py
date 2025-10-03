r'''
Task Description: 
     A word is considered elfish if it contains the letters: e, l and f in it, in any 
     order. For instance, we would say that the following words are elfish: tasteful, 
     whiteleaf, unfriendly and waffles, because they each contain those letters. Use 
     the recursive function to implement this. Write one program to call your recursive 
     function and tell the user whether the input word is one elfish or not. 
     
     HINT: You can recursively reduce both the elfish letters and input word. 
     The sample executions are provided as follows:

Note: 
     Your output should be in ONE line

Running example: 
     C:\INF1002\Lab4\elfish> python elfish.py waffles
     waffles is one elfish word!

     C:\INF1002\Lab4\elfish> python elfish.py instance
     instance is not an elfish word!
'''

import sys

# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.

def is_elfish_word(word):
     elfish_letters = {'e', 'l', 'f'}
     def helper(w, letters): #helper function to do the recursion
         if not letters: #if letters is empty, all letters found
             return True
         if not w: #if word is empty but letters still remain
             return False
         if w[0] in letters: #if the first letter of the word is in the set of letters
             letters.remove(w[0])
         return helper(w[1:], letters) #call helper on the rest of the word
     return helper(word.lower(), elfish_letters) #convert word to lowercase to make it case insensitive

def elfish():
     input_word = sys.argv[1]
     if is_elfish_word(input_word):
         print(f"{input_word} is one elfish word!")
     else:
         print(f"{input_word} is not an elfish word!")

if __name__=='__main__':
     elfish()
      
