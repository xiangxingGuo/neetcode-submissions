class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)

        i = 0
        j = length -1

        while i < j:
            left = numbers[i]
            right = numbers[j]

            cur_sum = left + right

            if cur_sum == target:
                return [i + 1, j + 1] # 1-index
            
            elif cur_sum > target:
                j -= 1
            
            elif cur_sum < target:
                i += 1

        