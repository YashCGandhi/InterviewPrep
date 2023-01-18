class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        edges = []

        for i, building in enumerate(buildings):
            edges.append([building[0],i])
            edges.append([building[1],i])

        edges.sort()

        live, ans =[], []
        idx = 0

        while idx < len(edges):
            curr_x = edges[idx][0]

            while idx < len(edges) and edges[idx][0] == curr_x:

                b = edges[idx][1]

                if buildings[b][0] == curr_x:
                    right = buildings[b][1]
                    height = buildings[b][2]

                    heapq.heappush(live, [-height, right])

                while live and live[0][1] <= curr_x:
                    heapq.heappop(live)
                idx += 1
            max_height = -live[0][0] if live else 0

            if not ans or ans[-1][1] != max_height:
                ans.append([curr_x, max_height])
        
        return ans





















        """
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
        """
