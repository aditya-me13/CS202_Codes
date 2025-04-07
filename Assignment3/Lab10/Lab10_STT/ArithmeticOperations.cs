using System;
using System.Transactions;

class ArithmeticOperations
{
    public static void Run()
    {
        Console.Write("Enter first number: ");
        int num1 = Convert.ToInt32(Console.ReadLine());

        Console.Write("Enter second number: ");
        int num2  = Convert.ToInt32(Console.ReadLine());
        
        int sum = num1 + num2;
        int diff = num1 - num2;
        int product = num1 * num2;
        double quotient = (num2 != 0) ? (double) num1/num2 : double.NaN;

        Console.WriteLine($"Sum: {sum}, Diff: {diff}, Product: {product}, Quotient: {quotient}");

        if (sum % 2 == 0)
            Console.WriteLine("The sum is even.");
        else
            Console.WriteLine("The sum is odd");
    }
}