class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> currentList = new ArrayList<>();
        backtrack(candidates, target, result, currentList, 0, 0);
        return result;

    }

    private void backtrack(int[] candidates, int target, List<List<Integer>> result, List<Integer> currentList, int currentSum, int index){
        
        if (index >= candidates.length || currentSum > target){
            return;
        } else if (currentSum == target){
            result.add(new ArrayList(currentList));
        }else{
            currentList.add(candidates[index]);
            backtrack(candidates, target, result, currentList, currentSum + candidates[index], index);

            currentList.remove(currentList.get(currentList.size() - 1));
            backtrack(candidates, target, result, currentList, currentSum, index + 1);
        }
    }
}
