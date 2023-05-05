class Solution {
    public int[] solution(int brown, int yellow) {
        int width, height;
        for(width = 3; width < 5000; width++){
            for(height = 3; height <= width; height++){
                if((width - 2) * (height - 2) == yellow){
                    if(width + height - 2 == brown / 2 ){
                        return new int[]{width, height};
                    }
                }
            }
        }
        return new int[]{};
    }
}