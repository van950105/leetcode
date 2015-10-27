class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lower=0
        upper=len(nums)-1
        if target>nums[upper]:
        	return upper+1
        if target<nums[0]:
        	return 0
        while lower<=upper:
        	index=(lower+upper)/2
        	if nums[index]>target:
        		upper=index-1
        		if upper>=0:
        			if nums[upper]<target:
        				return upper+1
        		else:
        			return 0
        	elif nums[index]<target:
        		lower=index+1
        		if lower==len(nums):
        			return lower-1
        		else:
        			if nums[1]>target:
        				return 1
        	else:
        		return index

a=Solution()
print a.searchInsert([1],2)