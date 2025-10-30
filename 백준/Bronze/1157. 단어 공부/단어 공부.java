import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int len = str.length();
        int[] cnt = new int[26];

        for (int i = 0; i < len; i++) {
            if ('A'<=str.charAt(i) && str.charAt(i) <= 'Z') {
                cnt[str.charAt(i) - 'A']++;
            }
            else{
                cnt[str.charAt(i) - 'a']++;
            }
        }

        int max = -1;
        char answer = '?';

        for (int i = 0; i < 26; i++) {
            if (cnt[i] > max) {
                max = cnt[i];
                answer = (char)(i+65);
            }
            else if(cnt[i]==max){
                answer = '?';
            }
        }

        System.out.println(answer);
    }
}
