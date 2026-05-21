class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        
        for index in range(len(nums)):
            prefix = 1
            for j in range(0, index):
                prefix = prefix * nums[j]        
            
            for j in range(index+1, len(nums)):
                prefix = prefix * nums[j]
            results.append(prefix)
        
        return results