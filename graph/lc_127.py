"""
LeetCode 127: Word Ladder
https://leetcode.com/problems/word-ladder/

Problem:
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, there is no valid transformation sequence.

Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""

from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength_BFS(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        BFS approach to find the shortest transformation sequence.
        Time Complexity: O(N * L * 26) where N is the number of words and L is the length of each word.
        Space Complexity: O(N) for the queue.
        """
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)
        queue = deque([beginWord])
        level = 1
        
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                word = queue.popleft()
                
                if word == endWord:
                    return level
                
                # Try changing each character in the word
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        
                        if newWord in wordSet:
                            wordSet.remove(newWord)  # Remove from set to mark as visited
                            queue.append(newWord)
            
            level += 1
        
        return 0

    def ladderLength_Bidirectional_BFS(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Bidirectional BFS approach for better performance.
        Time Complexity: O(N * L * 26) but with better average case performance.
        Space Complexity: O(N) for the queues and visited sets.
        """
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)
        beginSet = set([beginWord])
        endSet = set([endWord])
        visited = set()
        level = 1
        
        while beginSet and endSet:
            # Always work on the smaller set for better performance
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            
            nextSet = set()
            
            for word in beginSet:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        
                        if newWord in endSet:
                            return level + 1
                        
                        if newWord in wordSet and newWord not in visited:
                            visited.add(newWord)
                            nextSet.add(newWord)
            
            beginSet = nextSet
            level += 1
        
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Main method - using BFS approach by default.
        Can be changed to Bidirectional BFS by calling ladderLength_Bidirectional_BFS instead.
        """
        return self.ladderLength_BFS(beginWord, endWord, wordList)


def test_solution():
    solution = Solution()
    
    # Test case 1: Example from problem
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    result1 = solution.ladderLength(beginWord1, endWord1, wordList1)
    assert result1 == 5
    assert result1 == solution.ladderLength_BFS(beginWord1, endWord1, wordList1)
    assert result1 == solution.ladderLength_Bidirectional_BFS(beginWord1, endWord1, wordList1)
    print("Test case 1 passed: Example from problem")
    
    # Test case 2: Impossible case
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    result2 = solution.ladderLength(beginWord2, endWord2, wordList2)
    assert result2 == 0
    print("Test case 2 passed: Impossible case")
    
    # Test case 3: Same word
    beginWord3 = "hit"
    endWord3 = "hit"
    wordList3 = ["hot","dot","dog","lot","log","cog"]
    result3 = solution.ladderLength(beginWord3, endWord3, wordList3)
    assert result3 == 1
    print("Test case 3 passed: Same word")
    
    # Test case 4: Direct transformation
    beginWord4 = "hit"
    endWord4 = "hot"
    wordList4 = ["hot","dot","dog","lot","log","cog"]
    result4 = solution.ladderLength(beginWord4, endWord4, wordList4)
    assert result4 == 2
    print("Test case 4 passed: Direct transformation")
    
    # Test case 5: Complex case
    beginWord5 = "hit"
    endWord5 = "dog"
    wordList5 = ["hot","dot","dog","lot","log","cog"]
    result5 = solution.ladderLength(beginWord5, endWord5, wordList5)
    assert result5 == 4
    print("Test case 5 passed: Complex case")
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
    
    # Example usage
    solution = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print("Example: beginWord =", beginWord, ", endWord =", endWord, ", wordList =", wordList)
    print("Result:", solution.ladderLength(beginWord, endWord, wordList)) 