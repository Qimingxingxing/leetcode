"""
LeetCode 200: Number of Islands
https://leetcode.com/problems/number-of-islands/

Problem:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

from collections import deque
from typing import List

class Solution:
    def numIslands_BFS(self, grid: List[List[str]]) -> int:
        """
        BFS approach to count islands.
        Time Complexity: O(m * n) where m and n are the dimensions of the grid.
        Space Complexity: O(min(m, n)) for the queue in worst case.
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        def bfs(i: int, j: int):
            """BFS to mark all connected land cells as visited."""
            queue = deque([(i, j)])
            grid[i][j] = '0'  # Mark as visited
            
            while queue:
                curr_i, curr_j = queue.popleft()
                
                # Check all four directions
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = curr_i + di, curr_j + dj
                    
                    # Check if the new position is valid and is land
                    if (0 <= ni < m and 0 <= nj < n and 
                        grid[ni][nj] == '1'):
                        grid[ni][nj] = '0'  # Mark as visited
                        queue.append((ni, nj))
        
        # Iterate through the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i, j)
        
        return count

    def numIslands_DFS(self, grid: List[List[str]]) -> int:
        """
        DFS approach to count islands.
        Time Complexity: O(m * n) where m and n are the dimensions of the grid.
        Space Complexity: O(m * n) for the recursion stack in worst case.
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        def dfs(i: int, j: int):
            """DFS to mark all connected land cells as visited."""
            # Check if the position is valid and is land
            if (i < 0 or i >= m or j < 0 or j >= n or 
                grid[i][j] == '0'):
                return
            
            grid[i][j] = '0'  # Mark as visited
            
            # Explore all four directions
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(i + di, j + dj)
        
        # Iterate through the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        
        return count

    def numIslands_UnionFind(self, grid: List[List[str]]) -> int:
        """
        Union-Find approach to count islands.
        Time Complexity: O(m * n * α(m*n)) where α is the inverse Ackermann function.
        Space Complexity: O(m * n) for the parent array.
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        # Initialize Union-Find
        parent = list(range(m * n))
        rank = [0] * (m * n)
        
        def find(x: int) -> int:
            """Find the root of the set containing x."""
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int):
            """Union the sets containing x and y."""
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return
            
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
        
        # Process the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    curr = i * n + j
                    
                    # Check all four directions
                    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        ni, nj = i + di, j + dj
                        
                        if (0 <= ni < m and 0 <= nj < n and 
                            grid[ni][nj] == '1'):
                            neighbor = ni * n + nj
                            union(curr, neighbor)
        
        # Count unique roots
        islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands.add(find(i * n + j))
        
        return len(islands)

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Main method - using BFS approach by default.
        Can be changed to DFS or Union-Find by calling the respective methods.
        """
        return self.numIslands_BFS(grid)


def test_solution():
    solution = Solution()
    
    # Test case 1: Example from problem
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    result1 = solution.numIslands(grid1)
    assert result1 == 1
    assert result1 == solution.numIslands_BFS(grid1)
    assert result1 == solution.numIslands_DFS(grid1)
    assert result1 == solution.numIslands_UnionFind(grid1)
    print("Test case 1 passed: Example from problem")
    
    # Test case 2: Multiple islands
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    result2 = solution.numIslands(grid2)
    assert result2 == 3
    print("Test case 2 passed: Multiple islands")
    
    # Test case 3: No islands
    grid3 = [
        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]
    ]
    result3 = solution.numIslands(grid3)
    assert result3 == 0
    print("Test case 3 passed: No islands")
    
    # Test case 4: Single cell island
    grid4 = [["1"]]
    result4 = solution.numIslands(grid4)
    assert result4 == 1
    print("Test case 4 passed: Single cell island")
    
    # Test case 5: Single cell water
    grid5 = [["0"]]
    result5 = solution.numIslands(grid5)
    assert result5 == 0
    print("Test case 5 passed: Single cell water")
    
    # Test case 6: Diagonal islands (should be separate)
    grid6 = [
        ["1","0","1"],
        ["0","1","0"],
        ["1","0","1"]
    ]
    result6 = solution.numIslands(grid6)
    assert result6 == 5
    print("Test case 6 passed: Diagonal islands")
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
    
    # Example usage
    solution = Solution()
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print("Example: grid =", grid)
    print("Result:", solution.numIslands(grid)) 