class Solution:
    # store pairs of (position, speed) and sort them according to position. iterate through those pairs in reverse order. maintain a stack that contains the fleets. If a car can reach the target in the same or less time than the one on the top of the stack then dont add it to the stack. 
    # Return the len of stack after the iteration

    # T:O(nlogn) coz of the sorting
    # S:O(n) stack and pair array
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(position[i], speed[i]) for i in range(len(speed))]
        pair.sort(key = lambda x : x[0])

        for i in range(len(pair) - 1, -1, -1):
            if stack:
                time1 = (target - stack[-1][0]) / stack[-1][1]
                time2 = (target - pair[i][0]) / pair[i][1]

                if time2 <= time1:
                    continue
                else:
                    stack.append((pair[i]))
            else:
                stack.append(pair[i])
            print(stack)
        return len(stack)
