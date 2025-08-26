t = int(input())
while t>0:
    n = int(input())
    arr = list(map(int,input().split()))
    mina = 10000000000000
    maxa = -1
    for i in range(n):
        if arr[i]>maxa:
            maxa=arr[i]
        if arr[i]<mina:
            mina = arr[i]

    print(mina,maxa)