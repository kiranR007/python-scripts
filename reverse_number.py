number = int(input("Enter the number: "))
res = 0
while number:
    rem = number%10
    number = number//10
    res = res*10+rem
print(res)



    