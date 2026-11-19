# count how many times a particular element occurs in a list without using count function
l=[1,1,4,8,5,9,4,5,6,8,4]
c=0
number=4
for i in l:
    if number==i:
        c+=1
print(number,"occurs",c,"times")