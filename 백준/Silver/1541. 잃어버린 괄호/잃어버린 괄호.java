import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        String[] formula = str.split("-");
        
        int add =0;
        int result = 0;

        for(int i =0; i<formula.length ; i++){
            String[] plus = formula[i].split("\\+");
            
            for(int j =0; j<plus.length ; j++){
                add+=Integer.parseInt(plus[j]);
            }
            
            if(i==0) result = add;
            else result-=add;
            
            add=0;
        }

        System.out.println(result);

    }
}