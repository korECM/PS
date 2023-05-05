import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for(int i = 0; i < commands.length; i++){
            int[] command = commands[i];
            answer[i] = solve(array, command);
        }
        return answer;
    }
    
    private int solve(int[] array, int[] command){
        int[] newArray = new int[command[1] - command[0] + 1];
        for(int i = command[0]; i <= command[1]; i++){
            newArray[i - command[0]] = array[i - 1];
        }
        Arrays.sort(newArray);
        return newArray[command[2] - 1];
    }
}