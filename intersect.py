class Solution:
	"""
	intersection
	"""
	def intersect(self,nums1,nums2):
		#return list(set(nums1).intersection(set(nums2)))
		dt1 = {}
		s = []
		for i in nums1:
			if i in dt1:
				dt1[i] +=1
			else:
				dt1[i] =1
		for j in nums2:
			if j in dt1 and dt1[j] > 0:
				s.append(j)
				dt1[j] -=1
		return s




a = Solution()
l1=[2,2,3,4,5,6,8]
l2=[2,2,8]
b = a.intersect(l1,l2)
print(b) 