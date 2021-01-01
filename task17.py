def difference_two_lists(l1,l2):
    return list(list(set(l1)-set(l2)) + list(set(l2)-set(l1)))
list1 = [1,2,3,4,5,6,7,8,5,724]
list2= [1,1,2,3,4,5,6,7,90,12,34,1]
print(difference_two_lists(list1,list2))