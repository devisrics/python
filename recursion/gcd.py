a=int(input("Enter first nuber:"))
b=int(input("Enter second number:"))

def find_gcd(a,b):
    if b==0:
        return a
    else:
        return find_gcd(b,a%b)
    
print(find_gcd(a,b))