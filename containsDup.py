class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    	hashSet=set()
    	for i in nums:
    		if i not in hashSet:
    			hashSet.add(i)
    		else:
    			return True
    	return False