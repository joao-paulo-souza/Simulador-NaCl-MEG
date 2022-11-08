# Biblioteca gráfica
from tkinter import *
from auxiliar import gerar_tabela, converter_tabela
from text_funcs import manual

# Importação de classes
import atmosferic_evaporator as a
import stream as s
import heat_exchanger as h
import recirculation_pump as r
import vacuum_evaporator as v
import func as f

#from sys import exit

# Função que fecha o programa
#def close():
#    exit(0)

def principal(root):
	#root = Tk() # Método que cria a tela principal
	#root.protocol('WM_DELETE_WINDOW', close)

	def simulation_1():

		ae1.update()
		ve1.update()
		he1.update()
		alterar_cores()

	def ajuda():

		janela2 = Toplevel(root)
		janela2.geometry('695x660+650+10')
		janela2.title('Ajuda')

		manual(janela2)

	def exibir_tabela():

		def copiar_txt():
			janela.clipboard_clear()
			janela.clipboard_append(tabela_txt)

		def copiar_csv():
			tabela_csv = converter_tabela(tabela, 'csv')
			janela.clipboard_clear()
			janela.clipboard_append(tabela_csv)

		def copiar_tex():
			tabela_tex = converter_tabela(tabela, 'tex')
			janela.clipboard_clear()
			janela.clipboard_append(tabela_tex)
					
		tabela = gerar_tabela(correntes)
		tabela_txt = converter_tabela(tabela, 'txt')
		
		janela = Toplevel(root)
		janela.geometry('1270x400+10+10')
		
		texto = Text(janela, width=1250, height=20)
		texto.insert(INSERT, tabela_txt)
		texto.configure(state=DISABLED)
		texto.pack()

		botoes = Frame(janela)
		botoes.pack()
		
		Button(botoes, text='Copiar tabela para txt',
		       command=copiar_txt).grid(row=0, column=0)
		Button(botoes, text='Copiar tabela para csv',
		       command=copiar_csv).grid(row=0, column=1)
		Button(botoes, text='Copiar tabela para tex',
		       command=copiar_tex).grid(row=0, column=2)
	
	def alterar_cores():

		for item in setas:
			if item[0].concSalSoli > 0:
				item[2].itemconfig(item[1], fill='red')
			else:
				item[2].itemconfig(item[1], fill='black')

	# Altera a geometria e posicionamento da tela
	root.geometry("800x450+330+70") 

	# Conteiner principal
	cont1 = f.container(root) 

	# Objeto Stream 1 Recebe:
	st1 = s.Stream(cont1, 
				   {'temp': 115, 'pres': 101.3, 'megFrac': 66, 'salConc': 439, 'flow': 11247}, 
				   simulation_1, 
				   ['temp', 'megFrac', 'salConc', 'flow'], 
				   TRUE)
	
	# Método que mostra o texto do stream
	st1.draw('Corrente 1', 65, 175, 'n')
	c1 = f.canvas(cont1, 110, 10, 30, 190) # Função que cria um canvas
	l1 = c1.create_line(0, 5, 110, 5, arrow=LAST) #Linhas do st1 fill='red'
	
	# Objeto Stream 2
	st2 = s.Stream(cont1, {'pres': 101.3})
	st2.draw('Corrente 2', 160, 120)
	c2 = f.canvas(cont1, 15, 100, 200, 50)
	l2 = c2.create_line(10, 100, 10, 5, arrow=LAST)
	
	# Objeto Stream 3
	st3 = s.Stream(cont1, {'pres': 101.3})
	st3.draw('Corrente 3', 295, 175, 'n')
	c3 = f.canvas(cont1, 120, 10, 247, 190) # Função que cria um canvas
	l3 = c3.create_line(0, 5, 115, 5, arrow=LAST)
	
	# Objeto Evaporador 1
	ae1 = a.AtmosfericEvaporator(cont1, 115, 66.01, st1, st2, st3,
	                             simulation_1)
	ae1.draw('EQuip01.gif', 145, 150)

	st4 = s.Stream(cont1, {'pres': 23.0})
	st4.draw('Corrente 4', 360, 70)
	c4 = f.canvas(cont1, 10, 50, 396, 50)
	l4 = c4.create_line(5, 50, 5, 5, arrow=LAST)

	st5 = s.Stream(cont1, {'pres': 150.0})
	st5.draw('Corrente 5', 360, 350, 'n')
	c5 = f.canvas(cont1, 10, 50, 396, 306)
	l5 = c5.create_line(5, 0, 5, 50, arrow=LAST)

	st6 = s.Stream(cont1, {'pres': 23.0})
	st6.draw('Corrente 6', 508, 235)
	c6 = f.canvas(cont1, 140, 10, 445, 247) # Função que cria um canvas
	l6 = c6.create_line(0, 5, 125, 5, arrow=LAST) #Linhas do st1

	rp1 = r.RecirculationPump(cont1, 0)
	rp1.draw('Equip02.gif', 575, 235)

	st7 = s.Stream(cont1, {'pres': 500.0})
	st7.draw('Corrente 7', 715, 150, 'n')
	c7 = f.canvas(cont1, 22, 130, 620, 118) # Função que cria um canvas
	l7 = c7.create_line(0, 125, 20, 125, 20, 20, 0, 20, arrow=LAST)

	st8 = s.Stream(cont1, {'pres': 120.0})

	he1 = h.HeatExchanger(cont1, 138, 97, 508902, st6, st7, st8,
	                      simulation_1)
	he1.draw('Equip04.gif', 565, 110)
		
	st8.draw('Corrente 8', 508, 122, anchor='s')
	c8 = f.canvas(cont1, 130, 10, 440, 135)
	l8 = c8.create_line(130, 5, 0, 5, arrow=LAST)

	ve1 = v.VacuumEvaporator(cont1, 127, 39, ae1.megFrac, st3, st4, st5,
	                         st6, st7, simulation_1, 0.99999)
	ve1.draw('Equip03.gif', 365, 100)

	correntes = [st1, st2, st3, st4, st5, st6, st7, st8]
	linhas = [l1, l2, l3, l4, l5, l6, l7, l8]
	quadros = [c1, c2, c3, c4, c5, c6, c7, c8]
	setas = list(zip(correntes, linhas, quadros))

	# Menu
	menu = Menu(root)
	menu.add_command(label='Tabela', command=exibir_tabela)
	menu.add_command(label='Ajuda', command=ajuda)
	#menu.add_command(label="Fechar", command=close)
	
	root.config(menu=menu)
