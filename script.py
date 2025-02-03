def fibonacci(n):
    """Recursive function to return the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_pattern(rows):
    """Function to print a star pattern."""
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()  # Move to the next line after each row

def factorial(n):
    """Recursive function to calculate factorial."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(n):
    """Function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    # Fibonacci Series
    print("Fibonacci Series:")
    for i in range(10):
        print(f"Fibonacci({i}): {fibonacci(i)}")
    
    # Star Pattern
    print("\nStar Pattern:")
    print_pattern(5)

    # Factorial
    print("\nFactorial:")
    number = 5
    print(f"Factorial of {number}: {factorial(number)}")

    # Prime Check
    print("\nPrime Check:")
    numbers = [3, 4, 5, 10, 11]
    for num in numbers:
        print(f"Is {num} prime? {is_prime(num)}")

if __name__ == "__main__":
    main()
