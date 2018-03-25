import random
import signal,copy,sys,time
from board import *
from player import *
from obstacle import *
from getchunix import *
from alarmexception import *
from controls import *
from bomb import *

getch = GetchUnix()	

def alarmHandler(signum, frame):
	raise AlarmException

def input_to(timeout = 1):
	signal.signal(signal.SIGALRM, alarmHandler)
	signal.setitimer(signal.ITIMER_REAL,timeout)
	t0 = time.time()
	try:
		text = getch()
		signal.alarm(0)
		t1 = time.time()
		while (t1 - t0 < 0.5):
			t1 = time.time()
		return text
	except AlarmException:
		print(end='')
	signal.signal(signal.SIGALRM, signal.SIG_IGN)
	return ''

def main():
	print("Press any key to start game")
	level = 1
	score = 0
	t0 = time.time()
	while(1):
		villan = []
		hero = Hero()
		board_obj = Board()
		wall = Wall()
		wall.fabricate(board_obj)
		brick = []
		bomb = Bomb(level)
		brick_cnt = 35 - 3 * level
		for i in range(brick_cnt):
			brick.append(Brick())
			brick[i].fabricate(board_obj,wall)

		for i in range (bomb._villan_cnt):
			villan.append(Villan(board_obj,brick,wall))
		
		while(hero._lives and bomb._villan_cnt):
			
			move = input_to()
			controls(move,hero,board_obj,bomb)
			t1 = time.time()
			if(t1 - t0 > 1):
				t0 = time.time()
				for i in range (bomb._villan_cnt):
					villan[i].motion(board_obj,bomb,hero)
			board_obj.bombDraw(hero,bomb,villan)
			t2 = time.time()
			if(t2 - bomb._plant_time > 1):
				bomb._plant_time = time.time()
				if(bomb._positionX != -1):
					bomb._time -= 1
					bomb._upperShape=[bomb._boundary,bomb._time,bomb._time,bomb._boundary]
					bomb._lowerShape=[bomb._boundary,bomb._time,bomb._time,bomb._boundary]
			if(bomb._time == -1):
				bomb.blast(board_obj,hero,villan)
				blast = 1
			board_obj.playerDraw(hero)
			board_obj.draw()
			total_score = score + hero._score
			print("Score: " , total_score , "  Lives: " , hero._lives , "  Level: " , level)
		level += 1
		score += hero._score
if __name__ == '__main__':
	main()
