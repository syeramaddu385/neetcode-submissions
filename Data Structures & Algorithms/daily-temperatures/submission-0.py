class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack =[] #monotonic stack

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                warmerInd = stack.pop()
                res[warmerInd] = i - warmerInd
            stack.append(i)
        
        return res