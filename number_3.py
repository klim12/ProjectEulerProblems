n = 600851475143
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
i = 1
ans = 0
while i <= n**0.5:
    if n%i == 0 and prime(i) == 1:
        if i>ans:
            ans=i
    i+=1
for j in range(1, i):
    if n % j == 0 and prime(n//j) == 1:
        if n//j>ans:
            ans=n//j
print(ans)







