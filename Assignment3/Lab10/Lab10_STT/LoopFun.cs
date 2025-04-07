using System;

class LoopFun
{

    static void PrintNumbers(int n)
    {
        for (int i = 0; i < n; i++)
            Console.WriteLine(i);
    }

    static int Factorial(int n)
    {
        if (n == 1)
            return 1;
        return n * Factorial(n - 1);
    }
    public static void Run()
    {
        //Console.WriteLine("Hello, World!");
        //ArithmeticOperations.Run();

        Console.WriteLine("Numbers from 1 to 10:");
        PrintNumbers(10);

        Console.Write("Enter a number for factorial: ");
        int num = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine($"Factorial of {num} is {Factorial(num)}");

        string input;
        do
        {
            Console.Write("Type 'exit' to stop: ");
            input = Console.ReadLine();
        } while (input.ToLower() != "exit");
    }
}