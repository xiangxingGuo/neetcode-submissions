class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1 for num in nums]
        
        prefix = 1
        for index in range(len(nums)):
            results[index] = prefix
            prefix *= nums[index]
        
        postfix = 1
        for index in range(len(nums) -1 , -1, -1):
            results[index] *= postfix
            postfix *= nums[index]

        return results