class Solution {
    boolean solution(String s) {
        return count(s, 'p') == count(s, 'y');
    }
    
    private int count(String s, char c){
        int count = 0;
        for(char cs : s.toLowerCase().toCharArray()){
            if(cs == c) count++;
        }
        return count;
    }
}