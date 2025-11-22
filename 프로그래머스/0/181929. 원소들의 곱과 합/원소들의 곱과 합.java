class Solution {
    public int solution(int[] num_list) {
        int num_plus=0;
        int num_multi=1;
        for(int i=0;i<num_list.length;i++){
            num_plus+=num_list[i];
            num_multi*=num_list[i];
        }
        
        if ((num_plus*num_plus) > num_multi){
            return 1;
        }
        
        return 0;
    }
}