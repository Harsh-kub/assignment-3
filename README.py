# assignment-3
# task 1

n=int(input("Enter a number: "))
def fact(n):
    if n<2:
        return 1
    else:
        return n*fact(n-1)

r=fact(n)
print("The factorial of", n ,"is:", r)

# task 2

import math
n=float(input("Enter a number: "))
s=math.sqrt(n)
l=math.log(n)
si=math.sin(n)
print("square root:",s)
print("logarithm:",l)
print("sin:",si)

