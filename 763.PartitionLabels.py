class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # T : O(n * 26) so O(n). S : O(26) => O(1)
        # res = [0]
        # count = collections.Counter(s)
        # curSet = set()
        # last = 0
        # for i in range(len(s)):
        #     flag = True
        #     curSet.add(s[i])
        #     count[s[i]] -= 1
        #     for ele in curSet:
        #         if count[ele] > 0:
        #             flag = False
        #     if flag:
        #         res.append(i - last + 1)
        #         last = i + 1
        #         curSet = set()
        # return res[1:]

        # Neetcode Solution
        # T : O(n) && S : O(26) => O(1)
        res = []
        last_occurrence = {}
        for i in range(len(s)):
            last_occurrence[s[i]] = i
        
        size = 0
        end = 0
        for i in range(len(s)):
            end = max(end, last_occurrence[s[i]])
            size += 1

            if i == end:
                res.append(size)
                size = 0
        
        return res
