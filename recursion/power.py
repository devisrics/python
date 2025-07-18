base=int(input("Enter a number"))
power=int(input("Enter a number"))

def powerrr(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        return a * powerrr(a,b-1)

print(powerrr(base,power))