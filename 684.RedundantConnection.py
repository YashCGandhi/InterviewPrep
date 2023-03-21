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

            
# Union-Find T : O(n)        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [ i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]          
