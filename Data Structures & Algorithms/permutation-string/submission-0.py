class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_dict = {}

        for c in s1:
            target_dict[c] = target_dict.get(c, 0) + 1
        
        l = 0
        r = len(s1) - 1

        while r < len(s2):
            window = s2[l:r+1]
            window_dict = {}

            for c in window:
                window_dict[c] = window_dict.get(c, 0) + 1
            
            if window_dict == target_dict:
                return True
                
            l += 1
            r += 1

        return False