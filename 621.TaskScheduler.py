class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        heap = [-v for v in count.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0
        while heap or queue:

            
            time += 1
            if not heap:
                time = queue[0][1]
            else:
                task = 1 + heapq.heappop(heap)
            
                if task < 0:
                    queue.append([task, time + n])
            
            if queue and queue[0][1] == time:
                v,t = queue.popleft()
                heapq.heappush(heap, v)
            
        return time
