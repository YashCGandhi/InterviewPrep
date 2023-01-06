"""
A + B + C + D = 0 --> A + B = -(C + D)
Create a hashmap with sums of nums1 and nums2 
Check if complements exists in sums of nums3 and nums4
"""

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # mp1 = collections.defaultdict(int)
        mp1= {}
        for n1 in nums1:
            for n2 in nums2:
                mp1[n1 + n2] = 1 + mp1.get(n1+n2, 0)
        
        cnt = 0
        for n3 in nums3:
            for n4 in nums4:
                cnt += mp1.get(-(n3+n4),0)
        
        return cnt
