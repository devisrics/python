num=int(input("Enter a number:"))

def fact(s):
    if s==0 or s==1:
        return 1
    else:
        return s*fact(s-1)

print(fact(num))
