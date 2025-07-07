value=input("Enter a string:")
i=int(input("enter a value:"))
if(i>len(value)):
    print("i out of range")
elif(len(value)== 0):               #for empty string comapre with 0
    print("empty string")
else:
    print(value[i])