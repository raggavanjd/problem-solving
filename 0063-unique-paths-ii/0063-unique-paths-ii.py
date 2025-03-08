class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[M-1][N-1] == 1:
            return 0
        
        memo = {}
        
        def backtrack(i, j):
            if i >= M or j >= N:
                return 0
            
            if obstacleGrid[i][j] == 1:
                return 0
            
            if i == M - 1 and j == N - 1:
                return 1
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = backtrack(i + 1, j) + backtrack(i, j + 1)
            return memo[(i, j)]
        
        return backtrack(0, 0)