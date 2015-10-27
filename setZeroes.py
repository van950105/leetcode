class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        zeroList=[]
        m,n=len(matrix),len(matrix[0])
        for i in xrange(m):
        	for j in xrange(n):
        		if matrix[i][j]==0:
        			zeroList.append((i,j))
        for (a,b) in zeroList:
        	matrix[a]=[0]*n
        	for i in xrange(m):
        		matrix[i][b]=0
