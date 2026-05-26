class Solution:
    def minWindow(self, s: str, t: str) -> str:

        needed = {}

        for c in t:
            needed[c] = 1 + needed.get(c, 0)
        
        need = len(needed)

        l = 0
        ans = ""
        ans_len = float('inf')
        have = 0
        window = {}

        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in needed and window[char] == needed[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < ans_len:
                    ans = s[l: r+1]
                    ans_len = len(ans)
                
                old_char = s[l]

                if old_char in needed and window[old_char] == needed[old_char]:
                    have -= 1
                
                window[old_char] -= 1
                
                l += 1       

        return ans
