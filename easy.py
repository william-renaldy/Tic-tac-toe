import random
import medium 

def computer_turn(button,text,turn):
	if turn>=3:
		return medium.computer_turn(button,text,turn)
	while True:
		choice=random.choice(button)
		if choice.text==' ':
			break
	return choice