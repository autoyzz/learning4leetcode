class Solution():
	def isValidSukodu(self,board):
		for i in range(9):
			for j in range(9):
				temp = board[i][j]
				if temp == '.':
					continue
				board[i][j]='*'
				if self.valid(i,j,temp,board)== False:
					return False
				else:
					board[i][j] = temp
		return True
	def valid(self,x,y,temp,board):
		for i in range(9):
			if board[x][i]==temp:
				return False
			if board[i][y]==temp:
				return False
		for i in range(3):
			for j in range(3):
				if board[(x//3)*3+i][(y//3)*3+j]==temp:
					return False
		return True


a = Solution()
m = [[".","4",".",".",".",".",".",".","."],
      [".",".","4",".",".",".",".",".","."],
      [".",".",".","1",".",".","7",".","."],
      [".",".",".",".",".",".",".",".","."],
      [".",".",".","3",".",".",".","6","."],
      [".",".",".",".",".","6",".","9","."],
      [".",".",".",".","1",".",".",".","."],
      [".",".",".",".",".",".","2",".","."],
      [".",".",".","8",".",".",".",".","."]]
print(a.isValidSukodu(m))

