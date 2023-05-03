class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        int count = 0;
        char[] arr = s.toCharArray();
        for(char c : arr){
            if(!Character.isAlphabetic(c)) {
                count = 0;
                sb.append(c);
                continue;
            }
            count += 1;
            if(count % 2 == 1){
                sb.append(Character.toUpperCase(c));
            }else {
                sb.append(Character.toLowerCase(c));  
            }
        }
        
        return sb.toString();
    }
}