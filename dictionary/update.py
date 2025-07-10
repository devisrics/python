my_dict={"a":4,"b":3,"c":6}
key=input("Enter a key: ")
value=int(input("Enter a value: "))


if key not in my_dict:
    my_dict[key]=value

print(my_dict)