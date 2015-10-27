class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=dict()
        length=len(nums)
        for i in nums:
        	if i in d:
        		d[i]+=1
        	else:
        		d[i]=1
        	if d[i]>=(length/2+1):
        		return i


a=Solution()
print a.majorityElement([1,2,3,3,3,3])
        