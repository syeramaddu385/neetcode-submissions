class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fixed window size because the len is fixed
        if len(s1) > len(s2):
            return False
            
        s1_count = {}

        for c in s1:
            s1_count[c] = 1 + s1_count.get(c, 0)

        window_count = {}

        for i in range(len(s1)):
            window_count[s2[i]] = 1 + window_count.get(s2[i], 0)

        if window_count == s1_count:
            return True

        for r in range(len(s1), len(s2)):
            window_count[s2[r]] = 1 + window_count.get(s2[r], 0)

            l = r - len(s1)

            window_count[s2[l]] -= 1
            if window_count[s2[l]] == 0:
                del window_count[s2[l]]

            if window_count == s1_count:
                return True

        return False
                


            
