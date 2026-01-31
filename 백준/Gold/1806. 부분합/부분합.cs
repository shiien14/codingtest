class Program
{
    static void Main(string[] args)
    {
        string[] input = Console.ReadLine().Split();
        int n = int.Parse(input[0]);
        int s = int.Parse(input[1]);

        input = Console.ReadLine().Split();
        int[] nums = new int[n];

        for (int i = 0; i < n; i++)
        {
            nums[i] = int.Parse(input[i]);
        }

        int start = 0, end = 0, sum = 0;
        int minLength = int.MaxValue;

        while (true)
        {
            if (sum >= s)
            {
                minLength = Math.Min(minLength, end - start);
                sum -= nums[start++];
            }
            else if (end == n)
            {
                break;
            }
            else
            {
                sum += nums[end++];
            }
        }

        Console.WriteLine(minLength ==int.MaxValue ? 0 : minLength);
    }
}