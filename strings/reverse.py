value=input("Enter a string")
if (len(value) == 0):
    print("")
else:
    rv="".join(reversed(value))       #option1  reversed->["o","l","l","e","h"]
    print(rv)


#option2
rv=value[::-1]