class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> count = new HashMap<>();
        List<Integer> bucket[] = new ArrayList[nums.length + 1];

        // Similar to Counter in Python.
        for (int num : nums){
            count.put(num, count.getOrDefault(num, 0) + 1);
            //count.merge(num, 1, Integer::sum);
        }
        
        for(int key : count.keySet()){
            int freq = count.get(key);
            if(bucket[freq] == null){
                bucket[freq] = new ArrayList<>();
            }
            bucket[freq].add(key);
        }
        
        int index = 0;
        int[] res = new int[k];
        
        for (int i = nums.length; i >= 0; i--){
            if(bucket[i] != null){
                for (int val : bucket[i]){
                    res[index++] = val;
                    if (index == k){
                        return res;
                    }
                }
            }
        }

        return res;
    }
}
