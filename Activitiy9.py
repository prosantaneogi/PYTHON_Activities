list1=[1,2,3,4,5,5,6,6,7,7]
list2=[11,12,13,14,15,16]
list3=[]
for x in list1:
    if x%2==0:
        list3.append(x)
    else:
        pass

for y in list2:
    if y%2==0:
        pass
    else:
        list3.append(y)

print(list3)


