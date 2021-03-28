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
