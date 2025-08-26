t = int(input())
while(t>0):
    n = int(input())
    arr = list(map(int,input().split()))
    freq = [0]*40
    for i in range(n):
        freq[arr[i]]+=1
    
    for j in range(40):
        if(freq[j]>0):
            print(j,":",freq[j])

    t=t-1