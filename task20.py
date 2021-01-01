import itertools
def flattening_list(list1):
    return list(itertools.chain(*list1))
list3 = ([1,2,3],[4,3,1],[2,13,1])
print(flattening_list(list3))