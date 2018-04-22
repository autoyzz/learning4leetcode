class Solution:
	def singleNumber(self,nums):
		target = {}
		for i in nums:
			if i in target:
				target[i]+=1
			else:
				target[i]=1
		for j in target:
			if target[j]==1:
				return j

class Solution1:
	def singleNumber1(self,nums):
		for i in nums:
			if nums.count(i)==1:
				return i

a = [1,2,2]
b = Solution1().singleNumber1(a)
print(b)
		