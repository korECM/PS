import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        
        Stack<State> stack = new Stack();
        
        stack.push(new State(0, 0));
        
        while(!stack.isEmpty()){
            State state = stack.pop();
            
            if(state.index == numbers.length){
                if(state.acc == target) answer++;
                continue;
            }
            
            stack.push(new State(state.index + 1, state.acc + numbers[state.index]));
            stack.push(new State(state.index + 1, state.acc - numbers[state.index]));
        }
        
        return answer;
    }
}

class State {
    int index;
    int acc;
    State(int index, int acc){
        this.index = index;
        this.acc = acc;
    }
}