r'''
Task Description:
Develop a simple average calculator program. The program requirement is as follows:
1. Allow users to run your program with three input arguments by passing three 
   values to the program: a, b and c.

2. Your program will read the three arguments and calculate the average value.

3. After user inputs all the numbers, if the input numbers are invalid, you need to 
   present an error message "Your input is invalid!". Otherwise, you need to print 
   out the average value. The output average value requires to have 2 precisions (round up). 
   For instance, if the value is 23.456, it should print 23.46. If it is 23, 
   it should print 23.00.
   
NOTE: You have to strictly follow the input and output format.

Running example:
Assume your program is named as AverageCalculator.py. Example output is as follows:

C:\INF1002\Lab1\AverageCalculator>python AverageCalculator.py 3 4 5
Average:4.00

C:\INF1002\Lab1\AverageCalculator>python AverageCalculator.py 60 39 92
Average:63.67

C:\INF1002\Lab1\AverageCalculator>python AverageCalculator.py abc 10 20
Your input is invalid!
'''
import sys
# You can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.

# Request the user to input the three numbers
# Get the three arguments from command line
arg1 = sys.argv[1]  # First number
arg2 = sys.argv[2]  # Second number  
arg3 = sys.argv[3]  # Third number

def AverageCalculator():
    try:
        # Convert arguments to float
        num1 = float(arg1)
        num2 = float(arg2)
        num3 = float(arg3)

        # Calculate average
        average = (num1 + num2 + num3) / 3

        # Print average with 2 decimal places
        print(f"Average:{average:.2f}")
    except ValueError:
        print("Your input is invalid!")

if __name__=='__main__':
      AverageCalculator()
      
