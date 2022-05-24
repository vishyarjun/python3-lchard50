'''
URL: https://leetcode.com/problems/longest-valid-parentheses/
difficulty: HARD
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        ans = 0
        for i,char in enumerate(s):
            if char =='(':
                stk.append(i)
            else:
                if len(stk)>0 and s[stk[-1]]=='(':
                    stk.pop()
                else:
                    stk.append(i)
        big = len(s)
        while len(stk)>0:
            cur = stk.pop()
            ans = max(ans,big-cur-1)
            big = cur
        ans = max(ans,big-0)
        return ans
      
# Time Complexity: O(N)
# Space Complexity: O(N)
