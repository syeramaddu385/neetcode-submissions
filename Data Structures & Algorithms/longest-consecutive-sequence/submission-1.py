class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        distinct_elems = set(nums)

        for num in distinct_elems:
            if num - 1 in distinct_elems:
                continue
            else:
                streak = 1
                while num + 1 in distinct_elems:
                    streak += 1
                    num += 1
            max_count = max(streak, max_count)
        
        return max_count

        