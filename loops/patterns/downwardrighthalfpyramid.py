num=int(input("Enter a number:"))

for i in range(num):
    for j in range(i):                      #increasing spaces downwar
        print(" ",end="")
    for j in range(i,num):                    #decreasing stars upwards
        print("*",end="")
    print()