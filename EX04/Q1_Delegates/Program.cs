using System;

namespace Q1_Delegates
{
    public delegate double BinaryOperation(double a, double b);

    class Program
    {
        static double Add(double a, double b) => a + b;
        static double Subtract(double a, double b) => a - b;
        static double Multiply(double a, double b) => a * b;

        public static double ApplyOperation(BinaryOperation bOp, double a, double b)
        {
            return bOp(a, b);
        }

        static void Main(string[] args)
        {
            Console.WriteLine(ApplyOperation(Add, 3, 4));
            Console.WriteLine(ApplyOperation(Subtract, 10, 5));
            Console.WriteLine(ApplyOperation(Multiply, 2, 6));
        }
    }
}
