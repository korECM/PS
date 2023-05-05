import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        Integer[] nums = Arrays.stream(numbers)
            .boxed()
            .toArray(Integer[]::new);
        Arrays.sort(nums, (n1, n2) -> Integer.parseInt(n2.toString() + n1.toString()) -  Integer.parseInt(n1.toString() + n2.toString()));
        StringBuilder sb = new StringBuilder();
        for(Integer n : nums){
            sb.append(n.toString());
        }
        return sb.toString().replaceAll("^0+", "0");
    }
}