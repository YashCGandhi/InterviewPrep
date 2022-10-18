class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # store the prereqs in a hashmap
        # dfs through the graph
        # have a visited set to find out circular loop... thats the invalid case.
        preMap = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitedSet = set()
        
        def dfs(crs):
            if crs in visitedSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitedSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitedSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True
