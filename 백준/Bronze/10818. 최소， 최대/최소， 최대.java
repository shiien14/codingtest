import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());
        int arr[] = new int[t];
        
        st = new StringTokenizer(br.readLine(), " ");    
        
        int i=0;
        for(i =0;i<t;i++) {
        	arr[i]=Integer.parseInt(st.nextToken());
        }
        
        int h=arr[0];
        int l=arr[0];
        
        for(i=0;i<t-1;i++) {
        	if(h<arr[i+1]) {
        		h=arr[i+1];
        	}else if(l>arr[i+1])
        		l=arr[i+1];
        }
        bw.write(l+ " "+ h);
        bw.close();
    }
}

