#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
n = float(input("Input number\n"))
N = str(n).strip()
if n > 0:
    print(N + " is a positive integer.")
elif n == 0:
    print("That is zero")
elif n < 0:
    print(N + " is not a positive integer.")