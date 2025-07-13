my_str=input("Enter a string:")

for i in my_str[::-1]:          #option1
    print(i,end="")


for i in reversed(range(len(my_str))):  #option2
    print(my_str[i],end="")