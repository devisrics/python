num=int(input("Enter a number:"))

if (num==0) or (num==1):
    print(f"{num} is not a prime mumber")
else:
    for i in range(2,num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:  
        print(f"{num} is a prime number")
