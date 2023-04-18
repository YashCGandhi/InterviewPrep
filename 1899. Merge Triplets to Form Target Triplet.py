class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # T : O(m * n)
        if target in triplets:
            return True
        trip = [False] * len(target)
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for i, v in enumerate(t):
                if v == target[i]:
                    trip[i] = True
            if all(trip):
                return True

        return False

# I am a noob 
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # T : O(len(triplets * len(target)))
        # Remove the triplets with values greater than target 
        if target in triplets:
            return True

        toRemove = set()
        for idx,t in enumerate(triplets):
            for i, n in enumerate(t):
                if n > target[i]:
                    toRemove.add(idx)
                    break
        toRemove = sorted(list(toRemove))
        
        # Remove from the last index as size of the triplets array will change.
        for i in range(len(toRemove)-1, -1, -1):
            triplets.pop(toRemove[i])
        
        flags = [False] * len(target)
        for idx, t in enumerate(triplets):
            for i, n in enumerate(t):
                if n == target[i]:
                    flags[i] = True
                if all(flags):
                    return True
        return False
