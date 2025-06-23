"""
LeetCode 207: Course Schedule
https://leetcode.com/problems/course-schedule/

Problem:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
you must take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should 
also have finished course 1. So it is impossible.

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
    def canFinish_DFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        DFS approach using topological sorting with cycle detection.
        
        Time Complexity: O(V + E) where V is number of courses and E is number of prerequisites
        Space Complexity: O(V + E) for adjacency list and recursion stack
        """
        # Build adjacency list
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # States: 0 = unvisited, 1 = visiting (in recursion stack), 2 = visited
        visited = [0] * numCourses
        
        def has_cycle(course):
            if visited[course] == 1:  # Found a cycle
                return True
            if visited[course] == 2:  # Already processed
                return False
            
            visited[course] = 1  # Mark as visiting
            
            # Check all neighbors
            for neighbor in graph[course]:
                if has_cycle(neighbor):
                    return True
            
            visited[course] = 2  # Mark as visited
            return False
        
        # Check for cycles starting from each unvisited course
        for course in range(numCourses):
            if visited[course] == 0 and has_cycle(course):
                return False
        
        return True
    
    def canFinish_BFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        BFS approach using Kahn's algorithm (topological sorting).
        
        Time Complexity: O(V + E) where V is number of courses and E is number of prerequisites
        Space Complexity: O(V + E) for adjacency list and queue
        """
        # Build adjacency list and in-degree count
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Add all courses with 0 in-degree to queue
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
        courses_completed = 0
        
        while queue:
            course = queue.popleft()
            courses_completed += 1
            
            # Reduce in-degree for all neighbors
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If we can complete all courses, there's no cycle
        return courses_completed == numCourses
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Main method - using DFS approach by default.
        Can be changed to BFS by calling canFinish_BFS instead.
        """
        return self.canFinish_DFS(numCourses, prerequisites)


def test_solution():
    """Test cases for the Course Schedule problem."""
    solution = Solution()
    
    # Test case 1: Simple case - possible
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    assert solution.canFinish(numCourses1, prerequisites1) == True
    assert solution.canFinish_BFS(numCourses1, prerequisites1) == True
    print("Test case 1 passed: Simple case - possible")
    
    # Test case 2: Cycle detected - impossible
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    assert solution.canFinish(numCourses2, prerequisites2) == False
    assert solution.canFinish_BFS(numCourses2, prerequisites2) == False
    print("Test case 2 passed: Cycle detected - impossible")
    
    # Test case 3: No prerequisites
    numCourses3 = 3
    prerequisites3 = []
    assert solution.canFinish(numCourses3, prerequisites3) == True
    assert solution.canFinish_BFS(numCourses3, prerequisites3) == True
    print("Test case 3 passed: No prerequisites")
    
    # Test case 4: Complex case - possible
    numCourses4 = 4
    prerequisites4 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    assert solution.canFinish(numCourses4, prerequisites4) == True
    assert solution.canFinish_BFS(numCourses4, prerequisites4) == True
    print("Test case 4 passed: Complex case - possible")
    
    # Test case 5: Complex case with cycle - impossible
    numCourses5 = 4
    prerequisites5 = [[1, 0], [2, 1], [3, 2], [1, 3]]
    assert solution.canFinish(numCourses5, prerequisites5) == False
    assert solution.canFinish_BFS(numCourses5, prerequisites5) == False
    print("Test case 5 passed: Complex case with cycle - impossible")
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
    
    # Example usage
    solution = Solution()
    
    # Example 1
    numCourses = 2
    prerequisites = [[1, 0]]
    result = solution.canFinish(numCourses, prerequisites)
    print(f"Example 1: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Result: {result}")
    print()
    
    # Example 2
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    result = solution.canFinish(numCourses, prerequisites)
    print(f"Example 2: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Result: {result}") 