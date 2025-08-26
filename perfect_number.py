t = int(input())
sum = 0
while (t>0):
    n = int(input())
    for i in range(1,n):
        if n%i == 0:
            sum+=i
    if sum == n:
        print("perfect number")
    else:
        print("not perfect ")
    t=t-1