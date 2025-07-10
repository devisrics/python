import math                                       

a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))

discriminant=(b**2)-(4*a*c)

if discriminant<0:
    print("Complex Roots")
elif discriminant==0:
    r=-b/2*a
    print(r)
else:
    r1=( -b + math.sqrt(discriminant))/(2*a)
    r2=( -b + math.sqrt(discriminant))/(2*a)
    print(r1,r2)