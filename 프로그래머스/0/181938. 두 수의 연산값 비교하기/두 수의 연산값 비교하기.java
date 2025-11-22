class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        String str = a+""+b;
        
        return Integer.parseInt(str)>=2*a*b ? Integer.parseInt(str) : 2*a*b;
    }
}