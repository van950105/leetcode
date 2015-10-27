class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
    	d={"(":")","[":"]","{":"}"}
    	stack=[]
    	for i in s:
    		if i in d:
    			stack.append(i)
    		else:
    			if len(stack)==0 or d[stack[-1]]!=i:
    				return False
    			else:
    				stack.pop(-1)
    	if len(stack)!=0:
    		return False
    	else:
    		return True

a=Solution()
print a.isValid("]")

#Using stack