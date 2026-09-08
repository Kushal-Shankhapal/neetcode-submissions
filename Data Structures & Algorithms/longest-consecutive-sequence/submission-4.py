class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sub_count = 0 if len(nums) == 0 else 1
        sub_count = 1
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                sub_count += 1
                max_sub_count = max(max_sub_count, sub_count)
            elif nums[i + 1] == nums[i]:
                pass
            else:
                sub_count = 1
        return max_sub_count