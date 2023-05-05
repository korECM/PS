import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int len = numbers.length;
        Set<Integer> answers = new HashSet(len * len);
        for(int i = 0; i < len; i++){
            for(int j = i + 1; j < len; j++){
                answers.add(numbers[i] + numbers[j]);
            }
        }
        List<Integer> sortedAnswers = new ArrayList(answers);
        Collections.sort(sortedAnswers);
        return sortedAnswers.stream().mapToInt(i -> i).toArray();
    }
}