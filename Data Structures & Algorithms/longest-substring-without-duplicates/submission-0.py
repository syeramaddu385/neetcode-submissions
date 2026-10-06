class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        unique = set()
        n = len(s)
        longest = 0

        for r in range(n):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1

            w = r -l + 1
            longest = max(longest, w)
            unique.add(s[r])

        return longest
