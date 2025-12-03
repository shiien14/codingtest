import java.util.HashMap;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int n = nums.length;
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int num : nums){
            map.put(num, map.getOrDefault(num, 0)+1);
        }
        int m = map.size();
        answer = (m < n/2) ? m:n/2;
        return answer;
    }
}