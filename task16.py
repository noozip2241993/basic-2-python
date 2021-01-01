import math
def permutation(n,r):
    return  math.factorial(n)/(math.factorial(n-r))
print(permutation(3,3))