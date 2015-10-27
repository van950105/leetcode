class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        d=dict()
        (m,n)=(len(obstacleGrid),len(obstacleGrid[0])
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
        noObstaclePath=pathHelper(m,n)
        obstacleList=[]
        for i in xrange(m):
        	for j in xrange(n):
        		if obstacleGrid[i][j]==0:
        			obstacleList.append(i,j)
        for i in xrange(len(obstacleList)):
        	i+=1
        	for j in xrange()