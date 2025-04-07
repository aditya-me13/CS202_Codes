using System;
using System.Linq.Expressions;
using System.Transactions;

class ExceptionHandling
{
    public static void Run()
    {
        try
        {
            Console.Write("Enter first number: ");
            int num1 = Convert.ToInt32(Console.ReadLine());

            Console.Write("Enter second number: ");
            int num2 = Convert.ToInt32(Console.ReadLine());

            int sum = num1 + num2;
            int diff = num1 - num2;
            int product = num1 * num2;
            double quotient = num1 / num2;

            Console.WriteLine($"Sum: {sum}, Diff: {diff}, Product: {product}, Quotient: {quotient}");
        }
        catch(DivideByZeroException){
            Console.WriteLine("Error: Division by zero is not allowed.");
        }
        catch(FormatException){
            Console.WriteLine("Error: Invalid input.");
        }
    }
}