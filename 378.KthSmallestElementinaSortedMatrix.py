# Brute force approach is flatten the matrix and sort it. Then return the kth element in the list.
# T:O(n^2 logn^2)
# S:O(n^2)

# Method 2: Min-Heap
# T: X = min(k,N); X + Klog(X) --> heap construction takes O(X) and log(X) to add and remove elements --> X also is the size of the heap.
# S: O(X)

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)        

        minHeap = []

        for r in range(min(k,N)):
            minHeap.append((matrix[r][0], r, 0))

        heapq.heapify(minHeap)
        # print("after inital Insertion")
        # print(minHeap)
        # print("********************************")
        while k:

            element, r, c = heapq.heappop(minHeap)
            # print("ele : " + str(element))
            if c < N - 1:
                heapq.heappush(minHeap,(matrix[r][c+1], r, c + 1))
            # print(minHeap)
            k -= 1

        return element
