class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []

        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        
        sorted_pairs = sorted(pairs, reverse=True)

        stack = []

        for pos, sp in sorted_pairs:
            time = (target - pos) / sp

            if len(stack) == 0:
                stack.append(time)
            else:
                top = stack[-1]
                if time <= top:
                    pass
                else:
                    stack.append(time)
        
        return len(stack)