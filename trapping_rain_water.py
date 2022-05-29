'''
4, 2, 0, 3, 2, 5
            ^            
               ^


'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0:
            return 0
        mxLeft, mxRight = height[0],height[-1]
        l,r = 0,len(height)-1
        ans = 0
        while l<r:
            if mxLeft<mxRight:
                l+=1
                mxLeft = max(mxLeft,height[l])
                ans += (mxLeft-height[l])
            else:
                r-=1
                mxRight = max(mxRight, height[r])
                ans += (mxRight-height[r])
        return ans
        
       
        
        
