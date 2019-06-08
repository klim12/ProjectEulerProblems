sqrsum = 0
sumsqr = 0
for i in range(1, 101):
    sumsqr+=i**2

for i in range(1, 101):
    sqrsum+=i
print(sqrsum**2-sumsqr)