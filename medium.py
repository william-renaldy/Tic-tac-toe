import random
def computer_turn(button,text,turn):
	if text[0]==text[1] and text[0]=='O' and text[2]==' ':
		choice=button[2]
	elif text[3]==text[4] and text[3]=='O' and text[5]==' ':
		choice=button[5]
	elif text[6]==text[7] and text[7]=='O' and text[8]==' ':
		choice=button[8]
		
		
	elif text[0]==text[3] and text[0]=='O' and text[6]==' ':
		choice=button[6]
	elif text[1]==text[4] and text[1]=='O' and text[7]==' ':
		choice=button[7]
	elif text[2]==text[5] and text[2]=='O' and text[8]==' ':
		choice=button[8]
		
	elif text[0]==text[2] and text[0]=='O' and text[1]==' ':
		choice=button[1]
	elif text[3]==text[5] and text[3]=='O' and text[4]==' ':
		choice=button[4]
	elif text[6]==text[8] and text[6]=='O' and text[7]==' ':
		choice=button[7]
		
		
	elif text[0]==text[6] and text[0]=='O' and text[3]==' ':
		choice=button[3]
	elif text[1]==text[7] and text[1]=='O' and text[4]==' ':
		choice=button[4]
	elif text[2]==text[8] and text[2]=='O' and text[5]==' ':
		choice=button[5]
		
		
	elif text[1]==text[2] and text[1]=='O' and text[0]==' ':
		choice=button[0]
	elif text[4]==text[5] and text[4]=='O' and text[3]==' ':
		choice=button[3]
	elif text[7]==text[8] and text[7]=='O' and text[6]==' ':
		choice=button[6]
		
		
	elif text[3]==text[6] and text[3]=='O' and text[0]==' ':
		choice=button[0]
	elif text[4]==text[7] and text[4]=='O' and text[1]==' ':
		choice=button[1]
	elif text[5]==text[8] and text[5]=='O' and text[2]==' ':
		choice=button[2]
		
	
		
		
	elif text[0]==text[4] and text[0]=='O' and text[8]==' ':
		choice=button[8]
	elif text[2]==text[4] and text[2]=='O' and text[6]==' ':
		choice=button[6]
		
		
	elif text[0]==text[8] and text[0]=='O' and text[4]==' ':
		choice=button[4]
	elif text[2]==text[6] and text[2]=='O' and text[4]==' ':
		choice=button[4]
		

	elif text[4]==text[8] and text[4]=='O' and text[0]==' ':
		choice=button[0]
	elif text[4]==text[6] and text[4]=='O' and text[2]==' ':
		choice=button[2]
	else:
		pass
	
	try:
		return choice
	except:
		pass
		
	if text[0]==text[1] and text[0]=='X' and text[2]==' ':
		choice=button[2]
	elif text[3]==text[4] and text[3]=='X' and text[5]==' ':
		choice=button[5]
	elif text[6]==text[7] and text[7]=='X' and text[8]==' ':
		choice=button[8]
		
		
	elif text[0]==text[3] and text[0]=='X' and text[6]==' ':
		choice=button[6]
	elif text[1]==text[4] and text[1]=='X' and text[7]==' ':
		choice=button[7]
	elif text[2]==text[5] and text[2]=='X' and text[8]==' ':
		choice=button[8]
		
	elif text[0]==text[2] and text[0]=='X' and text[1]==' ':
		choice=button[1]
	elif text[3]==text[5] and text[3]=='X' and text[4]==' ':
		choice=button[4]
	elif text[6]==text[8] and text[6]=='X' and text[7]==' ':
		choice=button[7]
		
		
	elif text[0]==text[6] and text[0]=='X' and text[3]==' ':
		choice=button[3]
	elif text[1]==text[7] and text[1]=='X' and text[4]==' ':
		choice=button[4]
	elif text[2]==text[8] and text[2]=='X' and text[5]==' ':
		choice=button[5]
		
		
	elif text[1]==text[2] and text[1]=='X' and text[0]==' ':
		choice=button[0]
	elif text[4]==text[5] and text[4]=='X' and text[3]==' ':
		choice=button[3]
	elif text[7]==text[8] and text[7]=='X' and text[6]==' ':
		choice=button[6]
		
		
	elif text[3]==text[6] and text[3]=='X' and text[0]==' ':
		choice=button[0]
	elif text[4]==text[7] and text[4]=='X' and text[1]==' ':
		choice=button[1]
	elif text[5]==text[8] and text[5]=='X' and text[2]==' ':
		choice=button[2]
		
		
	elif text[0]==text[4] and text[0]=='X' and text[8]==' ':
		choice=button[8]
	elif text[2]==text[4] and text[2]=='X' and text[6]==' ':
		choice=button[6]
		
		
	elif text[0]==text[8] and text[0]=='X' and text[4]==' ':
		choice=button[4]
	elif text[2]==text[6] and text[2]=='X' and text[4]==' ':
		choice=button[4]
		

	elif text[4]==text[8] and text[4]=='X' and text[0]==' ':
		choice=button[0]
	elif text[4]==text[6] and text[4]=='X' and text[2]==' ':
		choice=button[2]
		
		
	elif (text[1]=='O' or text[3]=='O' or text[5]=='O' or text[7] == 'O') and text[4]==' ':
		choice=button[4]
	
	
	else:
		while True:
			choice=random.choice(button)
			if choice.text==' ':
				break
	return choice