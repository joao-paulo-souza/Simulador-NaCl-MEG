# -*- coding: cp1252 -*-
# Classe que contem funções do tkinter
import func as f
# Biblioteca tkinter
from tkinter import *


# Classe principal
class RecirculationPump:

    # Método inicializador
    # Inicializa os atributos da classe
    def __init__(self, cont, temp):
        self.cont = cont  # Conteiner princial
        self.temp = temp  # Temperatura

    # Método que adiciona a imagem do evaporador na tela principal
    def draw(self, img, x, y):
        evap = f.image(img, self.cont, x, y)  # Imagem do evaporador

        # Ao dar dois clicks na imagem, chama o metodo info_window
        evap.bind('<Double-Button-1>', self.info_window)

    # Método que cria uma nova tela e recebe o valor de temperatura
    def info_window(self, event):
        self.n = Tk()  # Nova tela
        self.n.geometry("335x100+140+300")  
        self.n.title('Bomba de reciclo')

        # Conteiners
        cont1 = f.container(self.n)
        cont2 = f.container(self.n)

        texto = '''
            Bomba de reciclo.
        A corrente 6 tem a mesma
        composi\u00E7\u00E3o da corrente 7.'''
        Label(cont1, text=texto).pack()
        
        # Ao clicar no botão, chama o método change_value
        bt1 = f.button(cont2, 'ok', LEFT)
        bt1['command'] = self.change_value

    def change_value(self):
        
        self.n.destroy()  # Fecha a tela info_window

