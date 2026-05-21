class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for one_str in strs:
            counts = [0] * 26
            for one_char in one_str:
                index = int(ord(one_char) - ord('a'))
                counts[index] += 1
            
            key = tuple(counts)

            if key not in groups:
                groups[key] = [one_str]
            else:
                groups[key].append(one_str)
        
        return list(groups.values())