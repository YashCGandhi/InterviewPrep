# T : O(n^2)
# get unique start and end positions and sort them
# store their x_val and index in a edge_map
# create a heights array of the len(positions) to store max height at that position
# loop through the heights and find out where the heights change and add those to the ans
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        positions = sorted(list(set([x for building in buildings for x in building[:2]])))

        edge_map = { x : i for i, x in enumerate(positions)}

        heights = [0] * len(positions)

        for l,r,h in buildings:
            left_idx = edge_map[l]
            right_idx = edge_map[r]

            for i in range(left_idx, right_idx):
                heights[i] = max(heights[i], h)
            
        ans = []

        for i in range(len(heights)):
            curr_height = heights[i]
            curr_x = positions[i]

            if not ans or ans[-1][1] != curr_height:
                ans.append([curr_x, curr_height])
        return ans
