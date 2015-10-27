class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        lenOfNeedle=len(needle)
        lenOfHaystack=len(haystack)
        i=0
        if needle=='':
        	return 0
        if haystack=='':
        	return -1
        while i<=lenOfHaystack-lenOfNeedle:
        	if haystack[i]==needle[0]:
        		if haystack[i:i+lenOfNeedle]==needle:
        			return i
        	i=i+1
        return -1


a=Solution()
print a.strStr('','')