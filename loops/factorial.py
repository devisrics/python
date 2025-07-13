num = int(input("Enter a number: "))
fact = 1

if (num == 0) or (num == 1):
    print(f"Factorial of {num} is: 1")
else:
    for i in range(2, num + 1):
        fact *= i
    print(f"Factorial of {num} is: {fact}")
