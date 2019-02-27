## Longest common substring 

- DP

重点在于如何构造递归的式子，即利用已存储的情况来预测未知的情况. 另外学到 *suffix table* 

```python
class Solution:
    def __init__(self):
        self.s1 = 'OldSite:GeeksforGeeks.org'
        self.s2 = 'NewSite:GeeksQuiz.com'

    def longest_common_string(self):
        m = len(self.s1)
        n = len(self.s2)
        suffix = [[0 for k in range(n+1)] for l in range(m+1)]
        result = 0

        for i in range(m + 1):
            for j in range(n + 1):
                if (i == 0 or j == 0):
                    suffix[i][j] = 0
                elif self.s1[i - 1] == self.s2[j - 1]:
                    suffix[i][j] = suffix[i-1][j-1] + 1
                    result = max(result, suffix[i][j])
                else:
                    suffix[i][j] = 0
        return result

```



## Longest Palindromic Substring

- Brute Force

```python
class Solution:
    def __init__(self):
        self.test = "abcfghejacjaa"

    def isPalindrome(self, s):
        length = int(len(s)/2)
        for i in range(length):
            if s[i] == s[len(s) - i - 1]:
                continue
            else:
                return False
        return True

    def longestPalindrome(self):
        """
        :type s: str
        :rtype: str
        """
        s = self.test
        if len(s) == 0:
            return ''
        else:
            longest_length = 1
            longest_Palin = s[0]
            for i in range(len(s)):
                for j in range(i,len(s)):
                    if self.isPalindrome(s[i:j+1]):
                        if j-i+1 > longest_length:
                            longest_length = j - i + 1
                            longest_Palin = s[i:j+1]
        return longest_Palin
```

- DP

```python
class Solution:
    def __init__(self):
        self.test = "forgeeksskeegfor"

    def longestPalindrome(self):
        """
        :type s: str
        :rtype: str
        """
        s = self.test
        m = len(s)
        if m == 0:
            return ''

        suffix = [[0 for i in range(m)] for j in range(m)]
        start = 0
        maxLength = 1

        # Check for substring of length 1
        for i in range(m):
            suffix[i][i] = True
            start = i
            maxLength = 1

        # Check for substring of length 2
        for i in range(m - 1):
            if s[i] == s[i + 1]:
                suffix[i][i + 1] = True
                start = i
                maxLength = 2

        # Check for substring of length >= 3
        k = 3
        while (k < m):
            i = 0
            while (i < m - k +1):
                j = i + k - 1
                if (suffix[i + 1][j - 1] and
                        s[i] == s[j]):
                    suffix[i][j] = True

                    if (k > maxLength):
                        start = i
                        maxLength = k
                i = i + 1
            k = k + 1

        print("Longest palindrome substring is: ", s[start : start + maxLength])
        return maxLength
```

- Expand around center

回文数的一个重要特征在于可以从中间往两侧展开

```python
class Solution:
    def __init__(self):
        self.test = "ab"

    def longestPalindrome(self):
        """
        :type s: str
        :rtype: str
        """
        s = self.test
        maxLength = 1

        start = 0
        length = len(s)

        low = 0
        high = 0
        for i in range(1, length):
            # Find the longest even length palindrome with center
            # points as i-1 and i.
            low = i - 1
            high = i
            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 > maxLength:
                    start = low
                    maxLength = high - low + 1
                low -= 1
                high += 1

            # Find the longest odd length palindrome with center
            # point as i
            low = i - 1
            high = i + 1
            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 > maxLength:
                    start = low
                    maxLength = high - low + 1
                low -= 1
                high += 1

        print("Longest palindrome substring is:" + s[start:start + maxLength]),

        return maxLength
```



## Median of Two Sorted Arrays

解题思路：求中位数即找到一个划分，似的集合A和B满足二者所含元素数量相同，并且A最大的数小于B最小的数.

```python
class Solution:
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # n>=m 
        m, n = len(A),len(B)
        if n<m:
            A, B, m, n = B, A, n, m
        
        imin, imax, halfLen = 0, m, (m+n+1)/2
        while(imin <= imax):
            i = int((imin+imax)/2)
            j = int(halfLen)-i
            if i > 0 and A[i-1] > B[j]:
                imax = i - 1
            elif i < m and A[i] < B[j-1]:
                imin = i + 1
            else:
                # i is perfect
                if i==0:
                    maxLeft = B[j-1]
                elif j==0:
                    maxLeft = A[i-1]
                else:
                    maxLeft = max(A[i-1], B[j-1])
                
                if (m+n) % 2 == 1:
                    return maxLeft
                else:
                    if i==m:
                        minRight = B[j]
                    elif j==n:
                        minRight = A[i]
                    else:
                        minRight = min(B[j],A[i])
                return (maxLeft+minRight)/2
```



### Container With Most Water

解题思路：*Two Pointer Approach*

```python
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r,_maxs = 0,len(height) - 1,0
        while l < r:
        	_maxs = max((r - l) * min(height[l],height[r]),_maxs)
        	if height[l] < height[r]:
        		l += 1
        	else:
        		r -= 1
        return _maxs
```

### Regular Expression Matching

- Recursion

如果正则表达式中不存在 * ,那么问题会变得很简单. 如果在匹配时遇到了 * ,则利用递归思想处理. 

```python
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))

        else:
            return first_match and self.isMatch(s[1:], p[1:])
```

- DP

```python
class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
```

## Generate Parentheses

题目叙述：Given *n* pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

- Backtracking

```python
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(S='', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
            if left < n:
                backtrack(S + '(', left+1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)
        backtrack()

        return ans
```

- Closure Number

利用递归的思想

```python
class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in xrange(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
```

### Valid Sudoku

题目叙述: Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**(数独)

```python
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        def check_lines(board):
            for i in range(len(board)):
                horiz = set()
                vert = set()
                for j in range(len(board[0])):
                    if board[i][j] in horiz or board[j][i] in vert:
                        return False
                    
                    if not board[i][j] == '.':
                        horiz.add(board[i][j])
                    if not board[j][i] == '.':
                        vert.add(board[j][i])
            return True
        
        def check_box(board):
            for x3 in range(0,len(board),3):
                for y3 in range(0,len(board[0]),3):
                    s = set()
                    for i in range(3):
                        for j in range(3):
                            cur = board[i+x3][j+y3]
                            if cur in s:
                                return False
                            if cur not in '.':
                                s.add(cur)
            return True
        return check_lines(board) and check_box(board)
```

### First Missing Positive

Question: Given an unsorted integer array, find the smallest missing positive integer.

[^注]:Your algorithm should run in *O*(*n*) time and uses constant extra space.

```python
 def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within 
         the range [1,...,l+1] 
    """
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i] < 0 or nums[i] >= n:
            nums[i]=0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        nums[nums[i] % n]+=n
    for i in range(1, len(nums)):
        if nums[i] // n==0:
            return i
    return n
```

### Trapping Rain Water

Question: Given *n* non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

```python

```

