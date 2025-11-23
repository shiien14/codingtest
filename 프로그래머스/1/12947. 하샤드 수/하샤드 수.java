import java.util.*;

class Solution {
    public boolean solution(int x) {
        // sum(x) %x ==0
        
        String[] str = Integer.toString(x).split("");
        int x_sum=0;
        for(int i=0;i<str.length;i++){
            x_sum+=Integer.parseInt(str[i]);
        }
        
        if (x%x_sum==0) return true;
        else return false;
    }
}