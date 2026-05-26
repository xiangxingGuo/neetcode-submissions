class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque()
        ans = []

        for r in range(len(nums)):
            num = nums[r]

            l = r - k + 1
            while q and q[0] < l:
                q.popleft()

            while len(q) and nums[q[-1]] < num:
                q.pop()
            
            q.append(r)

            if r - k + 1 >= 0:
                ans.append(nums[q[0]])

        return ans
            
            

        