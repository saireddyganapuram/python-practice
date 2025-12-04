def pattern(n):
    for i in range(n):
        for j in range(n):
            if(i == j):
                print(i+1,end=" ")
            elif((i + j) == (n - 1)):
                print(i+1,end=" ")
            else:
                print(" ",end=" ")
        print()


pattern(6)