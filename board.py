from random import randrange
from obstacle import *
from termcolor import colored
class Board():
	"""Manage and print game"""
	def __init__(self):
		self._breadth = 34
		self._length = 76
		self._board = []
		self._freesymbol=" "
		for i in range(self._length):
			self._board.append([])
			for j in range(self._breadth):
				if i == 0 or i == 1 or i == 2 or i == 3 or i == self._length-3 or i == self._length-4 or i == self._length-2 or i == self._length-1:
					self._board[i].append("#")
				else:
					if j == 0 or j == 1 or j ==self._breadth-2  or j == self._breadth-1:
						self._board[i].append("#")
					else:
						self._board[i].append(self._freesymbol)

	def draw(self):
		for j in range(self._breadth):
			print()
			for i in range(self._length):
				if(self._board[i][j] == "/"):
					print(colored(self._board[i][j],'yellow',attrs=['bold']),end='')
				elif(self._board[i][j] == "[" or self._board[i][j] == "]" or self._board[i][j] == "^"):
					print(colored(self._board[i][j],'cyan',attrs=['bold']),end='')
				elif(self._board[i][j] == "O" or self._board[i][j] == "}" or self._board[i][j] == "{"):
					print(colored(self._board[i][j],'magenta',attrs=['bold']),end='')					
				elif(self._board[i][j] == "0" or self._board[i][j] == "1" or self._board[i][j] == "2" or self._board[i][j] == "3" or self._board[i][j] == "|"):
					print(colored(self._board[i][j],'red',attrs=['bold']),end='')					
				else:
					print(self._board[i][j],end='')					
		print()

	def random_wall(self):
		x = random.randrange(2,self._length-3)
		y = random.randrange(2,self._breadth-3)

	def playerDraw(self,player):
		for i in range(4):
			self._board[player._positionX+i][player._positionY] = player._upperShape[i]
		for i in range(4):
			self._board[player._positionX+i][player._positionY+1] = player._lowerShape[i]

	def bombDraw(self,player,bomb,vill):
		if(bomb._positionX != -1 and (player._positionX != bomb._positionX or player._positionY != bomb._positionY) and self._board[bomb._positionX][bomb._positionY] != vill[0]._upperShape[0]):
			for i in range(4):
				self._board[bomb._positionX+i][bomb._positionY] = bomb._upperShape[i]
				self._board[bomb._positionX+i][bomb._positionY+1] = bomb._lowerShape[i]

		if(bomb._positionX == -1):
			for i in range(4):
				self._board[bomb._prevX+i][bomb._prevY] = self._freesymbol
				self._board[bomb._prevX+i][bomb._prevY+1] = self._freesymbol
			
			# Restore blast shape
			for i in range(bomb._prevX-4,bomb._prevX+8):
				if(self._board[i][bomb._prevY] != "#"):
					self._board[i][bomb._prevY] = self._freesymbol
					self._board[i][bomb._prevY+1] = self._freesymbol

			for i in range(bomb._prevX,bomb._prevX+4):
				if(self._board[i][bomb._prevY-2] != "#"):
					self._board[i][bomb._prevY-2] = self._freesymbol
					self._board[i][bomb._prevY-1] = self._freesymbol
				if(self._board[i][bomb._prevY+2] != "#"):
					self._board[i][bomb._prevY+2] = self._freesymbol
					self._board[i][bomb._prevY+3] = self._freesymbol
			
			bomb._prevX = -1
			bomb._prevY = -1
		

