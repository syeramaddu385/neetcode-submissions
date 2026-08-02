class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid

        pivot = l

        if target > nums[-1]:
            lo, hi = 0, pivot - 1
        else:
            lo, hi = pivot, len(nums) - 1
            
        while lo <= hi:
            mid = (lo + hi) // 2

            if target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
            else:
                return mid
            
        return -1