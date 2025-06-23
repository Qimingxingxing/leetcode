"""
LeetCode 210: Course Schedule II
https://leetcode.com/problems/course-schedule-ii/

Problem:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
you must take course bi first if you want to take course ai.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty list.

Example 1:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3] or [0,1,2,3]

Example 2:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder_BFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        BFS approach using Kahn's algorithm for topological sorting.
        Returns a valid order if possible, otherwise an empty list.
        """
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return order if len(order) == numCourses else []

    def findOrder_DFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        DFS approach for topological sorting with cycle detection.
        Returns a valid order if possible, otherwise an empty list.
        """
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        visited = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited
        order = []
        def dfs(node):
            if visited[node] == 1:
                return False  # cycle
            if visited[node] == 2:
                return True
            visited[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2
            order.append(node)
            return True
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []
        return order[::-1]

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Main method - using BFS approach by default.
        Can be changed to DFS by calling findOrder_DFS instead.
        """
        return self.findOrder_BFS(numCourses, prerequisites)


def test_solution():
    solution = Solution()
    # Test case 1: Example from problem
    numCourses1 = 4
    prerequisites1 = [[1,0],[2,0],[3,1],[3,2]]
    result1 = solution.findOrder(numCourses1, prerequisites1)
    assert set(result1) == set([0,1,2,3]) and result1.index(0) < result1.index(1) and result1.index(0) < result1.index(2) and result1.index(1) < result1.index(3) and result1.index(2) < result1.index(3)
    assert result1 == solution.findOrder_BFS(numCourses1, prerequisites1)
    assert result1 == solution.findOrder_DFS(numCourses1, prerequisites1)
    print("Test case 1 passed: Example from problem")
    # Test case 2: Single course
    numCourses2 = 1
    prerequisites2 = []
    result2 = solution.findOrder(numCourses2, prerequisites2)
    assert result2 == [0]
    print("Test case 2 passed: Single course")
    # Test case 3: Impossible (cycle)
    numCourses3 = 2
    prerequisites3 = [[1,0],[0,1]]
    result3 = solution.findOrder(numCourses3, prerequisites3)
    assert result3 == []
    print("Test case 3 passed: Impossible (cycle)")
    # Test case 4: No prerequisites
    numCourses4 = 3
    prerequisites4 = []
    result4 = solution.findOrder(numCourses4, prerequisites4)
    assert set(result4) == set([0,1,2])
    print("Test case 4 passed: No prerequisites")
    # Test case 5: Complex case
    numCourses5 = 6
    prerequisites5 = [[1,0],[2,1],[3,2],[4,2],[5,3],[5,4]]
    result5 = solution.findOrder(numCourses5, prerequisites5)
    assert set(result5) == set([0,1,2,3,4,5])
    print("Test case 5 passed: Complex case")
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
    # Example usage
    solution = Solution()
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print("Example: numCourses =", numCourses, ", prerequisites =", prerequisites)
    print("Order:", solution.findOrder(numCourses, prerequisites)) 