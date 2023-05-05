class Solution {
    public int[] solution(int[][] arr) {
        return solve(arr, 0, 0, arr[0].length, arr.length).toAnswer();
    }
    
    private Data solve(int[][] arr, int leftUpperX, int leftUpperY, int rightLowerX, int rightLowerY){
        if(leftUpperX == rightLowerX && leftUpperY == rightLowerY){
            return getCompressedResult(arr[leftUpperY][leftUpperX]);
        }
        if(canCompress(arr, leftUpperX, leftUpperY, rightLowerX, rightLowerY)){
            return getCompressedResult(arr[leftUpperY][leftUpperX]);
        }
        return solve(arr, leftUpperX, leftUpperY, (rightLowerX + leftUpperX) / 2, (rightLowerY + leftUpperY) / 2)
            .plus(solve(arr, (leftUpperX + rightLowerX) / 2, leftUpperY, rightLowerX, (rightLowerY + leftUpperY) / 2))
            .plus(solve(arr, leftUpperX, (leftUpperY + rightLowerY) / 2, (rightLowerX + leftUpperX) / 2, rightLowerY))
            .plus(solve(arr, (leftUpperX + rightLowerX) / 2, (leftUpperY + rightLowerY) / 2, rightLowerX, rightLowerY));
    }
    
    private boolean canCompress(int[][] arr, int leftUpperX, int leftUpperY, int rightLowerX, int rightLowerY){
        int initValue = arr[leftUpperY][leftUpperX];
        for(int x = leftUpperX; x < rightLowerX; x++){
            for(int y = leftUpperY; y < rightLowerY; y++){
                if(arr[y][x] != initValue) return false;
            }
        }
        return true;
    }
    
    private Data getCompressedResult(int value){
        if(value == 0){
            return new Data(1, 0);
        }else {
            return new Data(0, 1);
        }
    }
}

class Data{
    int zero, one;
    
    public Data(){
        zero = 0;
        one = 0;
    }
    
    public Data(int zero, int one){
        this.zero = zero;
        this.one = one;
    }
    
    public Data plus(Data data){
        return new Data(zero + data.zero, one + data.one);
    }
    
    public int[] toAnswer(){
        return new int[]{zero, one};
    }
}

/*

상태
(arr, leftUpperX, leftUpperY, rightLowerX, rightLowerY)

종료 조건
boundary size == 1 -> return new Data(0, 1) or new Data(1, 0)
모든 값이 같으면 -> return new Data(0, 1) or new Data(0, 1)

점화식
(arr, leftUpperX, leftUpperY, rightLowerX, rightLowerY)
=
(arr, leftUpperX, leftUpperY, (rightLowerX + leftUpperX) / 2, (rightLowerY + leftUpperY) / 2) +
(arr, (leftUpperX + rightLowerX) / 2, leftUpperY, rightLowerX, (rightLowerY + leftUpperY) / 2) +
(arr, leftUpperX, (leftUpperY + rightLowerY) / 2, (rightLowerX + leftUpperX) / 2, rightLowerY) +
(arr, (leftUpperX + rightLowerX) / 2, (leftUpperY + rightLowerY) / 2, rightLowerX, rightLowerY)

*/