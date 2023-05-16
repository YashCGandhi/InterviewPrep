class Solution {
    public int findMin(int[] nums) {
        int res = nums[0];

        int l = 0;
        int r = nums.length - 1;
        int mid;
        while (l <= r){
            if (nums[l] <= nums[r]){
                res = Math.min(res, nums[l]);
                break;
            }

            mid = (l + r) / 2;
            res = Math.min(res, nums[mid]);
            if (nums[mid] >= nums[l] && nums[mid] >= nums[r]){
                l = mid + 1;
            }else{
                r = mid - 1;
            }
        }

        return res;
    }
}
