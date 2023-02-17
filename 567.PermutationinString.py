class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        l = len(s1)

        for i in range(len(s2)):
            if s2[i] in s1_count:
                s1_count[s2[i]] -= 1
            if i >= l and s2[i-l] in s1_count:
                s1_count[s2[i-l]] += 1

            if all(value == 0 for value in s1_count.values()):
                return True

        return False

