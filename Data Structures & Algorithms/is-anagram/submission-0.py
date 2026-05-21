class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0 for i in range(26)]

        for s_ in s:
            index = int(ord(s_) - ord('a'))
            counts[index] += 1
        
        for t_ in t:
            index = int(ord(t_) - ord('a'))
            counts[index] -= 1
        
        if all(count == 0 for count in counts):
            return True
        
        return False
        