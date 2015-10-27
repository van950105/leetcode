class Solution(object):
	def summaryRanges(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		rangeList=[]
		i=0
		length=len(nums)
		while i<length:
			string=str(nums[i])
			j=i+1
			while j<length and nums[j-1]==nums[j]-1:
				j+=1
			j-=1
			if j!=i:
				string=string+"->"+str(nums[j])
			rangeList.append(string)
			i=j+1
		return rangeList

a=Solution()
print a.summaryRanges([0,1,2])