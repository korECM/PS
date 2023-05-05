import java.util.*;

class Solution {
    public int solution(int[] c) {
        int answer = 0;
        
        Arrays.sort(c);
        for(int i = c.length - 1; i >= 0; i--){
            int cc = c[i];
            if(cc >= c.length - i) answer += 1;
        }
        return answer;
    }
}

// [0 1 3 5 6]
// i = 4 -> c - i = 1 
// i = 3 -> c - i = 2
// i = 2 -> c - i = 3