using System;
using System.Collections.Generic;

namespace Q5_OperationTable
{
    class OperationTable<T>
    {
        public delegate T OpFunc(T x, T y);

        private List<T> rows;
        private List<T> cols;
        private OpFunc op;

        public OperationTable(List<T> rowValues, List<T> colValues, OpFunc operation)
        {
            rows = rowValues;
            cols = colValues;
            op = operation;
        }

        public void Print()
        {
            foreach (var r in rows)
            {
                foreach (var c in cols)
                    Console.Write($"{op(r, c)}\t");
                Console.WriteLine();
            }
        }
    }

    class Program
    {
        static void Main()
        {
            var values = new List<double> { 1, 0.5, 0.25 };
            var table = new OperationTable<double>(values, values, (x, y) => x + y);
            table.Print();
        }
    }
}
