import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String N = st.nextToken();
        int B = Integer.parseInt(st.nextToken());

        long result = 0;
        for (int i = 0; i < N.length(); i++) {
            char ch = N.charAt(i);

            int val;
            if ('0' <= ch && ch <= '9') val = ch - '0';
            else val = ch - 'A' + 10;

            result = result * B + val;
        }
        System.out.println(result);
    }
}