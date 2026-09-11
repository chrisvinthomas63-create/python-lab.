def fibonacci_recursive(n):
    """Calculate the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def main():
    print("=== Fibonacci Series Using Recursion ===")
    try:
        terms = int(input("Enter the number of terms to display: "))
        if terms <= 0:
            print("Please enter a positive integer.")
            return
        
        print(f"\nFibonacci series up to {terms} terms:")
        for i in range(terms):
            print(fibonacci_recursive(i), end=" ")
        print()
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()  