def display(elem,val):
    n = len(elem)
    s = 0
    for i in range(n):
        s += elem[i]
    if(val > s):
        print(val)

arr = [1,10,3,1,20,40]
n = len(arr)
for i in range(1,n):
    display(arr[:i],arr[i])

