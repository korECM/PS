import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings, (v1, v2) -> compare(v1, v2, n));
        return strings;
    }
    
    private int compare(String v1, String v2, int n){
        int result = v1.charAt(n) - v2.charAt(n);
        if(result == 0){
            return v1.compareTo(v2);
        }
        return result;
    }
}