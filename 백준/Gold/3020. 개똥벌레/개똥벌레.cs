class Program
{
    static void Main(string[] args)
    {
        string[] input = Console.ReadLine().Split();
        int n = int.Parse(input[0]);
        int h = int.Parse(input[1]);

        int[] bottom = new int[h + 1];
        int[] top = new int[h + 1];

        for(int i = 0; i < n; i++)
        {
            int stone = int.Parse(Console.ReadLine());
            if (i % 2 == 0) bottom[stone]++;
            else top[stone]++;
        }

        for(int i = h-1; i >= 1; i--)
        {
            bottom[i] += bottom[i + 1];
            top[i] += top[i + 1];
        }

        int m = n;
        int count = 0;

        for (int i = 1; i <= h; i++)
        {
            int cur = bottom[i] + top[h - i + 1];

            if (cur < m)
            {
                m = cur;
                count = 1;
            }
            else if(cur == m)
            {
                count++;
            }
        }
        Console.WriteLine($"{m} {count}");
    }
}