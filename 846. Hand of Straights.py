class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #1 Create a CountMap for all values in hand
        #2 Create a Min Heap to store all unique values
        #3 Use the Min value in the heap to find consecetive numbers.
        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        while minHeap:
            first = minHeap[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
