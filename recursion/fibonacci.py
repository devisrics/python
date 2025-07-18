num=int(input("Enter a number:"))

def fibonacci(s):
    if s==0 or s==1:
        return s
    else:
        return fibonacci(s-1)+fibonacci(s-2)
    
print(fibonacci(num))