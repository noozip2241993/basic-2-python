numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
numbers = [x for (i,x) in enumerate(numbers) if i not in (0,2,5,10,12)]
print(numbers)