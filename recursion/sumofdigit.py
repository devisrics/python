num=int(input("Enter a number:"))

def sd(sum):
    if sum==0:
        return 0
    else:
        return (sum % 10) +sd(sum // 10)

print(sd(num))
