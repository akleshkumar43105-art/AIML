def find_numbers(a):
    greatest = a[0]
    smallest = a[0]
    for i in a:
        if i > greatest:
            greatest = i

        if i < smallest:
            smallest = i
    print("greatest number:",greatest)
    print("smallest number:",smallest)          

 

a = [23,64,73,94,54,12,34,56,78,90]
find_numbers(a)              