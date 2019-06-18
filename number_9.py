# a<b<c , a^2 + b^2 = c^2  a+b+c=1000   a*b*c=?
#  a^2=(c-b)*(c+b)  ==> c+b = a^2/(c-b)
#  a + a^2/(c-b) =1000
# c-b = a^2/(1000-a)
# c+b = 1000 - a
# c = a^2/(2000 -2a) +500 -0.5a
# b=500 -0.5a -a^2/(2000-2a)
for i in range(1, 499):
     a = i
     b = 500 - 0.5*a - a**2/(2000 - 2*a)
     c = 500 - 0.5*a + a**2/(2000 - 2*a)
     if (a < b) and (b < c) and (b.is_integer() == True) and (c.is_integer() == True):
         print(a*b*c)
         break


