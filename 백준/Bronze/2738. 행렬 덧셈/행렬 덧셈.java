import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int N = Integer.parseInt(str.split(" ")[0]);
        int M = Integer.parseInt(str.split(" ")[1]);

        int[][] A = new int[N][M];
        int[][] B = new int[N][M];

        for(int i =0;i<N;i++){
            String line = br.readLine();
            for(int j =0;j<M;j++){
                A[i][j] = Integer.parseInt(line.split(" ")[j]);
            }
        }

        for(int i =0;i<N;i++){
            String line = br.readLine();
            for(int j =0;j<M;j++){
                B[i][j] = Integer.parseInt(line.split(" ")[j]);
            }
        }

        StringBuilder sb = new StringBuilder();
        for(int i=0;i<N;i++){
            for(int j =0;j<M;j++){
                sb.append((A[i][j]+B[i][j]));
                if(j<M-1){
                    sb.append(" ");
                }
            }
            sb.append("\n");
        }
        
        System.out.println(sb.toString());

    }
}
