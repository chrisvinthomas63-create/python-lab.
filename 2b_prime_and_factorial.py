# Program 2(b): Check Prime Number and Calculate Factorial
n = int(input("Enter a number: "))

# Prime number check
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Not a Prime Number")

# Factorial
if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print("Factorial:", fact)
