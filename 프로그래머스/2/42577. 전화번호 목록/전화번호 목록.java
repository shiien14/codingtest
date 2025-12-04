import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        HashSet<String> set = new HashSet<>();

        for(String number : phone_book){
            set.add(number);
        }
        
        List<String> sorted = new ArrayList<>(set);
        Collections.sort(sorted);
        
        for (int i = 0; i < sorted.size() - 1; i++) {
            String cur = sorted.get(i);
            String next = sorted.get(i + 1);
            if (next.startsWith(cur)) {
                return false;
            }
        }

        return true;
    }
}