from typing import List

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        col_maxes = [0] * n 
        for j in range(n):
            current_col_max = -1
            for i in range(m):
                current_col_max = max(current_col_max, matrix[i][j])
            col_maxes[j] = current_col_max
        
        answer = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    answer[i][j] = col_maxes[j]
                else:
                    answer[i][j] = matrix[i][j]
        
        return answer