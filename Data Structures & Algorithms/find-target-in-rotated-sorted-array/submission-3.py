class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            else:
                # left is sorted?
                if nums[left] <= nums[mid]: # sorted
                    # check target whether in sorted left
                    if nums[left] <=  target and target <= nums[mid]: # in sorted left part
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if nums[mid] <= target and target <= nums[right]: # in sorted right part
                        left = mid + 1
                    else:
                        right = mid - 1
        
        return -1