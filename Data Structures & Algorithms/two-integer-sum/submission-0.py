class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index in range(len(nums)):
            current_value = nums[index]
            completion = target - current_value

            if completion not in seen:
                seen[current_value] = index
            else:
                return [seen[completion], index]
        