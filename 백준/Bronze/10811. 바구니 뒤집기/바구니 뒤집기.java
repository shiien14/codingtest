import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] basket = new int[n];

        for (int i = 0; i < n; i++) basket[i] = i+1;

        for (int i = 0; i < m; i++) {
            StringTokenizer st1 = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st1.nextToken());
            int y = Integer.parseInt(st1.nextToken());

            while(x<y){
                int temp = basket[x-1];
                basket[x-1] = basket[y-1];
                basket[y-1] = temp;
                x++;
                y--;
            }
        }

        for(int i = 0; i < n; i++) System.out.print(basket[i]+" ");
    }
}
