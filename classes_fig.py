from constantes_tela import pasta
from tkinter import *


class Fig_Equipamento(object):

	def __init__(self, x, y, num_tagid, tela, area):
		self.tela = tela
		self.area = area
		self.x = x/100*tela.winfo_width()
		self.y = y/100*tela.winfo_height()
		self.num_tagid = num_tagid
		self.tagid = 'GEN-' + str(num_tagid)
		self.imagem = PhotoImage(file=pasta + 'figuras/' + 'tanque.gif')
		self.tipo = 'generico'
		self.ponto = {}

	def exibir(self):
		figura = Label(self.tela, image=self.imagem)
		figura.imagem = self.imagem
		larg, alt = figura.winfo_reqwidth(), figura.winfo_reqheight()
		self.area.create_window(self.x, self.y, window=figura)
		xcanvas = self.area.canvasx(self.x)
		ycanvas = self.area.canvasy(self.y)
		self.ponto.update(posicoes(xcanvas, ycanvas, larg, alt))


class Fig_Separador(Fig_Equipamento):

	def __init__(self, x, y, num_tagid, tela, area):
		super().__init__(x, y, num_tagid, tela, area)
		#self.x = x/100*tela.winfo_width()
		#self.y = y/100*tela.winfo_height()
		#self.num_tagid = num_tagid
		self.tagid = 'SEP-' + str(num_tagid)
		self.imagem = PhotoImage(file=pasta + 'figuras/' + 'separador-LP.gif')
		self.tipo = 'separador'


class Fig_Bomba(Fig_Equipamento):

	def __init__(self, x, y, num_tagid, tela, area, lado):
		super().__init__(x, y, num_tagid, tela, area)
		#self.x = x/100*tela.winfo_width()
		#self.y = y/100*tela.winfo_height()
		#self.num_tagid = num_tagid
		self.tagid = 'CP-' + str(num_tagid)
		self.imagem = PhotoImage(file=pasta + 'figuras/' + 'bomba-' + lado + '.gif')
		self.tipo = 'bomba ' + str(lado)


class Fig_Filtro(Fig_Equipamento):

	def __init__(self, x, y, num_tagid, tela, area):
		super().__init__(x, y, num_tagid, tela, area)
		#self.x = x/100*tela.winfo_width()
		#self.y = y/100*tela.winfo_height()
		#self.num_tagid = num_tagid
		self.tagid = 'FIL-' + str(num_tagid)
		self.imagem = PhotoImage(file=pasta + 'figuras/' + 'filtro.gif')
		self.tipo = 'filtro'


class Fig_Trocador(Fig_Equipamento):

	def __init__(self, x, y, num_tagid, tela, area):
		super().__init__(x, y, num_tagid, tela, area)
		#self.x = x/100*tela.winfo_width()
		#self.y = y/100*tela.winfo_height()
		#self.num_tagid = num_tagid
		self.tagid = 'HT-' + str(num_tagid)
		self.imagem = PhotoImage(file=pasta + 'figuras/' + 'trocador.gif')
		self.tipo = 'trocador'


class Fig_Trocador_Meg(Fig_Equipamento):

	def __init__(self, x, y, num_tagid, tela, area):
		super().__init__(x, y, num_tagid, tela, area)
		#self.x = x/100*tela.winfo_width()
		#self.y = y/100*tela.winfo_height()
		#self.num_tagid = num_tagid
		self.tagid = 'HT-' + str(num_tagid)
		self.imagem = PhotoImage(file=pasta + 'figuras/' + 'trocador-meg.gif')
		self.tipo = 'trocador meg'


class Fig_Aquecedor(Fig_Equipamento):

	def __init__(self, x, y, num_tagid, tela, area):
		super().__init__(x, y, num_tagid, tela, area)
		#self.x = x/100*tela.winfo_width()
		#self.y = y/100*tela.winfo_height()
		#self.num_tagid = num_tagid
		self.tagid = 'HT-' + str(num_tagid)
		self.imagem = PhotoImage(file=pasta + 'figuras/' + 'aquecedor.gif')
		self.tipo = 'aquecedor'


class Fig_Evaporador(Fig_Equipamento):

	def __init__(self, x, y, num_tagid, tela, area):
		super().__init__(x, y, num_tagid, tela, area)
		#self.x = x/100*tela.winfo_width()
		#self.y = y/100*tela.winfo_height()
		#self.num_tagid = num_tagid
		self.tagid = 'EATM-' + str(num_tagid)
		self.imagem = PhotoImage(file=pasta + 'figuras/' + 'evap-atm.gif')
		self.tipo = 'evaporador atm'

	def exibir(self):

		figura = Label(self.tela, image=self.imagem)
		figura.imagem = self.imagem
		larg, alt = figura.winfo_reqwidth(), figura.winfo_reqheight()
		self.area.create_window(self.x, self.y, window=figura)
		xcanvas = self.area.canvasx(self.x)
		ycanvas = self.area.canvasy(self.y)
		self.ponto.update(posicoes(xcanvas, ycanvas, larg, alt))	
		
		xno, yno = self.ponto['no']
		xne, yne = self.ponto['ne']
		p1, p2, p3 = 0.20, 0.7, 0.8
		esq1 = (xno, int(yno + p1*alt))
		esq2 = (xno, int(yno + p2*alt))
		esq3 = (xno, int(yno + p3*alt))
		dir1 = (xne, int(yne + p1*alt))
		dir2 = (xne, int(yne + p2*alt))
		dir3 = (xne, int(yne + p3*alt))
		extras = {'esquerda1':esq1, 'esquerda2':esq2, 'esquerda3':esq3,
		          'direita1':dir1, 'direita2':dir2, 'direita3':dir3}
		self.ponto.update(extras)


