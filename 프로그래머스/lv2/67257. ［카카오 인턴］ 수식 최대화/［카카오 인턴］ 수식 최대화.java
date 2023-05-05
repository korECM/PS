import java.util.*;

class Solution {
    private static final String[][] p = {
        "+*-".split(""),
        "+-*".split(""),
        "-+*".split(""),
        "-*+".split(""),
        "*+-".split(""),
        "*-+".split(""),
    };
    
    public long solution(String expression) {
        long answer = Long.MIN_VALUE;
        List<String> tokens = extractTokens(expression);
        for(String[] cp : p){
            List<String> curTokens = new ArrayList(tokens);
            for(String op : cp){
                int i = curTokens.indexOf(op);
                while(i != -1){
                    long result = calc(curTokens.get(i - 1), curTokens.get(i + 1), curTokens.get(i));
                    curTokens.remove(i - 1);
                    curTokens.remove(i - 1);
                    curTokens.remove(i - 1);
                    curTokens.add(i - 1, String.valueOf(result));
                    i = curTokens.indexOf(op);
                }
            }
            answer = Math.max(answer, Math.abs(Long.valueOf(curTokens.get(0))));
        }

        return answer;
    }
    
    private List<String> extractTokens(String expression){
        StringTokenizer st = new StringTokenizer(expression, "+-*", true);
        List<String> tokens = new ArrayList();
        while(st.hasMoreTokens()){
            tokens.add(st.nextToken());
        }
        return tokens;
    }
    
    private long calc(String lhsStr, String rhsStr, String ops){
        return calc(Long.valueOf(lhsStr), Long.valueOf(rhsStr), ops);
    }
    
    private long calc(long lhs, long rhs, String ops){
        switch(ops){
            case "+": return lhs + rhs;
            case "-": return lhs - rhs;
            case "*": return lhs * rhs;
            default: return 0;
        }
    }
}