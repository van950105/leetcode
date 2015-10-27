class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return [self.combine(rowIndex,j) for j in xrange(rowIndex+1)]

    def fact(self,n):
    	if n==0:
    		return 1
    	if n==1:
    		return 1
    	else:
	    	return n*self.fact(n-1)

    def combine(self,top,bottom):
    	return self.fact(top)/(self.fact(bottom)*self.fact(top-bottom))
