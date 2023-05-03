class Solution {
    public int[] solution(int n) {
        int[] dx = {0, 1, -1};
        int[] dy = {1, 0, -1};

        int totalLength = (n * (n + 1)) / 2;
        int[][] boards = new int[n][n];
        int x = 0;
        int y = -1;
        int cnt = -1;
        int singleLength = n;
        int i = 1;
        while (i <= totalLength) {
            cnt = (cnt + 1) % 3;
            for (int j = 0; j < singleLength; j++) {
                // System.out.println(cnt);
                x += dx[cnt];
                y += dy[cnt];
                boards[y][x] = i++;
            }
            singleLength--;
        }

        int[] answer = new int[totalLength];
        int index = 0;
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                if (boards[j][k] != 0) {
                    answer[index++] = boards[j][k];
                }
            }
        }

        return answer;
    }
}