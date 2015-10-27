import sys
class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        if divisor==0:
        	return sys.maxint
        else:
        	if abs(dividend)<abs(divisor):
        		return 0
        	elif abs(dividend)==abs(divisor):
        		return 1
        	else:
        		multi=0
        		tempDivisor=divisor
        		while abs(dividend)>abs(tempDivisor):
        			tempDivisor=tempDivisor<<1
        			multi+=1
        		multi-=1
        		return (1<<multi)+(self.divide(dividend-(divisor<<multi),divisor))
a=Solution()
print a.divide(-10,2)
print a.divide(2,2)

#print 1<<2