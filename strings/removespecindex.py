value=input("Enter a String:")
n=int(input("Enter a value:"))

if(len(value)==0):
    print("")
elif(n>=len(value)):
    print("Index out of range")
else:
    str =""
    for i in range(len(value)):
        if(i!=n):
            str +=value[i]
print(str)