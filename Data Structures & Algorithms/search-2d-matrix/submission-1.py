class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        t, b = 0, len(matrix)-1
        while t <= b:
            m = (t + b) // 2
            if target < matrix[m][0]:
                b = m - 1
            elif target > matrix[m][-1]:
                t = m + 1
            else:
                break

        if t > b:
            return False

        row = (t + b) // 2
        l, r = 0, len(matrix[row])-1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[row][m]:
                return True
            
            if matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False

        