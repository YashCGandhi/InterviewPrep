#DFS Solution. T : O(n^2)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        Map = {e:[] for e in range(1, len(edges) + 1)}

        visit = set()
        def dfs(start, end):
            if end in Map[start]:
                return False
            if start in visit:
                return True
            visit.add(start)
            for c in Map[start]:
                if not dfs(c, end):
                    return False
            visit.remove(start)
            return True
        for s, e in edges:
            if dfs(s, e):
                Map[s].append(e)
                Map[e].append(s)
            else:
                return [s, e]
