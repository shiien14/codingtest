using System;
using System.Collections.Generic;
class Program
{
    static void Main()
    {
        int S = int.Parse(Console.ReadLine());
        int[,] dist = new int[1001, 1001];

        for (int i = 0; i <= 1000; i++)
            for (int j = 0; j <= 1000; j++)
                dist[i, j] = -1;

        Queue<(int screen, int clipboard)> q = new Queue<(int, int)>();

        q.Enqueue((1, 0));
        dist[1, 0] = 0;

        while (q.Count > 0)
        {
            var curr = q.Dequeue();
            int s = curr.screen;
            int c = curr.clipboard;


            if (dist[s, s] == -1)
            {
                dist[s, s] = dist[s, c] + 1;
                q.Enqueue((s, s));
            }

            if (c > 0 && s + c <= 1000 && dist[s + c, c] == -1)
            {
                dist[s + c, c] = dist[s, c] + 1;
                q.Enqueue((s + c, c));
            }

            if (s - 1 >= 0 && dist[s - 1, c] == -1)
            {
                dist[s - 1, c] = dist[s, c] + 1;
                q.Enqueue((s - 1, c));
            }
        }

        int ans = int.MaxValue;
        for (int i = 0; i <= S; i++)
        {
            if (dist[S, i] != -1) ans = Math.Min(ans, dist[S, i]);
        }
        Console.WriteLine(ans);
    }
}