class Solution:

    def encode(self, strs: List[str]) -> str:
        results = ""
        for one_str in strs:
            length = len(one_str)
            results += str(length)
            results += "#"
            results += one_str
        
        return results

    def decode(self, s: str) -> List[str]:
        results = []
        
        index = 0
        digs = ""
        while index < len(s):
            if s[index] != "#":
                digs += s[index]
                index += 1
            else:
                length = int(digs)
                one_str = s[index + 1: index + 1 + length]
                results.append(one_str)
                index += (1 + length)

                digs = ""
        return results

            
