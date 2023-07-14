class Solution {
    public int longestSubsequence(int[] arr, int difference) {
        int n = arr.length;

        Map<Integer, Integer> dp = new HashMap<>();
        int ans = 0;
        for (int i = 0; i < n; i++){
            int prev = arr[i] - difference;

            dp.put(arr[i], dp.getOrDefault(prev, 0) + 1);
            ans = Math.max(ans, dp.get(arr[i]));

        }

        return ans;
    }
}
