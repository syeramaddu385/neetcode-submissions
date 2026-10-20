class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxLength = 0

        for num in nums:
            if num - 1 not in numset:
                cur = num
                count = 1
                while cur + 1 in numset:
                    cur += 1
                    count += 1
                maxLength = max(count, maxLength)

        return maxLength
