class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in checked:
                return [checked[compliment], i]
            else:
                checked[n] = i

