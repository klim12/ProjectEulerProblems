s=2      #sum contains a2=2
a1=1
a2=2
new=a1+a2  # new Fibonacci element
while new<4000000:
    if new%2==0:
        s=s + new
    a1=a2
    a2=new
    new=a2+a1

print(s)