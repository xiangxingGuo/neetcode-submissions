class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)

        results = []

        i = 0

        while i < len(sorted_nums) - 2:
            
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                i += 1
                continue
            

            j = i + 1
            k = len(sorted_nums) - 1
            while j < k:
                cur_sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]

                if cur_sum == 0:
                    results.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
                    k -= 1

                    while j < k and sorted_nums[j] == sorted_nums[j - 1]:
                        j += 1

                elif cur_sum > 0:
                    k -= 1
                elif cur_sum < 0:
                    j += 1
            
            i += 1
        
        return results
