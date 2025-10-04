import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        if ((a==b) && (b==c)) {
            System.out.println(10000+a*1000);
        }
        else if(a==b || b==c || a==c) {
            if(a==b || a==c) {
                System.out.println(1000+a*100);
            }else System.out.println(1000+b*100);
        }else {
            int max = a;
            if (a<b){
                if (c<b){
                    max=b;
                }
                else {
                    max=c;
                }
            }
            else if(a<c){
                if (c<b)
                    max=b;
                else if (b<c)
                    max=c;
            }
            System.out.println(max*100);
        }
    }
}
