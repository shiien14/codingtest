using System.Text;
class Program
{
    static void Main(string[] args)
    {

        const int MAX = 1000000;
        bool[] isNotPrime = new bool[MAX + 1];
        isNotPrime[0] = isNotPrime[1] = true;

        for (int i = 2; i * i <= MAX; i++)
        {
            if (!isNotPrime[i])
            {
                for (int j = i * i; j <= MAX; j += i)
                {
                    isNotPrime[j] = true;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        while (true)
        {
            string st = Console.ReadLine();
            if (st == null) break;
            int n = int.Parse(st);
            if (n == 0) break;
            bool found = false;
            for(int i = 3; i <= n / 2; i += 2)
            {
                if (!isNotPrime[i] && !isNotPrime[n - i])
                {
                    sb.AppendLine($"{n} = {i} + {n - i}");
                    found = true;
                    break;
                }
            }
            if (!found)
                sb.AppendLine("Goldbach's conjecture is wrong.");
        }

        Console.WriteLine(sb.ToString());
    }
}