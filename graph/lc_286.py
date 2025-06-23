"""
LeetCode 286: Walls and Gates
https://leetcode.com/problems/walls-and-gates/

Problem:
You are given an m x n grid rooms initialized with these three possible values:
- -1 A wall or an obstacle.
- 0 A gate.
- INF Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example 1:
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Example 2:
Input: rooms = [[-1]]
Output: [[-1]]

Constraints:
m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 2^31 - 1.
"""

from collections import deque
from typing import List

class Solution:
    def wallsAndGates_BFS(self, rooms: List[List[int]]) -> None:
        """
        BFS approach starting from all gates simultaneously.
        Time Complexity: O(m * n) where m and n are the dimensions of the grid.
        Space Complexity: O(m * n) for the queue in worst case.
        """
        if not rooms or not rooms[0]:
            return
        
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        
        # Find all gates and add them to the queue
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))
        
        # BFS from all gates
        while queue:
            i, j, distance = queue.popleft()
            
            # Check all four directions
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                
                # Check if the new position is valid and is an empty room
                if (0 <= ni < m and 0 <= nj < n and 
                    rooms[ni][nj] == 2147483647):
                    rooms[ni][nj] = distance + 1
                    queue.append((ni, nj, distance + 1))

    def wallsAndGates_DFS(self, rooms: List[List[int]]) -> None:
        """
        DFS approach starting from all gates.
        Time Complexity: O(m * n) where m and n are the dimensions of the grid.
        Space Complexity: O(m * n) for the recursion stack in worst case.
        """
        if not rooms or not rooms[0]:
            return
        
        m, n = len(rooms), len(rooms[0])
        
        def dfs(i: int, j: int, distance: int):
            # Check if the position is valid and the current distance is better
            if (i < 0 or i >= m or j < 0 or j >= n or 
                rooms[i][j] < distance):
                return
            
            rooms[i][j] = distance
            
            # Explore all four directions
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(i + di, j + dj, distance + 1)
        
        # Start DFS from all gates
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Main method - using BFS approach by default.
        Can be changed to DFS by calling wallsAndGates_DFS instead.
        """
        self.wallsAndGates_BFS(rooms)


def test_solution():
    solution = Solution()
    
    # Test case 1: Example from problem
    rooms1 = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647]
    ]
    expected1 = [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4]
    ]
    solution.wallsAndGates(rooms1)
    assert rooms1 == expected1
    print("Test case 1 passed: Example from problem")
    
    # Test case 2: Single wall
    rooms2 = [[-1]]
    expected2 = [[-1]]
    solution.wallsAndGates(rooms2)
    assert rooms2 == expected2
    print("Test case 2 passed: Single wall")
    
    # Test case 3: Single gate
    rooms3 = [[0]]
    expected3 = [[0]]
    solution.wallsAndGates(rooms3)
    assert rooms3 == expected3
    print("Test case 3 passed: Single gate")
    
    # Test case 4: All empty rooms
    rooms4 = [
        [2147483647, 2147483647],
        [2147483647, 2147483647]
    ]
    expected4 = [
        [2147483647, 2147483647],
        [2147483647, 2147483647]
    ]
    solution.wallsAndGates(rooms4)
    assert rooms4 == expected4
    print("Test case 4 passed: All empty rooms")
    
    # Test case 5: Gate in corner
    rooms5 = [
        [0, 2147483647],
        [2147483647, 2147483647]
    ]
    expected5 = [
        [0, 1],
        [1, 2]
    ]
    solution.wallsAndGates(rooms5)
    assert rooms5 == expected5
    print("Test case 5 passed: Gate in corner")
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
    
    # Example usage
    solution = Solution()
    rooms = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647]
    ]
    print("Example: rooms =", rooms)
    solution.wallsAndGates(rooms)
    print("Result:", rooms) 