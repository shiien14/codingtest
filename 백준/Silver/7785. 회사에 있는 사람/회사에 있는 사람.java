import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());

        HashSet<String> map = new HashSet<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String info = st.nextToken();

            if (info.equals("enter")){
                map.add(name);
            }else if(info.equals("leave")){
                map.remove(name);
            }
        }

        br.close();

        ArrayList<String> list = new ArrayList<String>(map);
        Collections.sort(list, Collections.reverseOrder());

        StringBuilder sb = new StringBuilder();
        for(String l : list){
            sb.append(l).append("\n");
        }

        System.out.println(sb);
    }
}
