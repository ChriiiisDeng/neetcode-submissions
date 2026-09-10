class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        

        # find the row

        while top <= bottom:
            r_mid = int((bottom - top) / 2) + top

            if matrix[r_mid][0] > target:
                bottom = r_mid - 1
                continue
            if matrix[r_mid][-1] < target:
                top = r_mid + 1
                continue
            else:
                left,right = 0,len(matrix[0]) - 1
                while left <= right:
                    c_mid = int((right - left) / 2) + left

                    if matrix[r_mid][c_mid] == target:
                        return True
                    elif matrix[r_mid][c_mid] < target:
                        left = c_mid + 1
                    else:
                        right = c_mid - 1
                return False
        return False
        