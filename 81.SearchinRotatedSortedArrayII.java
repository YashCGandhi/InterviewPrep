class Solution {
    public boolean search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        int mid;
        while ( l <= r ){
            while (l < r && nums[l] == nums[l + 1]){
                l++;
            }

            while( l < r && nums[r] == nums[r - 1]){
                r--;
            }

            mid = (l + r) / 2;

            if (nums[mid] == target){
                return true;
            }

            if (nums[mid] >= nums[l]){
                if ( target >= nums[l] && target <= nums[mid]){
                    r = mid - 1;
                }else{
                    l = mid + 1;
                }
            }else{
                if (target >= nums[mid] && target <= nums[r]){
                    l = mid + 1;
                }else{
                    r = mid - 1;
                }
            }
        }

        return false;
    }
}
