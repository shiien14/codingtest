import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            String s = st.nextToken();

            for (int i=0;i<s.length();i++){
                for  (int j=0;j<N;j++){
                    System.out.print(s.charAt(i));
                }
            }
            System.out.println();
        }
    }
}
