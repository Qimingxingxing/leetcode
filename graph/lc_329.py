"""
LeetCode 329: Longest Increasing Path in a Matrix
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Problem:
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 2^31 - 1
"""

from collections import deque
from typing import List

class Solution:
    def longestIncreasingPath_DFS(self, matrix: List[List[int]]) -> int:
        """
        DFS approach with memoization (top-down dynamic programming).
        Time Complexity: O(m * n) where m and n are the dimensions of the matrix.
        Space Complexity: O(m * n) for the memoization cache.
        """
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        memo = {}  # Cache for memoization
        
        def dfs(i: int, j: int) -> int:
            """DFS to find the longest increasing path starting from (i, j)."""
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Check all four directions
            max_length = 1
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                
                # Check if the new position is valid and has a larger value
                if (0 <= ni < m and 0 <= nj < n and 
                    matrix[ni][nj] > matrix[i][j]):
                    max_length = max(max_length, 1 + dfs(ni, nj))
            
            memo[(i, j)] = max_length
            return max_length
        
        # Try starting from each cell
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        
        return result

    def longestIncreasingPath_Topological(self, matrix: List[List[int]]) -> int:
        """
        Topological sort approach using BFS (Kahn's algorithm).
        Time Complexity: O(m * n) where m and n are the dimensions of the matrix.
        Space Complexity: O(m * n) for the queue and in-degree array.
        """
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        
        # Build adjacency list and in-degree count
        graph = {}
        in_degree = {}
        
        # Initialize all cells
        for i in range(m):
            for j in range(n):
                graph[(i, j)] = []
                in_degree[(i, j)] = 0
        
        # Build the graph
        for i in range(m):
            for j in range(n):
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    
                    if (0 <= ni < m and 0 <= nj < n and 
                        matrix[ni][nj] > matrix[i][j]):
                        graph[(i, j)].append((ni, nj))
                        in_degree[(ni, nj)] += 1
        
        # Kahn's algorithm
        queue = deque([(i, j) for i in range(m) for j in range(n) 
                      if in_degree[(i, j)] == 0])
        level = 0
        
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                i, j = queue.popleft()
                
                for ni, nj in graph[(i, j)]:
                    in_degree[(ni, nj)] -= 1
                    if in_degree[(ni, nj)] == 0:
                        queue.append((ni, nj))
            
            level += 1
        
        return level

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Main method - using DFS approach by default.
        Can be changed to Topological sort by calling longestIncreasingPath_Topological instead.
        """
        return self.longestIncreasingPath_DFS(matrix)


def test_solution():
    solution = Solution()
    
    # Test case 1: Example from problem
    matrix1 = [[9,9,4],[6,6,8],[2,1,1]]
    result1 = solution.longestIncreasingPath(matrix1)
    assert result1 == 4
    assert result1 == solution.longestIncreasingPath_DFS(matrix1)
    assert result1 == solution.longestIncreasingPath_Topological(matrix1)
    print("Test case 1 passed: Example from problem")
    
    # Test case 2: Example from problem
    matrix2 = [[3,4,5],[3,2,6],[2,2,1]]
    result2 = solution.longestIncreasingPath(matrix2)
    assert result2 == 4
    print("Test case 2 passed: Example from problem")
    
    # Test case 3: Single cell
    matrix3 = [[1]]
    result3 = solution.longestIncreasingPath(matrix3)
    assert result3 == 1
    print("Test case 3 passed: Single cell")
    
    # Test case 4: All same values
    matrix4 = [[1,1,1],[1,1,1],[1,1,1]]
    result4 = solution.longestIncreasingPath(matrix4)
    assert result4 == 1
    print("Test case 4 passed: All same values")
    
    # Test case 5: Strictly increasing
    matrix5 = [[1,2,3],[4,5,6],[7,8,9]]
    result5 = solution.longestIncreasingPath(matrix5)
    assert result5 == 9
    print("Test case 5 passed: Strictly increasing")
    
    # Test case 6: Strictly decreasing
    matrix6 = [[9,8,7],[6,5,4],[3,2,1]]
    result6 = solution.longestIncreasingPath(matrix6)
    assert result6 == 1
    print("Test case 6 passed: Strictly decreasing")
    
    # Test case 7: Complex case
    matrix7 = [
        [0,1,2,3,4,5,6,7,8,9],
        [19,18,17,16,15,14,13,12,11,10],
        [20,21,22,23,24,25,26,27,28,29],
        [39,38,37,36,35,34,33,32,31,30],
        [40,41,42,43,44,45,46,47,48,49],
        [59,58,57,56,55,54,53,52,51,50],
        [60,61,62,63,64,65,66,67,68,69],
        [79,78,77,76,75,74,73,72,71,70],
        [80,81,82,83,84,85,86,87,88,89],
        [99,98,97,96,95,94,93,92,91,90]
    ]
    result7 = solution.longestIncreasingPath(matrix7)
    assert result7 == 100
    print("Test case 7 passed: Complex case")
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
    
    # Example usage
    solution = Solution()
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    print("Example: matrix =", matrix)
    print("Result:", solution.longestIncreasingPath(matrix)) 