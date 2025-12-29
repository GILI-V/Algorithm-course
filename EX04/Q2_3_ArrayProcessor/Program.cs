using System;

namespace Q2_3_ArrayProcessor
{
    public class ArrayProcessor
    {
        public delegate void UnaryAction(double a);

        public static void ProcessArray(double[] array, UnaryAction processor)
        {
            foreach (double value in array)
                processor(value);
        }
    }

    public class SumCalculator
    {
        public double Sum { get; private set; }
        public void AddToSum(double a) => Sum += a;
    }

    public class MaxCalculator
    {
        public double Max { get; private set; } = double.MinValue;
        public void CheckMax(double a)
        {
            if (a > Max) Max = a;
        }
    }

    class Program
    {
        static void Main()
        {
            double[] arr = { 3.5, 7.2, 1.4, 9.8 };

            var sumCalc = new SumCalculator();
            var maxCalc = new MaxCalculator();

            ArrayProcessor.ProcessArray(arr, sumCalc.AddToSum);
            ArrayProcessor.ProcessArray(arr, maxCalc.CheckMax);

            Console.WriteLine($"Sum: {sumCalc.Sum}");
            Console.WriteLine($"Max: {maxCalc.Max}");
        }
    }
}
