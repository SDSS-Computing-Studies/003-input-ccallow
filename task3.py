#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

a= input("what is a? ")
b= input("What is b? ")
c= input("What is c? ")
a=float(a)
b=float(b)
c=float(c)
solution = (c-b)/a
x= float(solution)
print(x)
