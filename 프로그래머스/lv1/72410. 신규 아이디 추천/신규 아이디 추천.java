class Solution {
    public String solution(String newId) {
        String answer = newId.toLowerCase()
            .replaceAll("[^a-z0-9\\-_.]", "")
            .replaceAll("\\.+", ".")
            .replaceAll("^\\.|\\.$", "");
        if(answer.length() > 15){
            answer = answer.substring(0, 15)
            .replaceAll("^\\.|\\.$", "");
        }
        if(answer.length() == 0){
            answer = "aaa";
        }
        while(answer.length() <= 2){
            answer += answer.substring(answer.length() - 1, answer.length());
        }
        
        return answer;
    }
}