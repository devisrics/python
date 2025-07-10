my_str=input("Enter a String:").lower()
vowels=['a','e','i','o','u']

for char in my_str:
    if len(my_str)==0:
        print("String is Empty")
    elif char.isalpha():
        if char in vowels:
            print(f"{char} is a vowel")
        else:
            print(f"{char} is a consonant")
    else:
        print(f"{char} is not a letter")