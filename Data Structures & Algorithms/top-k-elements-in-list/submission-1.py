class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for key in counts.keys():
            count = counts[key]
            buckets[count].append(key)

        results = []
        for bucket in reversed(buckets):
            if len(results) >= k:
                break
                
            if len(bucket) != 0:
                results.extend(bucket)
        
        return results
            
        