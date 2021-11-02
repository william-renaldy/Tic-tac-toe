import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
import random
Window.clearcolor=(1,1,240/255,0)


class mygrid(GridLayout):
	def __init__(self,**kwargs):
		super(mygrid,self).__init__(**kwargs)
		self.size_x=Window.size[0]
		self.size_y=Window.size[1]
		self.size_hint_x=None
		self.size_hint_y=None
		self.height=self.size_y
		self.width=self.size_x
		
		self.check=True
		self.turn=0
		self.winner=None
		self.play_computer=False
		self.difficulty_level='Easy'
		self.cols=1
		self.add_widget(Label(size_hint_y=None,height=self.size_y/40))
	
		self.add_widget(Label(text='Tic - Tac - Toe',size_hint_y=None,height=self.size_y/9,font_size=self.size_x/10,color=(0,0,0,1)))
		self.add_widget(Label(size_hint_y=None,height=self.size_y/30))
		
		self.difficulty=GridLayout(cols=7,size_hint_y=None,height=0)
		self.add_widget(self.difficulty)
		

		
		
		self.add_widget(Label(size_hint_y=None,height=self.size_y/30))
		
		
		self.play_stat=Label(text='You are playing against Human',size_hint_y=None,height=self.size_y/21,font_size=self.size_x/20,color=(0,0,0,1))
		self.add_widget(self.play_stat)
		
		
		
		self.add_widget(Label(size_hint_y=None,height=self.size_y/42))
		
		
		
		self.number=GridLayout(cols=7,size_hint_y=None,height=self.size_y/2.5)
		self.add_widget(self.number)
	
		self.number.add_widget(Label(size_hint_x=None,width=self.size_x/12))
		
		
		self.button1=Button(text=' ',background_color=(1,1,240/255,0),color=(0,0,0,1),font_size=self.size_x/10)
		self.number.add_widget(self.button1)
		self.button1.bind(on_press=self.Button_pressed)
		self.number.add_widget(Button(size_hint_x=None,width=13,text='',background_color=(0,0,0,1)))
		
		
		
		self.button2=Button(text=' ',background_color=(1,1,240/255,0),color=(0,0,0,1),font_size=self.size_x/10)
		self.number.add_widget(self.button2)
		self.button2.bind(on_press=self.Button_pressed)
		self.number.add_widget(Button(size_hint_x=None,width=13,text='',background_color=(0,0,0,1)))
		self.button3=Button(text=' ',background_color=(1,1,240/255,0),color=(0,0,0,1),font_size=self.size_x/10)
		self.number.add_widget(self.button3)
		self.button3.bind(on_press=self.Button_pressed)
		
		
		self.number.add_widget(Label(size_hint_x=None,width=self.size_x/12,size_hint_y=None,height=13))
		self.number.add_widget(Label(size_hint_x=None,width=self.size_x/12,size_hint_y=None,height=13))
		
		
		self.number.add_widget(Button(size_hint_y=None,height=13,text='',background_color=(0,0,0,1)))
		self.number.add_widget(Button(size_hint_y=None,height=13,text='',size_hint_x=None,width=13,background_color=(0,0,0,1)))
		self.number.add_widget(Button(size_hint_y=None,height=13,text='',background_color=(0,0,0,1)))
		self.number.add_widget(Button(size_hint_y=None,height=13,text='',size_hint_x=None,width=13,background_color=(0,0,0,1)))
		self.number.add_widget(Button(size_hint_y=None,height=13,text='',background_color=(0,0,0,1)))
		
		
		
		self.number.add_widget(Label(size_hint_x=None,width=self.size_x/12,size_hint_y=None,height=13))
		self.number.add_widget(Label(size_hint_x=None,width=self.size_x/12,size_hint_y=None,height=13))

		self.button4=Button(text=' ',background_color=(1,1,240/255,0),color=(0,0,0,1),font_size=self.size_x/10)
		self.number.add_widget(self.button4)
		self.button4.bind(on_press=self.Button_pressed)
		self.number.add_widget(Button(size_hint_x=None,width=13,text='',background_color=(0,0,0,1)))
		self.button5=Button(text=' ',background_color=(1,1,240/255,0),color=(0,0,0,1),font_size=self.size_x/10)
		self.number.add_widget(self.button5)
		self.button5.bind(on_press=self.Button_pressed)
		self.number.add_widget(Button(size_hint_x=None,width=13,text='',background_color=(0,0,0,1)))
		self.button6=Button(text=' ',background_color=(1,1,240/255,0),color=(0,0,0,1),font_size=self.size_x/10)
		self.number.add_widget(self.button6)
		self.button6.bind(on_press=self.Button_pressed)
		self.number.add_widget(Label(size_hint_x=None,width=self.size_x/12,size_hint_y=None,height=13))
		self.number.add_widget(Label(size_hint_x=None,width=self.size_x/12,size_hint_y=None,height=13))
		
		self.number.add_widget(Button(size_hint_y=None,height=13,text='',background_color=(0,0,0,1)))
		self.number.add_widget(Button(size_hint_y=None,height=13,text='',size_hint_x=None,width=13,background_color=(0,0,0,1)))
		self.number.add_widget(Button(size_hint_y=None,height=13,text='',background_color=(0,0,0,1)))
		self.number.add_widget(Button(size_hint_y=None,height=13,text='',size_hint_x=None,width=13,background_color=(0,0,0,1)))
		self.number.add_widget(Button(size_hint_y=None,height=13,text='',background_color=(0,0,0,1)))
		
		self.number.add_widget(Label(size_hint_x=None,width=self.size_x/12,size_hint_y=None,height=13))
		self.number.add_widget(Label(size_hint_x=None,width=self.size_x/12))
		self.button7=Button(text=' ',background_color=(1,1,240/255,0),color=(0,0,0,1),font_size=self.size_x/10)
		self.number.add_widget(self.button7)
		self.button7.bind(on_press=self.Button_pressed)
		self.number.add_widget(Button(size_hint_x=None,width=13,text='',background_color=(0,0,0,1)))
		self.button8=Button(text=' ',background_color=(1,1,240/255,0),color=(0,0,0,1),font_size=self.size_x/10)
		self.number.add_widget(self.button8)
		self.button8.bind(on_press=self.Button_pressed)
		self.number.add_widget(Button(size_hint_x=None,width=13,text='',background_color=(0,0,0,1)))
		self.button9=Button(text=' ',background_color=(1,1,240/255,0),color=(0,0,0,1),font_size=self.size_x/10)
		self.number.add_widget(self.button9)
		self.button9.bind(on_press=self.Button_pressed)
		self.number.add_widget(Label(size_hint_x=None,width=self.size_x/12))
		
		
		self.res=Label(size_hint_y=None,height=self.size_y/8.5,font_size=self.size_x/18,color=(0,0,0,1))
		self.add_widget(self.res)
		
		
		
		self.play_grid=GridLayout(cols=5,size_hint_y=None,height=self.size_y/11)
		self.add_widget(self.play_grid)
		self.play_grid.add_widget(Label(size_hint_x=None,width=self.size_x/11))
		self.play=Button(text='Reset',size_hint_x=None,width=self.size_x*2.9/11,font_size=self.size_x/23,background_color=(0,1,0.3,1))
		self.play_grid.add_widget(self.play)
		self.play.bind(on_press=self.play_again)
		self.play_grid.add_widget(Label(size_hint_x=None,width=self.size_x/11))
		self.play_comp=Button(text='Play against Computer',size_hint_x=None,width=self.size_x*5.1/11,font_size=self.size_x/25,background_color=(0,1,0.3,1))
		self.play_comp.bind(on_press=self.play_against_computer)
		self.play_grid.add_widget(self.play_comp)
		self.play_grid.add_widget(Label(size_hint_x=None,width=self.size_x/11))
		
		
	def difficulty_fun(self,instance):
		self.easy.background_color=(0,1,0.3,1)
		self.medium.background_color=(0,1,0.3,1)
		self.hard.background_color=(0,1,0.3,1)
		self.difficulty_level=instance.text
		if instance.text=='Easy':
			instance.background_color=(10,0,1,1)
		if instance.text=='Medium':
			instance.background_color=(10,0,1,1)
		if instance.text=='Hard':
			instance.background_color=(10,0,1,1)
		
		
	def play_against_computer(self,instance):
		if self.play_computer==False:
			self.play_stat.text='You are playing against Computer'
			
			
			self.difficulty.height=self.size_y/15
			self.e1=Label()
			self.difficulty.add_widget(self.e1)
			self.easy=Button(text='Easy',background_color=(10,0,1,1),size_hint_x=None,width=self.size_x/4,on_press=self.difficulty_fun)
			self.difficulty.add_widget(self.easy)
			self.e2=Label()
			self.difficulty.add_widget(self.e2)
			self.medium=Button(text='Medium',size_hint_x=None,background_color=(0,1,0.3,1),width=self.size_x/4,on_press=self.difficulty_fun)
			self.difficulty.add_widget(self.medium)
			self.e3=Label()
			self.difficulty.add_widget(self.e3)
			self.hard=Button(text='Hard',background_color=(0,1,0.3,1),size_hint_x=None,width=self.size_x/4,on_press=self.difficulty_fun)
			self.difficulty.add_widget(self.hard)
			self.e4=Label()
			self.difficulty.add_widget(self.e4)
			self.play_computer=True
			instance.text='Play against Human'
			
		elif self.play_computer==True:
			self.difficulty.remove_widget(self.easy)
			self.difficulty.remove_widget(self.e1)
			self.difficulty.remove_widget(self.e2)
			self.difficulty.remove_widget(self.e3)
			self.difficulty.remove_widget(self.e4)
			self.difficulty.remove_widget(self.medium)
			self.difficulty.remove_widget(self.hard)
			self.difficulty.height=0
			self.play_stat.text='You are playing against Human'
			self.play_computer=False
			instance.text='Play against Computer'
		self.play_again(None)
		
		
	def result(self):
		if self.winner==None:
			if self.button1.text=='X' and self.button2.text=='X' and self.button3.text=='X':
				self.button1.background_color=(10,0,1,0.55)
				self.button2.background_color=(10,0,1,0.55)
				self.button3.background_color=(10,0,1,0.55)
				
				self.winner='X'
			elif self.button4.text=='X' and self.button5.text=='X' and self.button6.text=='X':
				self.button4.background_color=(10,0,1,0.55)
				self.button5.background_color=(10,0,1,0.55)
				self.button6.background_color=(10,0,1,0.55)
				self.winner='X'
			elif self.button7.text=='X' and self.button8.text=='X' and self.button9.text=='X':
				self.button7.background_color=(10,0,1,0.55)
				self.button8.background_color=(10,0,1,0.55)
				self.button9.background_color=(10,0,1,0.55)
				self.winner='X'
			elif self.button1.text=='X' and self.button4.text=='X' and self.button7.text=='X':
				self.button1.background_color=(10,0,1,0.55)
				self.button4.background_color=(10,0,1,0.55)
				self.button7.background_color=(10,0,1,0.55)
				self.winner='X'
			elif self.button2.text=='X' and self.button5.text=='X' and self.button8.text=='X':
				self.button2.background_color=(10,0,1,0.55)
				self.button5.background_color=(10,0,1,0.55)
				self.button8.background_color=(10,0,1,0.55)
				self.winner='X'
			elif self.button3.text=='X' and self.button6.text=='X' and self.button9.text=='X':
				self.button3.background_color=(10,0,1,0.55)
				self.button6.background_color=(10,0,1,0.55)
				self.button9.background_color=(10,0,1,0.55)
				self.winner='X'
			elif self.button1.text=='X' and self.button5.text=='X' and self.button9.text=='X':
				self.button1.background_color=(10,0,1,0.55)
				self.button5.background_color=(10,0,1,0.55)
				self.button9.background_color=(10,0,1,0.55)
				self.winner='X'
			elif self.button3.text=='X' and self.button5.text=='X' and self.button7.text=='X':
				self.button3.background_color=(10,0,1,0.55)
				self.button5.background_color=(10,0,1,0.55)
				self.button7.background_color=(10,0,1,0.55)
				self.winner='X'
			else:
				pass
	
	
	
			if self.button1.text=='O' and self.button2.text=='O' and self.button3.text=='O':
				self.button1.background_color=(10,0,1,0.55)
				self.button2.background_color=(10,0,1,0.55)
				self.button3.background_color=(10,0,1,0.55)
				self.winner='O'
			elif self.button4.text=='O' and self.button5.text=='O' and self.button6.text=='O':
				self.button4.background_color=(10,0,1,0.55)
				self.button5.background_color=(10,0,1,0.55)
				self.button6.background_color=(10,0,1,0.55)
				self.winner='O'
			elif self.button7.text=='O' and self.button8.text=='O' and self.button9.text=='O':
				self.button7.background_color=(10,0,1,0.55)
				self.button8.background_color=(10,0,1,0.55)
				self.button9.background_color=(10,0,1,0.55)
				self.winner='O'
			elif self.button1.text=='O' and self.button4.text=='O' and self.button7.text=='O':
				self.button1.background_color=(10,0,1,0.55)
				self.button4.background_color=(10,0,1,0.55)
				self.button7.background_color=(10,0,1,0.55)
				self.winner='O'
			elif self.button2.text=='O' and self.button5.text=='O' and self.button8.text=='O':
				self.button2.background_color=(10,0,1,0.55)
				self.button5.background_color=(10,0,1,0.55)
				self.button8.background_color=(10,0,1,0.55)
				self.winner='O'
			elif self.button3.text=='O' and self.button6.text=='O' and self.button9.text=='O':
				self.button3.background_color=(10,0,1,0.55)
				self.button6.background_color=(10,0,1,0.55)
				self.button9.background_color=(10,0,1,0.55)
				self.winner='O'
			elif self.button1.text=='O' and self.button5.text=='O' and self.button9.text=='O':
				self.button1.background_color=(10,0,1,0.55)
				self.button5.background_color=(10,0,1,0.55)
				self.button9.background_color=(10,0,1,0.55)
				self.winner='O'
			elif self.button3.text=='O' and self.button5.text=='O' and self.button7.text=='O':
				self.button3.background_color=(10,0,1,0.55)
				self.button5.background_color=(10,0,1,0.55)
				self.button7.background_color=(10,0,1,0.55)
				self.winner='O'
			else:
				pass
				
		if self.winner!=None:
			if self.play_computer==True:
				self.res.text='{} won the game'.format('You' if self.winner=='X' else 'Computer')
			else:
				self.res.text='{} won the game'.format(self.winner)
			self.play.text='Play again'
		elif self.winner==None and self.turn==9:
			self.winner='Draw'
			self.res.text='Game drawn'
			self.play.text='Play again'
	
	
	def computer(self):
		if self.winner==None:
			text=(self.button1.text,self.button2.text,self.button3.text,self.button4.text,self.button5.text,self.button6.text,self.button7.text,self.button8.text,self.button9.text)
			button=(self.button1,self.button2,self.button3,self.button4,self.button5,self.button6,self.button7,self.button8,self.button9)
			
			if self.difficulty_level=='Easy':
				import easy as c
			if self.difficulty_level=='Medium':
				import medium as c
			if self.difficulty_level=='Hard':
				import hard as c
			
			
		
		
		
			computer_choice=c.computer_turn(button,text,self.turn)
			computer_choice.text='O'
			self.turn+=1
			self.result()
		
		
		
	def Button_pressed(self,button):
		if self.play_computer==False:
			if self.winner!=None:
				pass
			elif self.check==True and button.text==' ':
				button.text='X'
				self.check=False
				self.turn+=1
				self.result()
			elif self.check==False and button.text==' ':
				button.text='O'
				self.check=True
				self.turn+=1
				self.result()
			else:
				pass
		elif self.play_computer==True:
			if self.winner!=None:
				pass
			elif button.text==' ':
				button.text='X'
				self.turn+=1
				self.result()
				self.computer()
				
	def play_again(self,instance):
			self.check=True
			self.turn=0
			self.winner=None
			self.button1.text=' '
			self.button2.text=' '
			self.button3.text=' '
			self.button4.text=' '
			self.button5.text=' '
			self.button6.text=' '
			self.button7.text=' '
			self.button8.text=' '
			self.button9.text=' '
			self.button1.background_color=(1,1,240/255,0)
			self.button2.background_color=(1,1,240/255,0)
			self.button3.background_color=(1,1,240/255,0)
			self.button4.background_color=(1,1,240/255,0)
			self.button5.background_color=(1,1,240/255,0)
			self.button6.background_color=(1,1,240/255,0)
			self.button7.background_color=(1,1,240/255,0)
			self.button8.background_color=(1,1,240/255,0)
			self.button9.background_color=(1,1,240/255,0)
			self.res.text=' '
		
			
			self.play.text='Reset'
			
			
class myapp(App):
	def build(self):
		return mygrid()

if __name__=='__main__':
	myapp().run()