
import random
import curses

class Food_Snake:

	def __init__(self):
		print("nada")
		

	def pintar_comida(self,stdscr):

		self.x_pos=random.randint(8,70)
		self.y_pos=random.randint(5,20)
		tipo=random.randint(1,50)

		x=self.x_pos
		y=self.y_pos
		malo="*"
		bueno="+"

		if tipo <=5:
			stdscr.addstr(int(y),int(x),malo)
			return str(malo)


		else:
			stdscr.addstr(int(y),int(x),bueno)
			return str(bueno)


	def get_xcomida(self):
		
		xcomida=self.x_pos
		return xcomida

	def get_ycomida(self):
		
		ycomida=self.y_pos
		return ycomida


	def pintar_obstaculos(self,stdscr):

		self.obs_x=random.randint(8,70)
		self.obs_y=random.randint(5,20)

		bad="E"
		obsx=self.obs_x
		obsy=self.obs_y

		stdscr.addstr(int(obsy),int(obsx),bad)

		return str(bad)


	def get_obsx(self):

		a=self.obs_x
		return a


	def get_obsy(self):

		b=self.obs_y
		return b
	

