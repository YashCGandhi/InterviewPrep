class Solution {
    public int trap(int[] height) {
        int size = height.length;
        int[] leftMax = new int[size];
        int[] rightMax = new int[size];
        int result = 0;

        leftMax[0] = 0;
        rightMax[size-1] = 0;

        for (int i = 1; i < size; i++){
            leftMax[i] = Math.max(leftMax[i-1], height[i-1]);
        }

        for (int i = size - 2; i >= 0; i--){
            rightMax[i] = Math.max(rightMax[i+1], height[i+1]);
        }

        for (int i = 0; i < size; i++){
            int water = Math.min(leftMax[i], rightMax[i]) - height[i];
            if (water > 0){
                result += water;
            }
        }

        return result;
    }
}
