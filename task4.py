import math
def largest_number(n1):
    result = -1000000000000
    for i in n1:
        if i >= result:
            result = i
    return result
print(largest_number([1,2,3,4,3,1,776,5555]))