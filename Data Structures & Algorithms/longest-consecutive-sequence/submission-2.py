class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        nums = set(nums)

        longest = 0
        candidates = []
        
        for num in nums:
            length = 0
            if num - 1 in nums:
                pass
                
            else:
                max_index = len(nums)
                for j in range(0, max_index):
                    if num + j in nums:
                        length += 1
                    else:
                        break
                
                longest = max(length, longest)
            
        return longest