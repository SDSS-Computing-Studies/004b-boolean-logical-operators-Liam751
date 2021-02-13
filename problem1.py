"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue
"""

#! python3

a = float(input("a number "))
divide6 = False
divide8 = False

if (a % 6) == 0:
    divide6 = True

if (a % 8) == 0:
    divide8 = True


if (divide6 == True) and (divide8 == False):
    print(str(a) + " is frue")
else:
    print(str(a) + " is not frue")