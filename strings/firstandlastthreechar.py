value=input("Enter a string")
if (len(value)<6):
    print("")
else:
    firlas=value[:3] + value[len(value)-3:]     #[:3]->[0,1,2]   #[9-3:]->[6,7,8]
    print(firlas)