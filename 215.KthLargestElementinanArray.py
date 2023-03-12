# For T : O(nlogn) use sorting 

# Avg. Case T : O(n) 
# Worst Case T : O(n^2)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p < k:
                return quickSelect(p + 1, r)
            
            elif p > k:
                return quickSelect(l , p - 1)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)
      
