class Solution {
    public int[] dailyTemperatures(int[] tmp) {
        Stack<int[]> stack = new Stack<>();
        int[] ans = new int[tmp.length];

        for(int i = 0; i < tmp.length; i++){
            while(!stack.isEmpty() && tmp[i] > stack.peek()[0]){
                int[] curr = stack.pop();
                ans[curr[1]] = i - curr[1];
            }
            stack.push(new int[]{tmp[i], i});
        }
        return ans;
    }
}
