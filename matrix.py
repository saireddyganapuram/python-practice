m = 4
n = 4
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
target = 12
low = 0
high = (m*n) - 1
while(low <= high):
    mid = (low + high) // 2
    i = mid // n
    j = mid % n
    if(a[i][j] == target):
        print("True")
        break
    elif(a[i][j] < target):
        low = mid + 1
    else:
        high = mid - 1
print("False")
