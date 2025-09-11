import math
def non_prime(arr):
    n = len(arr)
    res =[]
    for i in range(n):
        for j in range(i+1,n):
            if math.gcd(arr[i],arr[j])>1:
                res.append((arr[i],arr[j]))
    return res
nums = [6, 8, 15, 25, 17]
print(non_prime(nums))
