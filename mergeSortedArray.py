class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        (i,j)=(0,0)
        if m==0:
        	nums1.extend(nums2)
        for j in xrange(n):
        	while i<m+j and nums2[j]>nums1[i]:
        		i+=1
        	nums1.insert(i,nums2[j])
        	if i==m+j:
        		break
        	nums1[m+j+1:]=nums2[j+1:]