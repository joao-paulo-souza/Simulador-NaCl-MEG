# -*- coding: cp1252 -*-
# Classe que contem funções do tkinter
import func as f
# Biblioteca tkinter
from tkinter import *
from sep_flash import balanco_sep_flash
from calculos import definido_Cs

# Classe principal
class VacuumEvaporator:

    # Método inicializador
    # Inicializa os atributos da classe
    def __init__(self, cont,
                 temp_vapor, temp_salmoura, 
                 megFrac_vapor, entrada, vapor, liquido,
                 reciclo_baixa_pressao, reciclo_alta_pressao, 
                 funcao, fator_evaporacao):

        self.cont = cont  # Conteiner princial
        self.temp_vapor = temp_vapor  # Temperatura
        self.temp_salmoura = temp_salmoura  # Temperatura
        self.megFrac_vapor = megFrac_vapor

        self.entrada = entrada
        self.vapor = vapor
        self.liquido = liquido

        self.reciclo_baixa_pressao = reciclo_baixa_pressao
        self.reciclo_alta_pressao = reciclo_alta_pressao

        self.resp_vapor = None
        self.resp_liquido = None
        self.fator_evaporacao = fator_evaporacao

        self.funcao = funcao

    # Método que adiciona a imagem do evaporador na tela principal
    def draw(self, img, x, y):
        draw = f.image(img, self.cont, x, y)  # Imagem do evaporador

        # Ao dar dois clicks na imagem, chama o metodo info_window
        draw.bind('<Double-Button-1>', self.info_window)

    # Método que cria uma nova tela e recebe o valor de temperatura
    def info_window(self, event):
        self.n = Tk()  # Nova tela
        self.n.geometry("350x200+140+300")  
        self.n.title('Evaporador \u00E0 V\u00E1cuo')

        # Conteiners
        cont1 = f.container(self.n)
        cont2 = f.container(self.n)
        cont3 = f.container(self.n)

        # Recebe o valor de temperatura
        f.text(cont1, 'Temperatura vapor (\u00B0C)', LEFT)
        self.txt1 = f.txt_box(cont1, 10, self.temp_vapor, RIGHT, 
                              state=NORMAL)

        # Recebe o valoR
        f.text(cont2, 'Temperatura salmoura (\u00B0C)', LEFT)
        self.txt2 = f.txt_box(cont2, 10, self.temp_salmoura, RIGHT, 
                              state=NORMAL)

        # Ao clicar no botao, chama o metodo change_value
        bt1 = f.button(cont3, 'ok', LEFT)
        bt1['command'] = self.change_value

    #
    def change_value(self):
        self.temp_vapor = float(self.txt1.get())
        self.temp_salmoura = float(self.txt2.get())

        self.update()
        self.funcao()
        self.n.destroy()  # Fecha a tela info_window

    def update(self):

        self.reciclo_baixa_pressao.temp = self.temp_vapor
        self.reciclo_alta_pressao.temp = self.temp_vapor
        self.vapor.temp = self.temp_vapor
        self.liquido.temp = self.temp_salmoura
        self.megFrac_vapor = self.entrada.megFrac

        dados = [self.entrada.fracMasMEG, self.entrada.fracMasSal, 
                 self.entrada.flow]
        resp = balanco_sep_flash(self.temp_vapor, self.temp_salmoura,
                                 dados, self.megFrac_vapor/100, 
                                 self.fator_evaporacao)

        self.resp_vapor, self.resp_liquido = resp

        self.vapor.atribuicao(self.resp_vapor)
        self.liquido.atribuicao(self.resp_liquido)
        self.liquido.change_label()
