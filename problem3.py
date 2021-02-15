#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

a = float(input("an integer "))
b = float(input("an integer "))
c = float(input("an integer "))

if a > b and a > c:
    small1 = b
    small2 = c
    big = a
elif b > a and b > c:
    small1 = a
    small2 = c
    big = b
elif c > a and c > b:
    small1 = a
    small2 = b
    big = c

if (small1**2 + small2**2) == big**2:
    print(str(int(small1)) + "," + str(int(small2)) + "," + str(int(big)) + " form a Pythagorean triple")
else:
    print(str(int(small1)) + "," + str(int(small2)) + "," + str(int(big)) + " do not form a Pythagorean triple")