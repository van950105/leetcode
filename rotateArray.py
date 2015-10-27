class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        self.reverse(nums,0,length-k)
        self.reverse(nums,length-k,length)
        self.reverse(nums,0,length)
    
    def reverse(self,num,s,e):
    	num[s:e]=num[s:e][::-1]


#Rotate first part,second part and the whole list
a=Solution()
print a.rotate([1],1)

