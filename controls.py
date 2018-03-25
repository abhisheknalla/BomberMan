import sys

def controls(move,hero,board,bomb):

	if(move == 'w' and (board._board[hero._positionX][hero._positionY-2] == board._freesymbol)):
		hero.clr(board)
		hero._positionY -= 2

	if(move == 's' and (board._board[hero._positionX][hero._positionY+2] == board._freesymbol)):
		hero.clr(board)
		hero._positionY += 2
		
	if(move == 'a' and (board._board[hero._positionX-4][hero._positionY] == board._freesymbol)):
		hero.clr(board)
		hero._positionX -= 4
		
	if(move == 'd' and (board._board[hero._positionX+4][hero._positionY] == board._freesymbol)):
		hero.clr(board)
		hero._positionX += 4
	
	if(move == 'x'):
		bomb.plant(hero,board)

	if (move == 'q'):
			sys.exit(0)	

