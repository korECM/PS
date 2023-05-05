import java.util.*;

class Solution {
    public int solution(String word) {
        List<String> m = new ArrayList(5 + 5 * 5 + 5 * 5 * 5 + 5 * 5 * 5 * 5 + 5 * 5 * 5 * 5 * 5);
        solve("", m);
        return m.indexOf(word);
    }
    
    private void solve(String word, List<String> m){
        m.add(word);
        if(word.length() == 5) return;
        for(String s : List.of("A", "E", "I", "O", "U")){
            solve(word + s, m);    
        }
    }
}


/*
상태
(word, m)

종료 조건
길이 5 -> m.add(word) 

점화식
(word, m) ->
m.add(word)
m.add((word + "A", m))
m.add((word + "E", m))
m.add((word + "I", m))
m.add((word + "O", m))
m.add((word + "U", m))

*/