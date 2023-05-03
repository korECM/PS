import java.util.*;

class Solution {
    private static final int[] fdx = {0, 1, -1, 0};
    private static final int[] fdy = {1, 0, 0, -1};
    private static final int[][] sdx = {
            {-1, 0, 1},
            {0, 1, 0},
            {-1, 0, 0},
            {-1, 0, 1}
    };
    private static final int[][] sdy = {
            {0, 1, 0},
            {1, 0, -1},
            {0, -1, 1},
            {0, -1, 0}
    };


    public int[] solution(String[][] places) {
        int[] answer = new int[places.length];
        for (int i = 0; i < places.length; i++) {
            System.out.println("Board : " + i);
            answer[i] = solve(places[i]);
        }
        return answer;
    }

    private int solve(String[] place) {
        int size = place.length;
        String[][] boards = new String[size][size];
        
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                boards[i][j] = String.valueOf(place[i].charAt(j));
            }
        }
        
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (!boards[i][j].equals("P")) continue;
                int x = j;
                int y = i;
                for (int fdi = 0; fdi < 4; fdi++) {
                    int fx = x + fdx[fdi];
                    int fy = y + fdy[fdi];
                    if (fx < 0 || fy < 0 || fx >= size || fy >= size) continue;
                    if (boards[fy][fx].equals("X")) continue;
                    if (boards[fy][fx].equals("P")) System.out.println("x : " + x + " y : " + y + " fail[1] fdi : " + fdi);
                    if (boards[fy][fx].equals("P")) return 0;
                    for (int sdi = 0; sdi < 3; sdi++) {
                        int sx = fx + sdx[fdi][sdi];
                        int sy = fy + sdy[fdi][sdi];
                        if (sx < 0 || sy < 0 || sx >= size || sy >= size) continue;
                        if (boards[sy][sx].equals("P")) System.out.println("x : " + x + " y : " + y + " sx : " + sx + " sy : " + sy + " fail[2] sdi : " + sdi + " fdi : " + fdi);
                        if (boards[sy][sx].equals("P")) return 0;
                    }
                }
            }
        }

        return 1;
    }
}