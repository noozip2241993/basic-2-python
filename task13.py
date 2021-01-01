positions = ['Husband','Wife','Father','Mother','Brother']
names = ['Khang','Trang','Ninh','Tho','Thinh']
list=[]
for position,name in zip(positions,names):
    list += position,name
print(list)
list = [x for (i,x) in enumerate(list) if i not in (0,2,4,6,8)]
list = [x.upper() for x in reversed(list)]
print(list)