class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x,y in points:
            heap.append([math.sqrt(x**2 + y **2), (x, y)])
        heapq.heapify(heap)
        
        while heap and k > 0:
            val, coor = heapq.heappop(heap)
            res.append(coor)
            k -= 1

        return res
