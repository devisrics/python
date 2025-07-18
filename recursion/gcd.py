a=int(input("Enter first nuber:"))
b=int(input("Enter second number:"))

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)