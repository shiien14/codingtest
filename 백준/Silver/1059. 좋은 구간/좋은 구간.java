import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int L = Integer.parseInt(br.readLine());
        int[] S = new int[L];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < L; i++) {
            S[i] = Integer.parseInt(st.nextToken());
        }

        int n = Integer.parseInt(br.readLine());
        Arrays.sort(S);

        int left = 0;
        int right = 0;

        for (int i = 0; i < L; i++) {
            if (S[i] == n) {
                System.out.println(0);
                return;
            }
        }

        for (int i = 0; i < L; i++) {
            if (S[i] < n) left = S[i];
            else {
                right = S[i];
                break;
            }
        }

        if (left == 0) left = 0;
        if (right == 0) right = n + 1000;
        
        int result = (n - left) * (right - n) - 1;
        System.out.println(result);
    }
}