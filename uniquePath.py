class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d=dict()
        for i in xrange(m+1):
        	for j in xrange(n+1):
        		d[(i,j)]=0
        d[(1,1)]=1
        def pathHelper(m,n):
	        if (m==1) or (n==1):
				return d[(1,1)]
        	else:
        		f=d[(m,n)]
        		if f==0:
        			f=pathHelper(m-1,n)+pathHelper(m,n-1)
        			d[(m,n)]=f
        		return f
        return pathHelper(m,n)


        	


a=Solution()
print a.uniquePaths(100,100)
