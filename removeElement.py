class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
		nums.sort()
		try:
			start=nums.index(val)
			end=len(nums)-nums[::-1].index(val)
		except Exception:
			return len(nums)
		for i in xrange(end-start):
			nums.pop(start)
		return len(nums)

a=Solution()
print a.removeElement([1,2,3,4,4],0)