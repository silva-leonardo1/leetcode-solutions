class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix[0]) - 1
        amount = 0

        for i in range(len(matrix)//2):
            for j in range(i, n-i):
                matrix[i][j], matrix[n - j][i] = matrix[n - j][i], matrix[i][j]
                matrix[n-j][i], matrix[n-i][n-j] = matrix[n-i][n-j], matrix[n-j][i]
                matrix[n-i][n-j], matrix[j][n-i] = matrix[j][n-i], matrix[n-i][n-j]



        