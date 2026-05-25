class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        r = 0
        ans = 0

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1

            window_length = r - l + 1

            if window_length - max(count.values()) <= k:
                ans = max(ans, window_length)
            else:
                count[s[l]] -= 1
                l += 1
            
            r += 1
        
        return ans

