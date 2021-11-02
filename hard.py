import random
import medium

def computer_turn(button,text,turn):
	
	
	
	
	if turn==1:
		
		if text[4]!='X':
			choice=button[4]
			
		if text[4]=='X':
			choice=button[8]
			
			
			
			
			
			
			
			
	if turn==3:
		
		
		#0
		
		if text[0]=='X' and text[1]=='X':
			choice=button[2]
			
		if text[0]=='X' and text[2]=='X':
			choice=button[1]
			
		if text[0]=='X' and text[3]=='X':
			choice=button[6]
			
		if text[0]=='X' and text[5]=='X':
			choice=button[7]
				
		if text[0]=='X' and text[6]=='X':
			choice=button[3]
				
		if text[0]=='X' and text[7]=='X':
			choice=button[5]
				
		if text[0]=='X' and text[8]=='X':
			choice=button[1]
			
			
			
		#1
			
		if text[1]=='X' and text[0]=='X':
			choice=button[2]
			
		if text[1]=='X' and text[2]=='X':
			choice=button[0]
			
		if text[1]=='X' and text[3]=='X':
			choice=button[0]
			
		if text[1]=='X' and text[5]=='X':
			choice=button[3]
				
		if text[1]=='X' and text[6]=='X':
			choice=button[0]
				
		if text[1]=='X' and text[7]=='X':
			choice=button[6]
				
		if text[1]=='X' and text[8]=='X':
			choice=button[2]
			
			
			
		#2
			
		if text[2]=='X' and text[0]=='X':
			choice=button[1]
			
		if text[2]=='X' and text[1]=='X':
			choice=button[0]
			
		if text[2]=='X' and text[3]=='X':
			choice=button[1]
			
		if text[2]=='X' and text[5]=='X':
			choice=button[8]
				
		if text[2]=='X' and text[6]=='X':
			choice=button[1]
				
		if text[2]=='X' and text[7]=='X':
			choice=button[5]
				
		if text[2]=='X' and text[8]=='X':
			choice=button[5]
			
		
			
		#3
			
		if text[3]=='X' and text[0]=='X':
			choice=button[6]
			
		if text[3]=='X' and text[1]=='X':
			choice=button[0]
			
		if text[3]=='X' and text[2]=='X':
			choice=button[0]
			
		if text[3]=='X' and text[5]=='X':
			choice=button[2]
				
		if text[3]=='X' and text[6]=='X':
			choice=button[0]
				
		if text[3]=='X' and text[7]=='X':
			choice=button[6]
				
		if text[3]=='X' and text[8]=='X':
			choice=button[6]
			
			
			
		#4
			
		if text[4]=='X' and text[0]=='X':
			choice=button[6]
			
		if text[4]=='X' and text[1]=='X':
			choice=button[7]
			
		if text[4]=='X' and text[2]=='X':
			choice=button[6]
			
		if text[4]=='X' and text[3]=='X':
			choice=button[5]
				
		if text[4]=='X' and text[5]=='X':
			choice=button[3]
				
		if text[4]=='X' and text[6]=='X':
			choice=button[2]
				
		if text[4]=='X' and text[7]=='X':
			choice=button[1]
			
			
			
			
		#5
			
		if text[5]=='X' and text[0]=='X':
			choice=button[2]
			
		if text[5]=='X' and text[1]=='X':
			choice=button[2]
			
		if text[5]=='X' and text[2]=='X':
			choice=button[8]
			
		if text[5]=='X' and text[3]=='X':
			choice=button[2]
				
		if text[5]=='X' and text[6]=='X':
			choice=button[8]
				
		if text[5]=='X' and text[7]=='X':
			choice=button[8]
				
		if text[5]=='X' and text[8]=='X':
			choice=button[2]
			
			
		#6
			
			
		if text[6]=='X' and text[0]=='X':
			choice=button[3]
			
		if text[6]=='X' and text[1]=='X':
			choice=button[0]
			
		if text[6]=='X' and text[2]=='X':
			choice=button[1]
			
		if text[6]=='X' and text[3]=='X':
			choice=button[0]
				
		if text[6]=='X' and text[5]=='X':
			choice=button[8]
				
		if text[6]=='X' and text[7]=='X':
			choice=button[8]
				
		if text[6]=='X' and text[8]=='X':
			choice=button[7]
			
		

			
		#7
			
		if text[7]=='X' and text[0]=='X':
			choice=button[6]
			
		if text[7]=='X' and text[1]=='X':
			choice=button[6]
			
		if text[7]=='X' and text[2]=='X':
			choice=button[8]
			
		if text[7]=='X' and text[3]=='X':
			choice=button[6]
				
		if text[7]=='X' and text[5]=='X':
			choice=button[8]
				
		if text[7]=='X' and text[6]=='X':
			choice=button[8]
				
		if text[7]=='X' and text[8]=='X':
			choice=button[6]
			
			
		#8
		
		if text[8]=='X' and text[0]=='X':
			choice=button[1]
			
		if text[8]=='X' and text[1]=='X':
			choice=button[5]
			
		if text[8]=='X' and text[2]=='X':
			choice=button[5]
			
		if text[8]=='X' and text[3]=='X':
			choice=button[7]
			
		if text[8]=='X' and text[5]=='X':
			choice=button[2]
				
		if text[8]=='X' and text[6]=='X':
			choice=button[7]
				
		if text[8]=='X' and text[7]=='X':
			choice=button[6]
			
			
	if 'choice' not in locals():
			choice=medium.computer_turn(button,text,turn)


	return choice
