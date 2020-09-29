#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
n1 = int(input("Input number\n"))
n2 = int(input("Input number\n"))
if n1 > n2:
    a = n1
    b = n2
if n2 > n1:
    a = n2
    b = n1
if a % b == 0:
    print(b , "is a factor of" , a)
else:
    (b , "is not a factor of" , a)