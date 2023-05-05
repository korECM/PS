import java.util.*;

class Solution {
    public int solution(String[] userIds, String[] bannedIds) {
        bannedIds = Arrays.stream(bannedIds)
            .map(b -> b.replace('*', '.'))
            .toArray(String[]::new);
        Set<Integer> accSet = new HashSet();
        solve(userIds, bannedIds, 0, 0, accSet);
        
        return accSet.size();
    }
    
    private void solve(String[] userIds, String[] bannedIds, int banIndex, int acc, Set<Integer> accSet){
        if(banIndex == bannedIds.length) {
            accSet.add(acc);
            return;
        }
        String banRegex = bannedIds[banIndex];
        for(int i = 0; i < userIds.length; i++){
            // 이미 밴된 경우
            if((acc & (1 << i)) > 0) continue;
            // 불량 사용자 X
            if(!userIds[i].matches(banRegex)) continue;
            acc |= 1 << i;
            solve(userIds, bannedIds, banIndex + 1, acc, accSet);
            acc ^= 1 << i;
        }
    }
}

/*
상태
(userIds, userChecked, bannedIds, banChecked, acc)

종료 조건

점화식
for (bannedId : bannedIds) {
    if(banChecked[]) continuie;
    for(int i = 0; i < userIds.length; i++){
        if(userChecked[i]) continue;
        userChecked[i] = true;
        banChecked[] = true;
        (userIds, userChecked, bannedIds, banChecked, acc | 1 << i)
        banChecked[] = false;
    }
}

userChecked -> acc 비트 연산으로 대체


*/