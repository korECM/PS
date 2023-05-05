class Solution {
    public int[] solution(String s) {
        int[] answer = {0, 0};
        
        while(!s.equals("1")){
            int oneCount = count(s);
            answer[0] += 1;
            answer[1] += s.length() - oneCount;
            s = Integer.toString(oneCount, 2);
        }
        
        return answer;
    }
    
    private int count(String s){
        int count = 0;
        char[] arr = s.toCharArray();
        for(char c : arr){
            if(c == '1'){
                count += 1;
            }
        }
        return count;
    }
}