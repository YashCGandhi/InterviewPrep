# The only change in permutation 1 and 2 is that 2 contains duplicates in the array which is provided. So, we have to make sure we dont add duplicates in the result. This is done by using a hashmap which contains the numbers of occurences of each number in the array. We only add an element to the current permutation if the count of that number in the hashmap is greater than 0.
def permuteUnique(self, nums: List[int]) -> List[List[int]]:  
        count = collections.Counter(nums)
        res = []
        perm = []
        
        def dfs():

            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] += 1
                    perm.pop()
        dfs()
        return res
