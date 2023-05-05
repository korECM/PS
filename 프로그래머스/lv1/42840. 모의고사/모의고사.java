import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final int[] a = new int[]{1, 2, 3, 4, 5};
    private static final int[] b = new int[]{2, 1, 2, 3, 2, 4, 2, 5};
    private static final int[] c = new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

    public int[] solution(int[] answers) {
        List<Integer> answer = new ArrayList();
        int aCount = 0, bCount = 0, cCount = 0;
        for (int i = 0; i < answers.length; i++) {
            if (a[i % a.length] == answers[i]) aCount += 1;
            if (b[i % b.length] == answers[i]) bCount += 1;
            if (c[i % c.length] == answers[i]) cCount += 1;
        }
        int max = Math.max(aCount, Math.max(bCount, cCount));
        if (max == aCount) {
            answer.add(1);
        }
        if (max == bCount) {
            answer.add(2);
        }
        if (max == cCount) {
            answer.add(3);
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}