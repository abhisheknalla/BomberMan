import time

class Bomb():
	def __init__(self,level):
		self._positionX = -1
		self._positionY = -1
		self._prevX = -1
		self._prevY = -1
		self._time = 4
		self._boundary = "|"
		self._upperShape = [self._boundary,self._time,self._time,self._boundary]
		self._lowerShape = [self._boundary,self._time,self._time,self._boundary]
		self._villan_cnt = 3 * level
		self._plant_time = time.time()
	def plant(self,hero,board):
		if(self._positionX == -1):
			self._positionX = hero._positionX
			self._positionY = hero._positionY

	def blast(self,board,hero,villan):
		self._blastshape = "^"
		self._prevX = self._positionX
		self._prevY = self._positionY		
		self._positionX = -1
		self._positionY = -1
		self._time = 4

		# Brick score

		if (board._board[self._prevX-4][self._prevY] == "/"):
			hero._score += 20

		if (board._board[self._prevX+4][self._prevY] == "/"):
			hero._score += 20

		if (board._board[self._prevX][self._prevY-2] == "/"):
			hero._score += 20

		if (board._board[self._prevX][self._prevY+2] == "/"):
			hero._score += 20	
				
		for i in range(self._prevX-4,self._prevX+8):
			if(board._board[i][self._prevY] != "#"):
				board._board[i][self._prevY] = self._blastshape
				board._board[i][self._prevY+1] = self._blastshape

		for i in range(self._prevX,self._prevX+4):
			if(board._board[i][self._prevY-2] != "#"):
				board._board[i][self._prevY-2] = self._blastshape
				board._board[i][self._prevY-1] = self._blastshape
			
			if(board._board[i][self._prevY+2] != "#"):
				board._board[i][self._prevY+2] = self._blastshape
				board._board[i][self._prevY+3] = self._blastshape
		if(((hero._positionX >= self._prevX -4 and hero._positionX < self._prevX +5) and (hero._positionY == self._prevY)) or ((hero._positionY >= self._prevY -2 and hero._positionY < self._prevY +3) and hero._positionX == self._prevX)):
			hero.kill(board)

		for i in range(self._villan_cnt):
			if(((villan[i]._positionX >= self._prevX -4 and villan[i]._positionX < self._prevX +5) and (villan[i]._positionY == self._prevY)) or ((villan[i]._positionY >= self._prevY -2 and villan[i]._positionY < self._prevY +3) and villan[i]._positionX == self._prevX)):
				self._villan_cnt -= 1
				villan[i].kill(board,hero)

