class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        return self.letterCombinationsHelper(digits,[''])

    global MAP
    MAP={'1':[""],'2':["a","b","c"],'3':["d","e","f"],'4':["g","h","i"],'5':["j","k","l"],'6':["m","n","o"],\
    	'7':["p","q","r","s"],'8':["t","u","v"],'9':["w","x","y","z"],'0':[""]}

    def letterCombinationsHelper(self,digits,psbCombo):
    	if len(digits)==0:
    		if psbCombo==[""]:
    			psbCombo=[]
    		return psbCombo
    	else:
    		currentDigit=digits[0]
    		digits=digits[1:]
    		newList=[]
    		for i in MAP[currentDigit]:
    			for j in psbCombo:
    				newList.append(j+i)
    		return self.letterCombinationsHelper(digits,newList)


a=Solution()
print a.letterCombinations('')
#when there s no input, it should return an empty list