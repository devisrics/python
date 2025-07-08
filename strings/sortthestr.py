value=input("Enter a String:")

spt=value.split(" ")
new_str=""

for word in spt:
    sor="".join(sorted(word.lower()))
    new_str +=sor + " "

new_str.rstrip()
print(new_str)