class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        length=len(nums)
        while i<length:
        	if nums[i]!=0:
        		i+=1
        	else:
        		j=i
        		while (j<length) and nums[j]==0:
        			j+=1
        			if j==length:
        				return 
        		nums[i]=nums[j]
        		nums[j]=0
        		i+=1
        return 
a=Solution()
print a.moveZeroes([0,1,2,3])