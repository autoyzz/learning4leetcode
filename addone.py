class Solution:
	def plusone(self,digits):
		digits[-1]+=1
		while 10 in digits:
			n = digits.index(10)
			if n == 0:
				digits.insert(0,1)
				digits[1]=0
			else:
				digits[n]=0
				digits[n-1]+=1
		return digits