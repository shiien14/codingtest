class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        int tmp = Integer.parseInt(a+""+b);
        
        return tmp>=2*a*b ? tmp : 2*a*b;
    }
}