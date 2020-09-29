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
48 is frue.
"""

#! python3
n = int(input("Input number\n"))
s = n / 6
e = n / 8
N = str(n)
if s % 1 == 0 and e % 1 != 0:
    print(N , "is frue")
else:
    print(N , "is not frue")