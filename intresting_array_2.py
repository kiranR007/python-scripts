def main():
    t=int(input())
    while (t!=0):
        n = int(input())
        arr = list(map(int,input().split()))
        k = int(input())
        i = 0
        j = n-1
        flag = 0
        while(i<j):
            sum = arr[i]+arr[j]
            if sum == k:
                flag = 1
                print(i,j)
                break
            elif sum>k:
                j-=1
            else:
                i+=1
        if flag == 0:
            print(-1)
        t-=1




if __name__=='__main__':
    main()