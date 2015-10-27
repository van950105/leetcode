class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d=dict()
        for i in xrange (len(nums)):
        	if nums[i] not in d:
        		d[nums[i]]=[i]
        	else:
        		if (i-d[nums[i]][-1])<=k:
        			return True
        		else:
        			d[nums[i]].append(i)
        return False


a=Solution()
print a.containsNearbyDuplicate([1,2,3,4,4],2)
