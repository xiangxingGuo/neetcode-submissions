class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        best_rate = max(piles)
        best_time = sum([(pile + best_rate - 1) // best_rate for pile in piles])

        while left <= right:
            mid  = (left + right) // 2

            times = sum([(pile + mid - 1) // mid  for pile in piles])

            if times <= h:
                best_rate = mid
                best_time = times


                right = mid -1
            elif times > h:
                left = mid + 1
            
        return best_rate