my_str=input("Enter a String:").lower()
new_dict={}

for char in my_str:
    if char.isalpha():
        if char in new_dict:
            new_dict[char] +=1
        else:
            new_dict[char]=1

print(new_dict)