class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        swapK=(-1)
        swapL=(-1)
        for i in xrange(len(nums)-1):
        	if nums[i]<nums[i+1]:
        		swapK=i
        if swapK==(-1):nums=nums[::-1]
        else:
        	for i in xrange(len(nums)-1):
        		if nums[i]>nums[swapK]:
        			swapL=i
        	tempK=nums[swapK]
        	tempL=nums[swapL]
        	nums[swapL]=tempK
        	nums[swapK]=tempL
        	