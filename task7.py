def unique(n1):
    list = []
    for i in n1:
        if i not in list:
            list.append(i)
    return list
print(unique([1,1,2,3,2,4,5,7]))