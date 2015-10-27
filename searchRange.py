class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lower=0
        upper=len(nums)-1
        if target<nums[lower]:
        	return [-1,-1]
        if target>nums[upper]:
        	return [-1,-1]
        while lower<=upper:
        	index=(lower+upper)/2
        	if target==nums[index]:
        		s=index
        		e=index
        		while s>=0 and nums[s]==target:
        			s-=1
        		while e<len(nums) and nums[e]==target:
        			e+=1
        		(s,e)=(s+1,e-1)
        		return [s,e]
        	elif target<nums[index]:
        		if index==0:
        			return [-1,-1]
        		else:
        			upper=index-1
        	elif target>nums[index]:
        		if index==len(nums)-2:
        			if target==nums[index+1]:
        				return [index+1,index+1]
        			else:
        				return [-1,-1]
        		else:
        			if target<nums[index+1]:
        				return[-1,-1]
        			lower=index+1



a=Solution()
print a.searchRange([1,4,4],4)


