import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[][] dist = new int[N][N];

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if (i == j) dist[i][j] = 0;
                else dist[i][j] = 1000;
            }
        }

        for(int i = 0; i < N; i++){
            char[] T = br.readLine().toCharArray();

            for(int j = 0; j < N; j++){
                if(T[j]=='Y'){
                    dist[i][j]=1;
                }
            }

        }

        for (int k = 0; k < N; k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }

        int answer = 0;

        for (int i = 0; i < N; i++) {
            int count = 0;
            for (int j = 0; j < N; j++) {
                if (i == j) continue;
                if (dist[i][j] <= 2) count++;
            }

            answer = Math.max(answer, count);
        }

        System.out.println(answer);
    }

}