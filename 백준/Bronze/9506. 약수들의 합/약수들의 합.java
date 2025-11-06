import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            int N = Integer.parseInt(br.readLine());
            if (N == -1) break;

            StringBuilder sb = new StringBuilder();
            int sum = 1;

            sb.append(N+" = " + "1");
            for(int i=2;i<N;i++){
                if (N%i==0){
                   sum+=i;
                   sb.append(" + "+i);
                }
            }

            if (sum==N){
                System.out.println(sb.toString());
            }
            else System.out.println(N+" is NOT perfect.");
        }

    }
}
