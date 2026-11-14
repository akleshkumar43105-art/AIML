def duplicate_elements(a):
    new_list = []
    for i in range(len(a)):
        if a[i] not in new_list:
            new_list.append(a[i])
    print(new_list)    
a = [1,2,2,3,4,5,5,6,7]
duplicate_elements(a)

