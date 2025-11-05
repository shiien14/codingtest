import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str;
        char[][] arr = new char[5][15];

        for(int i=0;i<5;i++){
            str=br.readLine();
            for(int j =0;j<str.length();j++){
                arr[i][j]=str.charAt(j);
            }
        }

        for(int i=0;i<15;i++){
            for(int j=0;j<5;j++){
                if('\0' != arr[j][i]){
                    System.out.print(arr[j][i]);
                }
            }
        }

    }
}
