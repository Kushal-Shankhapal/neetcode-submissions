class Solution(object):
    def climbStairs(self, n):
        ways = 0
        ones = n
        twos = 0

        while twos < (n//2):
            twos += 1
            ones -= 2
            ways += int(math.factorial(n - twos) / ((math.factorial(ones)) * (math.factorial(twos))))
        return ways + 1

        # n = 4
        # 1 1 1 1 n! / n! * (0 + 0)!
        # 1 1 2 (n-1)! / (n-2)! * (0 + 1)!
        # 1 2 1
        # 2 1 1
        # 22 

        # n = 5
        # 1 1 1 1 1
        # 1 1 1 2
        # 1 1 2 1
        # 1 2 1 1
        # 2 1 1 1
        # 1 2 2
        # 2 1 2
        # 2 2 1