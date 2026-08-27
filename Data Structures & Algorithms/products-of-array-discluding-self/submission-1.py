class Solution(object):
    def productExceptSelf(self, nums):
        prod = 1

        for n in nums:
            if n != 0:
                prod *= n

        if nums.count(0) > 1:
            ans = [0] * len(nums)
        elif nums.count(0) == 1:
            ans = [0] * len(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    ans[i] = prod
        else:
            ans = [prod] * len(nums)
            for i in range(len(nums)):
                ans[i] = int(ans[i] / nums[i])
        return ans