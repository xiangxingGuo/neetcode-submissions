class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = [] # index of days are waiting for a warmer temperature

        for i in range(0, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre_index = stack.pop()
                results[pre_index] = i - pre_index
            
            stack.append(i)

        return results
                    