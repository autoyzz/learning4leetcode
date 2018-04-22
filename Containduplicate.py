class Solution:
	def caontainsDuplicate(self,nums):
		"""
		:typr nums: List[int]
		:rtype:bool
		"""
		s = set(nums)
		if len(s) ==len(nums):
			return False
		else:
			return True



