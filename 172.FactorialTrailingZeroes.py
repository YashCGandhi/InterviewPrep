class Solution:
    def trailingZeroes(self, n: int) -> int:
        # O(n^2)
        """
        fact = 1
        count = 0
        for i in range(1,n+1):
            fact = i * fact

        while fact % 10 == 0:
            count += 1
            fact //= 10
        
        return count
        """
        # O(n)
        # fives = 0
        # for i in range(1, n + 1):
        #     rem = i
        #     while rem % 5 == 0:
        #         rem //= 5
        #         fives += 1
        # return fives


        # O(log(n))
        zero_count = 0
        curr_multiple = 5
        while n >= curr_multiple:
            zero_count += n // curr_multiple
            curr_multiple *= 5
        return zero_count
