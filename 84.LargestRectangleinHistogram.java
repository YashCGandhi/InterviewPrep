class Solution {
    class Pair{
        int idx, height;
        public Pair(int idx, int height){
            this.idx = idx;
            this.height = height;
        }
    }
    public int largestRectangleArea(int[] heights) {
        Stack<Pair> stack = new Stack<>();
        int N = heights.length;
        int maxArea = 0;

        for(int i = 0; i < N; i++){
            if(stack.isEmpty() || stack.peek().height < heights[i]){
                stack.add(new Pair(i, heights[i]));
                continue;
            }
            else{
                int index = i;
                while(!stack.isEmpty() && stack.peek().height >= heights[i]){
                    Pair p = stack.pop();
                    index = p.idx;
                    maxArea = Math.max(maxArea, (i - p.idx) * p.height);
                }
                stack.add(new Pair(index, heights[i]));
            }
        }
        while(!stack.isEmpty()){
            Pair s = stack.pop();
            maxArea = Math.max(maxArea, (N - s.idx) * s.height);
        }
        return maxArea;

    }
}
