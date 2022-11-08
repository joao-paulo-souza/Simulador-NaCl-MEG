from tkinter import *
from funcoes_tela import *
from constantes_tela import *
from classes_fig import *
from main_2 import principal

# interface com tkinter

class TelaInicial(object):

	def __init__(self, master):

		self.master = master

		master.update_idletasks()
		largura = master.winfo_width() - 5
		altura = master.winfo_height() - 5

		area = Canvas(master, height=altura, width=largura)
		area.pack()

		self.area = area
		
		separador01 = Fig_Separador(11, 24, 101, master, area)
		separador02 = Fig_Tanque(93, 10, 102, master, area)
		bomba01 = Fig_Bomba(16, 37, 101, master, area, direita)
		bomba02 = Fig_Bomba(47, 47, 102, master, area, esquerda)
		bomba03 = Fig_Bomba(58, 56, 103, master, area, esquerda)
		bomba04 = Fig_Bomba(73, 96, 104, master, area, direita)
		bomba05 = Fig_Bomba(74, 77, 105, master, area, cima)
		bomba06 = Fig_Bomba(87, 15, 106, master, area, esquerda)
		filtro01 = Fig_Filtro(23, 52, 101, master, area)
		filtro02 = Fig_Filtro(83, 43, 102, master, area)
		calor01 = Fig_Trocador_Meg(28, 50, 101, master, area)
		calor02 = Fig_Trocador(47, 33, 102, master, area)
		calor03 = Fig_Aquecedor(72, 66, 103, master, area)
		calor04 = Fig_Trocador(85, 5, 104, master, area)
		evapatm = Fig_Evaporador(58, 28, 101, master, area)
		flash = Fig_Flash(64, 75, 101, master, area)
		destil = Fig_Torre(72, 31, 101, master, area)
		comp = Fig_Compressor(96, 3, 101, master, area)

		exibir = [separador01, separador02, bomba01, bomba02, bomba03,
				  bomba04, bomba05, bomba06, filtro01, filtro02, calor01,
				  calor02, calor03, calor04, evapatm, flash, destil, comp]

		for equip in exibir:
			equip.exibir()


		lconex(separador01, sul, bomba01, oeste, area, inicio=vertical)
		
		sconex(bomba01, ne, filtro01, oeste, area, inicio=horizontal,
			   quebra=0.5)
		
		cconex(bomba02, no, calor02, oeste, area, inicio=horizontal,
			   excesso=-60)
		
		rconex(separador01, norte, area, direcao=vertical, distancia=-50)
		
		rconex(separador01, oeste, area, direcao=horizontal, distancia=-50,
		       seta=FIRST)
		
		sconex(filtro01, leste, calor01, so, area, inicio=horizontal)
		
		#linha meg pobre
		rconex(calor01, no, area, direcao=horizontal, distancia=-300) 
		
		cconex(bomba02, no, flash, esquerda1, area, inicio=horizontal,
			   excesso=-30)
		
		sconex(calor01, ne, evapatm, esquerda1, area, inicio=horizontal,
			   quebra=0.15)
		
		sconex(evapatm, esquerda3, bomba02, leste, area, inicio=horizontal,
			   quebra=0.5)
		
		area.create_line(bomba02.ponto[no],
						 (bomba02.ponto[no][0]-100, bomba02.ponto[no][1]),
						 (bomba02.ponto[no][0]-100, calor01.ponto[se][1]), 
						 fill='darkblue', arrow=LAST)
		
		sconex(calor02, leste, evapatm, esquerda2, area, inicio=horizontal,
			   quebra=0.5)
		
		lconex(bomba03, no, calor01, se, area, inicio=vertical)
		
		lconex(destil, sul, bomba03, leste, area, inicio=vertical)
		
		lconex(flash, norte, destil, so, area, inicio=vertical)
		
		lconex(destil, norte, calor04, no, area, inicio=vertical)
		
		lconex(calor04, se, separador02, oeste, area, inicio=vertical)
		
		lconex(separador02, norte, comp, oeste, area, inicio=vertical)
		
		rconex(comp, leste, area, direcao=horizontal, distancia=20)
		
		lconex(separador02, sul, bomba06, leste, area, inicio=vertical)
		
		sconex(bomba06, no, destil, ne, area, inicio=horizontal,
			   quebra=0.5)
		
		lconex(bomba06, no, filtro02, norte, area, inicio=horizontal)
		
		lconex(flash, sul, bomba04, oeste, area, inicio=vertical)
		
		#cconex(bomba04, ne, flash, direita5, area, inicio=horizontal,
			   #excesso=50)
		
		lconex(filtro02, sul, flash, direita4, area, inicio=vertical)
		
		rconex(bomba04, no, area, direcao=horizontal, distancia=200)
		
		area.create_line(filtro02.ponto[sul],
						 (filtro02.ponto[sul][0], bomba04.ponto[no][1]),
						 fill='darkblue', arrow=LAST)
		
		#cconex(bomba05, ne, flash, direita3, area, inicio=horizontal,
			    # excesso=30)
		
		lconex(flash, direita2, bomba05, oeste, area, inicio=vertical)
		
		lconex(bomba05, ne, calor03, leste, area, inicio=vertical)
		
		lconex(calor03, oeste, flash, direita1, area, inicio=vertical)

		botao = Button(master, text='Clique\naqui', command=self.utilizar,
					   background='lightblue')
		
		area.create_window(flash.x, flash.y*0.92, window=botao)

		titulo_coords = (area.canvasx(0.50*master.winfo_width()),
						 area.canvasy(0.05*master.winfo_height()))
		
		area.create_text(titulo_coords, text=titulo, font='75')
		
		coords1 = (area.canvasx(separador01.ponto[so][0]),
				   area.canvasy(separador01.ponto[so][1]+20))
		
		area.create_text(coords1, text='Separador\nTrifásico', font='20')

		coords2 = (area.canvasx(evapatm.ponto[sul][0]),
				   area.canvasy(evapatm.ponto[sul][1]+20))
		
		area.create_text(coords2, text='Evaporador\nAtmosférico',
						 font='20')
		
		coords3 = (area.canvasx(flash.ponto[oeste][0]-60),
				   area.canvasy(flash.ponto[oeste][1]))
		
		area.create_text(coords3, text='Evaporador\nFlash (23 kPa)',
		                 font='20')

		coords4 = (area.canvasx(destil.ponto[leste][0]+50),
		           area.canvasy(destil.ponto[leste][1]))
		
		area.create_text(coords4, text='Destilação', font='20')


	def utilizar(self):
		utilizacao = Toplevel(self.master)
		#TelaUtilizacao(utilizacao)
		principal(utilizacao)


# definindo objeto da classe tkinter
tela = Tk()
largura = 1300
altura = 600
tamanho = '{}x{}'.format(largura, altura)
tela.geometry(tamanho + '-55+0')
tela.title('---Solub NaClex---')

TelaInicial(tela)
tela.mainloop()
