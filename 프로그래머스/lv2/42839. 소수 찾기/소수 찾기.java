import java.util.*;

class Solution {
    public int solution(String numbers) {
        Set<Integer> primes = new HashSet();
        check("", Arrays.asList(numbers.split("")), primes);
        return primes.size();
    }
    
    private void check(String n, List<String> numbers, Set<Integer> primes){
        if(n.length() > 0){
            int num = Integer.valueOf(n);
            if(isPrime(num)) primes.add(num);    
        }
        if(numbers.isEmpty()) return;
        for(int i = 0; i < numbers.size(); i++){
            String newChar = n + numbers.get(i);
            List<String> newNumbers = new ArrayList(numbers);
            newNumbers.remove(i);
            check(newChar, newNumbers, primes);
        }
    }
    
    private boolean isPrime(int n){
        if(n <= 1) return false;
        if(n <= 3) return true;
        for(int i = 2; i <= Math.floor(Math.sqrt(n)); i++){
            if(n % i == 0) return false;
        }
        return true;
    }
}

/*
상태
(str, numbers, primes)

종료 조건
numbers.isEmpty()

점화식
(str, numbers, primes) ->
(str + numbers[0], numbers - numbers[0], primes)
(str + numbers[1], numbers - numbers[1], primes)
...


*/
