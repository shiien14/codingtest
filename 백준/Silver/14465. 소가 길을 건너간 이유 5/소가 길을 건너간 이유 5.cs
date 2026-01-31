class Program
{
    static void Main(string[] args)
    {
        string[] input = Console.ReadLine().Split();
        int n = int.Parse(input[0]);
        int k = int.Parse(input[1]);
        int b = int.Parse(input[2]);
        int[] nums = new int[n];
        int[] prefix_sum = new int[n+1];

        for (int i = 0; i < n; i++)
        {
            nums[i] = 1;
        }

        for (int i = 0; i < b; i++)
        {
            int num = int.Parse(Console.ReadLine())-1;
            nums[num] = 0;
        }

        prefix_sum[0] = 0;
        for (int i = 0; i < n; i++)
        {
            prefix_sum[i+1] = prefix_sum[i] + nums[i];
        }

        int m = k;

        for (int i = 0; i <=n-k; i++)
        {
            if (k - (prefix_sum[i + k] - prefix_sum[i]) < m)
            {
                m = k - (prefix_sum[i + k] - prefix_sum[i]);
            }

        }

        Console.WriteLine(m);
    }
}