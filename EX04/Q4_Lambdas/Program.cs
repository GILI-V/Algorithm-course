using System;

namespace Q4_Lambdas
{
    class Program
    {
        static void Main()
        {
            double[] arr = { 4.2, 6.1, 2.9, 8.3 };

            double sum = 0;
            double max = double.MinValue;

            foreach (double value in arr)
            {
                ((Action<double>)(x => sum += x))(value);
                ((Action<double>)(x => { if (x > max) max = x; }))(value);
            }

            Console.WriteLine($"Sum: {sum}");
            Console.WriteLine($"Max: {max}");
        }
    }
}
