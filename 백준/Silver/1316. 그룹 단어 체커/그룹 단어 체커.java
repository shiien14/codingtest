import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int answer=n;
        for (int i = 0; i < n; i++) {
            String str = br.readLine();

            boolean[] check = new boolean[26];
            int prev=0;

            for (int j = 0; j < str.length(); j++) {
                int now = str.charAt(j);

                if (prev != now){
                    if (!check[now - 'a']){
                        check[now-'a']=true;
                        prev = now;
                    }
                    else{
                        answer--;
                        break;
                    }
                }
            }
        }
        System.out.println(answer);
    }
}
