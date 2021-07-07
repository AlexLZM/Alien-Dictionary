# Alien Dictionary

### Problem Description
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

 

### Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
### Example 2:

Input: words = ["z","x"]
Output: "zx"
### Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
 

### Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.

### My Strategy

Construct a graph as a representation of the order relationships of the letters and do topological sort.

1. Initiate dictionaries as data structure for the graph;
2. Parse the list of words and construct gragh;
3. Pick letters with 0 indegree as start points to sort into stack;
4. pick the current letter from stack and add to the result string;
5. decrease 1 indegree for all children, add to stack if indegree is 0;
6. delete the current letter from graph.
7. repeat 4 - 6 






