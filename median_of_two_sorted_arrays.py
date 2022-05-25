'''
1, 4, 7,  8, 9
      ^         
2, 10, 11, 12
^
total = 9
half = 4


half = 1
1 3  


2
^

'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1
        total = len(nums1) + len(nums2)
        half = total//2
        l,r = 0, len(nums1)-1
        while True:
            m1 = (l+r)//2 
            m2 = half-m1-2
            l1 = nums1[m1] if m1>=0 else float("-inf") # 2
            r1 = nums1[m1+1] if m1+1<len(nums1) else float("inf") # inf
            l2 = nums2[m2] if m2>=0 else float("-inf") # -inf
            r2 = nums2[m2+1] if m2+1<len(nums2) else float("inf") # 1
            if l1<=r2 and l2<=r1:
                if total%2:
                    return min(r1,r2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2
            elif l1>r2:
                r = m1-1
            else:
                l = m1+1
                    
            
            
        
        
