class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search rows for row
        t, b = 0, len(matrix)-1
        while t <= b:
            m = (t+b) // 2
            if target < matrix[m][0]:
                b = m-1
            elif target > matrix[m][-1]:
                t = m+1
            else:
                break
        
        if t > b:
            return False
        
        row = (t+b) // 2
        l, r = 0, len(matrix[row])-1
        while l <= r:
            m = (l+r) // 2
            if target == matrix[row][m]:
                return True
            
            if target < matrix[row][m]:
                r = m-1
            else:
                l = m+1
        return False