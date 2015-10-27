class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
    	ans=[]
    	self.dfs(n,n,ans,"")
    	return ans


    def dfs(self,left,right,ans,string):
    	if right<left:
    		return 
    	if left==0 and right==0:
    		ans.append(string)
    		return
    	if left!=0:
    		self.dfs(left-1,right,ans,string+"(")
    	if right!=0:
    		self.dfs(left,right-1,ans,string+")")


a=Solution()
print a.generateParenthesis(3)