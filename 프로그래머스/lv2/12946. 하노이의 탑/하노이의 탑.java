import java.util.*;

class Solution {
    public int[][] solution(int n) {
        return solve(n, 1, 2, 3).toArray(new int[0][]);
    }
    
    private List<int[]> solve(int n, int s, int m, int d){
        if(n == 1) return List.of((new int[]{s, d}));
        List<int[]> result = new ArrayList();
        result.addAll(solve(n - 1, s, d, m));
        result.addAll(solve(1, s, m, d));
        result.addAll(solve(n - 1, m, s, d));
        return result;
    }
}

/*
상태
(n, s, m, d)

종료 조건
n == 1 -> [s, d]

재귀
(n, s, m, d) = (n - 1, s, d, m) + (1, s, m, d) + (n - 1, m, s, d)

*/