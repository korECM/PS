class Solution {
    public int[] solution(long n) {
        String reversed = new StringBuilder(Long.toString(n)).reverse().toString();
        char[] chars = reversed.toCharArray();
        int[] answer = new int[chars.length];
        for(int i = 0; i < chars.length; i++){
            answer[i] = chars[i] - '0';
        }
        return answer;
    }
}