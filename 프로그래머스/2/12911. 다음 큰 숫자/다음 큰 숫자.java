class Solution {
    public int solution(int n) {
        String binary = Integer.toBinaryString(n);

        int nCount = 0;
        for (int i = 0; i < binary.length(); i++) {
            if (binary.charAt(i) == '1') {
                nCount++;
            }
        }

        int count = 0;
        int cur = n;
        while (true) {
            cur += 1;

            String new1 = Integer.toBinaryString(cur);

            count = 0;
            for (int i = 0; i < new1.length(); i++) {
                if (new1.charAt(i) == '1') {
                    count++;
                }
            }

            if (count == nCount) {
                return cur;
            }
        }
    }
}
