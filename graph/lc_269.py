"""
LeetCode 269: Alien Dictionary
https://leetcode.com/problems/alien-dictionary/

Problem:
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
"""

from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder_BFS(self, words: List[str]) -> str:
        """
        BFS approach using Kahn's algorithm for topological sorting.
        Time Complexity: O(C) where C is the total number of characters in all words.
        Space Complexity: O(1) since there are at most 26 characters.
        """
        # Build adjacency list and in-degree count
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        
        # Initialize all characters that appear in words
        for word in words:
            for char in word:
                in_degree[char] = 0
        
        # Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            
            # Check if word2 is a prefix of word1 (invalid case)
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            
            # Find the first different character
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break
        
        # Kahn's algorithm
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []
        
        while queue:
            char = queue.popleft()
            result.append(char)
            
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if we have a valid topological order
        return "".join(result) if len(result) == len(in_degree) else ""

    def alienOrder_DFS(self, words: List[str]) -> str:
        """
        DFS approach for topological sorting with cycle detection.
        Time Complexity: O(C) where C is the total number of characters in all words.
        Space Complexity: O(1) since there are at most 26 characters.
        """
        # Build adjacency list
        graph = defaultdict(set)
        
        # Initialize all characters that appear in words
        chars = set()
        for word in words:
            for char in word:
                chars.add(char)
        
        # Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            
            # Check if word2 is a prefix of word1 (invalid case)
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            
            # Find the first different character
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break
        
        # DFS with cycle detection
        visited = {}  # 0=unvisited, 1=visiting, 2=visited
        result = []
        
        def dfs(char):
            if char in visited:
                if visited[char] == 1:  # Cycle detected
                    return False
                if visited[char] == 2:  # Already processed
                    return True
            
            visited[char] = 1  # Mark as visiting
            
            for neighbor in graph[char]:
                if not dfs(neighbor):
                    return False
            
            visited[char] = 2  # Mark as visited
            result.append(char)
            return True
        
        # Process all characters
        for char in chars:
            if char not in visited:
                if not dfs(char):
                    return ""
        
        return "".join(result[::-1])  # Reverse to get correct order

    def alienOrder(self, words: List[str]) -> str:
        """
        Main method - using BFS approach by default.
        Can be changed to DFS by calling alienOrder_DFS instead.
        """
        return self.alienOrder_BFS(words)


def test_solution():
    solution = Solution()
    
    # Test case 1: Example from problem
    words1 = ["wrt","wrf","er","ett","rftt"]
    result1 = solution.alienOrder(words1)
    assert result1 == "wertf"
    assert result1 == solution.alienOrder_BFS(words1)
    assert result1 == solution.alienOrder_DFS(words1)
    print("Test case 1 passed: Example from problem")
    
    # Test case 2: Simple case
    words2 = ["z","x"]
    result2 = solution.alienOrder(words2)
    assert result2 == "zx"
    print("Test case 2 passed: Simple case")
    
    # Test case 3: Invalid case (cycle)
    words3 = ["z","x","z"]
    result3 = solution.alienOrder(words3)
    assert result3 == ""
    print("Test case 3 passed: Invalid case (cycle)")
    
    # Test case 4: Invalid case (prefix)
    words4 = ["abc","ab"]
    result4 = solution.alienOrder(words4)
    assert result4 == ""
    print("Test case 4 passed: Invalid case (prefix)")
    
    # Test case 5: Single word
    words5 = ["abc"]
    result5 = solution.alienOrder(words5)
    assert result5 == "abc"
    print("Test case 5 passed: Single word")
    
    # Test case 6: Empty list
    words6 = []
    result6 = solution.alienOrder(words6)
    assert result6 == ""
    print("Test case 6 passed: Empty list")
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
    
    # Example usage
    solution = Solution()
    words = ["wrt","wrf","er","ett","rftt"]
    print("Example: words =", words)
    print("Result:", solution.alienOrder(words)) 