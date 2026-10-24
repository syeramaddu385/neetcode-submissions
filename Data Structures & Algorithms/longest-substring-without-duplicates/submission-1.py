class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques = set()
        l = r = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in uniques:
                uniques.remove(s[l])
                l += 1
            
            w = r - l + 1
            longest = max(longest, w)
            uniques.add(s[r])

        return longest