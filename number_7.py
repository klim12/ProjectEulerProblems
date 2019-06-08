i = 0 #
n = 1 #prime number
def prime(x):     #prime number checker
    ans=1
    if x == 2:
        ans=1
    elif x == 1 or x % 2 == 0:
        ans=0
    else:
        i = 3
        while i <= x**0.5:
            if x % i == 0:
                ans=0
            i+=1
    return ans


while i != 10001:
    if prime(n) == 1:
        i += 1
    n += 1
print(n-1)




