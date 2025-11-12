import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st;

        Set<String> set = new HashSet<String>();
        set.add("ChongChong");

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            String A = st.nextToken();
            String B = st.nextToken();

            if(set.contains(A)){
                set.add(B);
            } else if (set.contains(B)){
                set.add(A);
            }
        }
        System.out.println(set.size());
    }
}
