# rotat a list to right by one position
l=[1,1,8,5,9,4,5,6,8,4]
l=l[-1:]+l[:-1]
print(l)