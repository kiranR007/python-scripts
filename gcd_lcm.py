def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# Test
a, b = 12, 18
print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))
