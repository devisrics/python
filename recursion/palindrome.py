val=input("Enter a string:")

def string(value):
    value=value.lower()

    if len(value)<=0:
        return True
    elif value[0] != value[-1]:
        return False
    else:
        return string(value[1:-1])
    
print(string(val))