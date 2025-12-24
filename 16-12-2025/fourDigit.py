def display(n):
    temp = n
    first = n % 100
    n = n // 100
    second = n % 100

    if(first == second):
        print(temp)
    
for i in range(1000,10000):
    display(i)