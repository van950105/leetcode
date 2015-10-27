class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits==[]:return[1]
        if digits[-1]<9:
        	digits[-1]+=1
        	return digits
        else:
        	temp=self.plusOne(digits[:-1])
        	temp.append(0)
        	return temp
