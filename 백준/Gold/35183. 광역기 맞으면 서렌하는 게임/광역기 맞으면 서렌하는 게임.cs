class Program
{
    static int n;
    static int[] L, R;

    static void Main(string[] args)
    {
        n = int.Parse(Console.ReadLine());
        L = new int[n];
        R = new int[n];
        for (int i = 0; i < n; i++)
        {
            string[] str = Console.ReadLine().Split();
            L[i] = int.Parse(str[0]);
            R[i] = int.Parse(str[1]);
        }

        bool[,,] dp = new bool[1001, 2005, 2];
        int offset = 1000;

        for (int p = -1000; p <= 1000; p++)
        {
            if (p >= L[0] && p <= R[0]) dp[0, p + offset, 0] = true;
            dp[0, p + offset, 1] = true;
        }

        for (int t = 0; t < n - 1; t++)
        {
            for (int p = 0; p <= 2000; p++)
            {
                if (!dp[t, p, 0] && !dp[t, p, 1]) continue;

                for (int move = -1; move <= 1; move++)
                {
                    int nextP = p + move;
                    if (nextP < 0 || nextP > 2000) continue;

                    if (dp[t, p, 1] && (nextP - offset >= L[t + 1] && nextP - offset <= R[t + 1]))
                        dp[t + 1, nextP, 1] = true;

                    if (dp[t, p, 0])
                    {
                        if (nextP - offset >= L[t + 1] && nextP - offset <= R[t + 1])
                            dp[t + 1, nextP, 0] = true;
                        dp[t + 1, nextP, 1] = true;
                    }
                }
            }
        }
        bool canWin = false;

        for (int p = 0; p <= 2000; p++)
        {
            if (dp[n - 1, p, 0] || dp[n - 1, p, 1])
            {
                canWin = true;
                break;
            }
        }

        if (canWin) Console.WriteLine("World Champion");
        else Console.WriteLine("Surrender");

    }
}