import random
class Hero():
	"""docstring for Hero"""
	def __init__(self):
		self._positionX = 4
		self._positionY = 2
		self._upperShape = ["[","^","^","]"]
		self._lowerShape = [" ","]","["," "]
		self._lives = 3
		self._score = 0

	def clr(self,Board):
		for i in range(4):
			Board._board[self._positionX+i][self._positionY] = " "
		for i in range(4):
			Board._board[self._positionX+i][self._positionY+1] = " "

	def kill(self,board):
		self.clr(board)
		self._lives -= 1
		self._positionX = 4
		self._positionY = 2

class Villan(Hero):
	"""docstring for Villan"""
	def __init__(self,board,brick,wall):
		super(Villan, self).__init__()
		overlap = 1
		while (overlap):
			self._positionX =random.randrange(16,board._length-4,4)
			self._positionY =random.randrange(10,board._breadth-3,2)
			if (board._board[self._positionX][self._positionY] == board._freesymbol):
				overlap = 0
		self._upperShape = ["^","O","O","^"]
		self._lowerShape = [" ","}","{"," "]
		self._status = 1 # 1 -> Life   0 -> Death

	def kill(self,board,hero):
		hero._score += 100
		self._status = 0
		self.clr(board)

	def motion(self,board,bomb,hero):
		# 0 -> UP 1-> DOWN 2 -> LEFT 3 -> RIGHT
		if self._status == 0:
			return
		overlap = 1
		motion = random.randrange(0,4)
		count = 0
		while (overlap):
			if(motion == 0):
				checkY = self._positionY-2
				checkX = self._positionX
			if(motion == 1):
				checkY = self._positionY+2
				checkX = self._positionX
			if(motion == 2):
				checkY = self._positionY
				checkX = self._positionX-4
			if(motion == 3):
				checkY = self._positionY
				checkX = self._positionX+4
			if (board._board[checkX][checkY] == board._freesymbol or board._board[checkX][checkY] == "["):
				overlap = 0
				self.clr(board)
				self._positionX = checkX
				self._positionY = checkY
				if(self._positionX == hero._positionX and self._positionY == hero._positionY):
					hero.kill(board)
			motion = (motion + 1) % 4
			count += 4
			if (count > 5):
				break

		board.playerDraw(self)
		