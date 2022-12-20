class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        negatives = 0
        if dividend < 0:
            negatives += 1
            dividend = -dividend
        if divisor < 0:
            negatives += 1
            divisor = -divisor
        
        quotient =  0
        while dividend >= divisor:
            power_of_two = 1
            value = divisor

            while value + value < dividend:
                value += value
                power_of_two += power_of_two

            quotient += power_of_two
            dividend -= value
        
        if negatives == 1:
            return -quotient
        else:
            return quotient
