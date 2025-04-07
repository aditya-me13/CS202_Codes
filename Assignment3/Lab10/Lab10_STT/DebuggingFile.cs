using System;

// Main class to demonstrate different debugging techniques
class DebuggingFile
{
    public static void Main()
    {
        Console.WriteLine("Program Execution Started...");

        try
        {
            // Instantiate MathHelper class
            MathHelper helper = new MathHelper();

            int a = 12, b = 8;

            int result = helper.CalculateSum(a, b); // Place breakpoint here
            Console.WriteLine($"Addition Result: {result}");

            int factOfNumber = helper.ComputeFactorial(4); // Debug recursion
            Console.WriteLine($"Factorial of 4: {factOfNumber}");

            int[] data = { 2, 4, 6, 8 };
            Console.WriteLine($"Total of Array Elements: {helper.CalculateArrayTotal(data)}"); // Debug loop

            Console.WriteLine("Please enter a divisor for 50:");
            int inputDivisor = Convert.ToInt32(Console.ReadLine());

            double divisionOutput = helper.PerformSafeDivision(50, inputDivisor);
            Console.WriteLine($"50 divided by {inputDivisor} equals {divisionOutput}");
        }
        catch (FormatException)
        {
            Console.WriteLine("Input error: Please provide a valid integer.");
        }
        catch (DivideByZeroException)
        {
            Console.WriteLine("Error: Division by zero detected.");
        }
    }
}

// Helper class with different methods to debug
class MathHelper
{
    // Adds two numbers
    public int CalculateSum(int x, int y)
    {
        return x + y;
    }

    // Recursive factorial calculation
    public int ComputeFactorial(int n)
    {
        if (n <= 1) return 1;
        return n * ComputeFactorial(n - 1); // Recursive call
    }

    // Calculates sum of array elements
    public int CalculateArrayTotal(int[] arr)
    {
        int total = 0;
        for (int i = 0; i < arr.Length; i++)
        {
            total += arr[i];
        }
        return total;
    }

    // Safe division with error check
    public double PerformSafeDivision(int numerator, int denominator)
    {
        if (denominator == 0)
            throw new DivideByZeroException();
        return numerator / (double)denominator;
    }
}
