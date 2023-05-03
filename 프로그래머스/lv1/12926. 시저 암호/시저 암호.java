class Solution {
    public String solution(String s, int n) {
        StringBuilder sb = new StringBuilder();
        
        char[] arr = s.toCharArray();
        for(char c : arr) {
            if(!Character.isAlphabetic(c)) {
                sb.append(c);
                continue;
            }
            boolean isUp = c < 'a';
            int nn = isUp ? c - 'A' : c - 'a';
            nn = (nn + n) % 26;
            if(isUp){
                sb.append((char)(nn + 'A'));
            } else {
                sb.append((char)(nn + 'a'));
            }
        }
        
        return sb.toString();
    }
}