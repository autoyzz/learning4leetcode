class Solution():
	def rotate(self,matrix):
		'''
		matrix T and reverse
		'''
		n = len(matrix[0])
		for i in range(n):
			for j in range(i+1,n):
				matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
		for k in range(n):
			matrix[k].reverse()
		print(matrix) 
a = Solution()
b = [[1,2,3],[4,5,6],[7,8,9]]
a.rotate(b)