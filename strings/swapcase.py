value=input("Enter a String:")

spt=value.split(" ")
new_s=""

for word in spt:
    res="".join(reversed(word))
    swap_cs=res.swapcase()
    new_s +=swap_cs + " "

new_s.rstrip()
print(new_s)