"""
This script demonstrates recursion, loops, and conditionals in Python.
It includes functions to compute Fibonacci numbers, print a star pattern,
compute the factorial of a number, and check if a number is prime.
"""

def fibonacci(n):
    """Recursive function to return the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def print_pattern(rows):
    """Function to print a star pattern."""
    for i in range(1, rows + 1):
        print("*" * i)

def factorial(n):
    """Recursive function to calculate the factorial of a number."""
    if n in (0, 1):
        return 1
    return n * factorial(n-1)

def is_prime(num):
    """Function to check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
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
