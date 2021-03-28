# Recursion = A way of solving a problem by having a function calling itself.

# performing the same operation multiple times with different inputs.
# in every step, we try smaller input to make the problem smaller.
# Base condition is needed to stop the recursion or infinite loop will occur.

# Example 1:
def openRussianDoll(doll):
    if doll == 1:
        print("All Dolls are opened")
    else:
        openRussianDoll(doll - 1)
"""
Why we need recursion?

Recursive thinking is important in programming and it helps to break down big problems into smaller ones
and easier to use.

When to choose recursion?
If you can define the problem into similar sub problems
Design an algorithm to compute nth
Write code to list n...
Implement a method to compute all.
Practice

Prominent use of recursion in data structures like trees and graphs.
It is used in many algorithms.
"""

"""
How recursion works?

conditions: 
1. A method calls itself
2. Exit from infinite loop

def recursionMethod(parameters):
    if exit from condition statement:
        return some value
    else:
        recursionMethod(modified parameters)
        
"""
# Example 2:
def firstMethod():
    secondMethod()
    print("I am the first method")

def secondMethod():
    thirdMethod()
    print("I am the second method")

def thirdMethod():
    forthMethod()
    print("I am the third method")

def forthMethod():
    print("I am the forth method")

firstMethod()
secondMethod()
thirdMethod()
forthMethod()

# Stack memory collects firstMethod, secondMethod and thirdMethod
# and hence it remembers to call it after the fourthMethod

def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursiveMethod(n - 1)
        print(n)

recursiveMethod(4)

# Recursive vs Iterative Solutions

# Recursive
def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2

# Iterative
def powerOfTwoIt(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i += 1
    return power

print(powerOfTwo(5))
print(powerOfTwoIt(5))

"""
When to use recursion?

When we can easily breakdown a problem into similar subproblem
When we are fine with extra space and time
When we need a quick working solution instead of efficient one 
When we traverse a tree
When we use memoization in recursion
"""
"""
When not to use recursion?

If time and space complexity matter for us
Takes more memory, not suitable for phone or embedded systems
Recursion can be slow
"""

# How to write recursion in 3 steps?

# Factorial:
# Step 1 = Recursive case - The flow
# import sys
# sys.setrecursionlimit(1)
def factorial(n):
    print(n)
    return n * factorial(n-1)

# factorial(5)

# Step 2 = Base Case - The stopping criteria
def factorial2(n):
    if n in [0,1]:
        return 1
    else:
        return n * factorial2(n-1)

# print(factorial2(10))

# Step 3 = Unintentional case - the constant
def factorial3(n):
    assert n >= 0 and int(n) == n, "The number must be positive integer"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial3(n-1)

print(factorial3(-10))