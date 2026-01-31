class Program
{
    static void Main(string[] args)
    {
        string[] input = Console.ReadLine().Split();
        int n = int.Parse(input[0]);
        int x = int.Parse(input[1]);
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

        int m = 0;

        for(int i = 0; i <= n-x; i++)
        {
            if(prefix_sum[i+x] - prefix_sum[i] > m)
            {
                m = prefix_sum[i+x] - prefix_sum[i];
                cnt = 0;
            }
            if(prefix_sum[i+x] - prefix_sum[i] == m)
            {
                cnt += 1;
            }
        }

        if (m == 0)
        {
            Console.WriteLine("SAD");
        }
        else
        {
            Console.WriteLine(m);
            Console.WriteLine(cnt);
        }
    }
}