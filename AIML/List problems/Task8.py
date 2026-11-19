# seperate even and odd numbers into two different lists
l=[1,1,8,5,9,4,5,6,8,4]
odd=[]
even=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)