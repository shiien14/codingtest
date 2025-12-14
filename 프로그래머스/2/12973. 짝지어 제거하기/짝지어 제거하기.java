import java.util.*;

class Solution
{
    public int solution(String s)
    {
        int answer = 0;
        
        Stack<Character> stack = new Stack();
        
        char[] chars = s.toCharArray();
        
        for(int i = 0; i<chars.length;i++){
            if(stack.isEmpty()){
                stack.push(chars[i]);
            }
            else if(stack.peek() == chars[i]){
                stack.pop();
            }
            else stack.push(chars[i]);
        }
        
        if (stack.size()==0) return 1;

        return answer;
    }
}