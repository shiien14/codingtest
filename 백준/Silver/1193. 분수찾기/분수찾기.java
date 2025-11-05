import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        int line = 0;
        int count = 0;
        
        while (count < n) {
            line++;
            count = line * (line + 1) / 2;
        }
        
        int diff = count - n;

        if (line % 2 == 0) {
            System.out.println((line - diff) + "/" + (1 + diff));
        } else {
            System.out.println((1 + diff) + "/" + (line - diff));
        }
    }
}

