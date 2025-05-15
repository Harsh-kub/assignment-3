# ASSIGNMENT 3
# TASK 1

n=int(input("Enter a number: "))
def fact(n):
    if n<2:
        return 1
    else:
        return n*fact(n-1)

r=fact(n)
print("The factorial of", n ,"is:", r)
