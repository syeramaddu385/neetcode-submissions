class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        row = -1

        while l <= r:
            m = (l+r) // 2
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                row = m
                break
    
        return self.binarySearch(matrix[row], target) != -1

    def binarySearch(self, arr: List[int], target: int) -> int:
        l, r = 0, len(arr) - 1
        
        while l <= r:
            m = (l+r) // 2

            if target < arr[m]:
                r = m - 1
            elif target > arr[m]:
                l = m + 1
            else:
                return m

        return -1