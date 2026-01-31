class Program
{
    static void Main(string[] args)
    {
        string[] input = Console.ReadLine().Split();
        int n = int.Parse(input[0]);
        int m = int.Parse(input[1]);
        input = Console.ReadLine().Split();
        int[] nums = new int[n];
        int[] prefix_sum = new int[n+1];
        int cnt = 0;

        for (int i = 0; i < n; i++)
        {
            nums[i] = int.Parse(input[i]);
        }

        prefix_sum[0] = 0;
        for (int i = 0; i < n; i++)
        {
            prefix_sum[i+1] = prefix_sum[i] + nums[i];
        }

        for(int i = 0; i < n; i++)
        {
            for(int j = i+1; j <= n; j++)
            {
                if(prefix_sum[j] - prefix_sum[i] == m)
                {
                    cnt += 1;
                }
            }
        }

        Console.WriteLine(cnt);
    }
}