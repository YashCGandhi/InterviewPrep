class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> currentList = new ArrayList<>();
        backtrack(ans, 0, nums, currentList);
        return ans;
    }

    private void backtrack(List<List<Integer>> ans, int index, int[] nums, List<Integer> currentList){
        if (index == nums.length){
            ans.add(new ArrayList(currentList));
            return;
        } else{
            
            currentList.add(nums[index]);
            backtrack(ans, index + 1, nums, currentList);

            // removing the last element is important because, if not it will get carried on in the next recursive call. ( Draw out the recursive stack)
            currentList.remove(currentList.size() - 1);
            backtrack(ans, index + 1, nums, currentList);
        }


    }
}
