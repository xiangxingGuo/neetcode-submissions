class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum()).lower()

        length = len(s)

        if length == 1:
            return True

        i = 0
        j = length - 1

        while i < j:
            left_value = s[i]
            right_value = s[j]

            if left_value != right_value:
                return False
            
            i += 1
            j -= 1
        
        return True