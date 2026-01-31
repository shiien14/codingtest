class Program
{
    static int n, s, result;
    static int[] nums;

    static void Main(string[] args)
    {
        string[] str = Console.ReadLine().Split();
        n = int.Parse(str[0]);
        s = int.Parse(str[1]);

        nums = new int[n];
        str = Console.ReadLine().Split();
        for (int i = 0; i < n; i++)
            nums[i] = int.Parse(str[i]);

        result = 0;

        Backtrack(0, 0);

        if (s == 0) result--;

        Console.WriteLine(result);
    }

    private static void Backtrack(int index, int total)
    {
        if (index == n)
        {
            if (total == s)
            {
                result++;
            }
            return;
        }

        Backtrack(index + 1, total + nums[index]);
        Backtrack(index + 1, total);
    }
}