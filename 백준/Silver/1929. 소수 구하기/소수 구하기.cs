class Program
{
    static void Main(string[] args)
    {
        string[] str = Console.ReadLine().Split();
        int n = int.Parse(str[0]);
        int m = int.Parse(str[1]);

        bool[] isPrime = new bool[m + 1];
        isPrime[0] = isPrime[1] = false;

        for (int i = 2; i <= m; i++)
        {
            isPrime[i] = true;
        }

        for (int i = 2; i * i <= m; i++)
        {
            if (isPrime[i])
            {
                for (int j = i * i; j <= m; j += i)
                {
                    isPrime[j] = false;
                }
            }
        }

        for (int i = n; i <= m; i++)
        {
            if (isPrime[i]) Console.WriteLine(i);
        }

    }
}