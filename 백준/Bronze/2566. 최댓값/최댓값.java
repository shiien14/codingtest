import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[][] A = new int[9][9];

        int max = 0;
        int x = 1;
        int y = 1;

        for(int i=0;i<9;i++){
            String str = br.readLine();
            for(int j=0;j<9;j++){
                A[i][j]=Integer.parseInt(str.split(" ")[j]);
                if (A[i][j]>max){
                    max=A[i][j];
                    x=i+1;
                    y=j+1;
                }
            }
        }
        
        System.out.println(max);
        System.out.print(x+" "+ y);
    }
}
