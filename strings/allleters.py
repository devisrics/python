import string

value=input("Enter a String:")
is_panagram=True

for char in string.ascii_lowercase:
    if char not in value.lower():
        is_panagram=False

print(is_panagram)