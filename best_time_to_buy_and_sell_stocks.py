'''

        3  2  6  5  0  3
  0     0  0  0  0  0  0
  1     0  0  4  4  4  4
  2     0  0  4  0  0  0

mn = 2
'''


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k==0 or len(prices)==0:
            return 0
        dp=[[0 for _ in range(len(prices))] for _ in range(k+1)]
        
        
        for i in range(len(dp)):
            mx=0-prices[0]
            for j in range(len(dp[0])):
                if i==0 or j==0:
                    dp[i][j]=0
                else:
                    mx=max(mx,dp[i-1][j-1]-prices[j-1])
                    dp[i][j]=max(dp[i][j-1],prices[j]+mx)
                    
       
        return dp[-1][-1]
