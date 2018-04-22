class Solution:
	"""
	intersection
	"""
	def intersect(self,nums1,nums2):
		return list(set(nums1).intersection(set(nums2)))

a = Solution()
l1=[1,2,2,3,4,5,6]
l2=[2,2,8]
b = a.intersect(l1,l2)
print(b)