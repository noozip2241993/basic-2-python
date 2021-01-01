def smallest_number(n1):
    smallest_number = 100000000000
    for i in n1:
        if i < smallest_number:
            smallest_number = i
    return smallest_number
print(smallest_number([1,2,3,4,24,22,-99]))