class Fig_Flash(Fig_Equipamento):

	def __init__(self, x, y, num_tagid, tela, area):
		super().__init__(x, y, num_tagid, tela, area)
		#self.x = x/100*tela.winfo_width()
		#self.y = y/100*tela.winfo_height()
		#self.num_tagid = num_tagid
		self.tagid = 'FSH-' + str(num_tagid)
		self.imagem = PhotoImage(file=pasta + 'figuras/' + 'evap-vacuo.gif')
		self.tipo = 'flash'

	def exibir(self):

		figura = Label(self.tela, image=self.imagem)
		figura.imagem = self.imagem
		larg, alt = figura.winfo_reqwidth(), figura.winfo_reqheight()
		self.area.create_window(self.x, self.y, window=figura)
		xcanvas = self.area.canvasx(self.x)
		ycanvas = self.area.canvasy(self.y)
		self.ponto.update(posicoes(xcanvas, ycanvas, larg, alt))	
		
		xno, yno = self.ponto['no']
		xne, yne = self.ponto['ne']
		p1, p2, p3, p4, p5 = 0.15, 0.55, 0.7, 0.8, 0.9
		esq1 = (xno, int(yno + p1*alt))
		esq2 = (xno, int(yno + p2*alt))
		esq3 = (xno, int(yno + p3*alt))
		esq4 = (xno, int(yno + p4*alt))
		esq5 = (xno, int(yno + p5*alt))
		dir1 = (xne, int(yne + p1*alt))
		dir2 = (xne, int(yne + p2*alt))
		dir3 = (xne, int(yne + p3*alt))
		dir4 = (xne, int(yne + p4*alt))
		dir5 = (xne, int(yne + p5*alt))
		extras = {'esquerda1':esq1, 'esquerda2':esq2, 'esquerda3':esq3,
		          'esquerda4':esq4, 'esquerda5':esq5, 'direita1':dir1,
				  'direita2':dir2, 'direita3':dir3, 'direita4':dir4,
				  'direita5':dir5}
		self.ponto.update(extras)


class Fig_Torre(Fig_Equipamento):

	def __init__(self, x, y, num_tagid, tela, area):
		super().__init__(x, y, num_tagid, tela, area)
		#self.x = x/100*tela.winfo_width()
		#self.y = y/100*tela.winfo_height()
		#self.num_tagid = num_tagid
		self.tagid = 'DES-' + str(num_tagid)
		self.imagem = PhotoImage(file=pasta + 'figuras/' + 'torre.gif')
		self.tipo = 'destilacao'


class Fig_Compressor(Fig_Equipamento):

	def __init__(self, x, y, num_tagid, tela, area):
		super().__init__(x, y, num_tagid, tela, area)
		#self.x = x/100*tela.winfo_width()
		#self.y = y/100*tela.winfo_height()
		#self.num_tagid = num_tagid
		self.tagid = 'COMP-' + str(num_tagid)
		self.imagem = PhotoImage(file=pasta + 'figuras/' + 'compressor.gif')
		self.tipo = 'compressor'


class Fig_Tanque(Fig_Equipamento):

	def __init__(self, x, y, num_tagid, tela, area):
		super().__init__(x, y, num_tagid, tela, area)
		#self.x = x/100*tela.winfo_width()
		#self.y = y/100*tela.winfo_height()
		#self.num_tagid = num_tagid
		self.tagid = 'SEP-' + str(num_tagid)
		self.imagem = PhotoImage(file=pasta + 'figuras/' + 'tanque.gif')
		self.tipo = 'tanque'


def posicoes(x0, y0, larg, alt):
	
	centro = (x0, y0)
	nortex, nortey = x0, y0 - alt//2
	sulx, suly = x0, y0 + alt//2
	lestex, lestey = x0 + larg//2, y0
	oestex, oestey = x0 - larg//2, y0

	norte = (nortex, nortey)
	sul = (sulx, suly)
	leste = (lestex, lestey)
	oeste = (oestex, oestey)

	ne = (lestex, nortey)
	no = (oestex, nortey)
	se = (lestex, suly)
	so = (oestex, suly)

	pontos = {'norte': norte, 'sul': sul, 'leste': leste, 'oeste': oeste,
	          'ne': ne, 'no': no, 'se': se, 'so': so, 'centro': centro}

	return pontos