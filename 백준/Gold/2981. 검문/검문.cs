class Program
{
    static void Main(string[] args)
    {

        int n = int.Parse(Console.ReadLine());
        int[] nums = new int[n];

        for(int i = 0; i < n; i++)
        {
            nums[i]= int.Parse(Console.ReadLine());
        }

        Array.Sort(nums);

        int m = nums[1] - nums[0];
        for (int i = 0; i < n-1; i++)
        {
            m = Gcd(m, nums[i + 1] - nums[i]);
        }

        for(int i = 2; i <= m; i++)
        {
            if (m % i == 0) Console.Write(i+" ");
        }
    }

    private static int Gcd(int x, int y)
    {
        return (x % y == 0 ? y : Gcd(y, x % y));
    }
}