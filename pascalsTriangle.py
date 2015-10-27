class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result=[]
        for i in xrange(numRows):
        	result.append([(self.combine(i,j)) for j in xrange(i+1)])
        return result

    def fact(self,n):
    	if n==0:
    		return 1
    	if n==1:
    		return 1
    	else:
	    	return n*self.fact(n-1)

    def combine(self,top,bottom):
    	return self.fact(top)/(self.fact(bottom)*self.fact(top-bottom))

a=Solution()
print a.generate(5)