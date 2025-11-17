import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i = 0; i < n; i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        int m = Integer.parseInt(br.readLine());
        st= new StringTokenizer(br.readLine());

        for(int i = 0; i < m; i++){
            int num = Integer.parseInt(st.nextToken());
            bw.write(findEnd(arr,num) - findStart(arr,num)+" ");
        }
        bw.flush();
        bw.close();

    }

    private static int findStart(int[] arr, int num){
        int left = 0;
        int right = arr.length;

        while(left<right){
            int mid = (left+right)/2;
            if (num<=arr[mid]){
                right = mid;
            }
            else left = mid+1;
        }
        return left;
    }

    private static int findEnd(int[] arr, int num){
        int left = 0;
        int right = arr.length;
        while(left<right){
            int mid = (left+right)/2;
            if (num<arr[mid]){
                right = mid;
            }
            else left = mid+1;
        }

        return left;
    }
}
