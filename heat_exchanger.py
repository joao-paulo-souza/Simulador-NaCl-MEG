# Classe que contem funções do tkinter
import func as f
# Biblioteca tkinter
from tkinter import *
from calculos import definido_Cs
from auxiliar import number_formatter
from modelos import Solub


# Classe principal
class HeatExchanger:

    # Método inicializador
    # Inicializa os atributos da classe
    def __init__(self, cont, temp_saida, megFrac, flow, pre_entrada,
                 entrada, saida, funcao):
        self.cont = cont  # Conteiner princial

        self.temp_saida = temp_saida
        self.megFrac = megFrac
        self.flow = flow
        self.salConc = None

        self.entrada = entrada
        self.saida = saida
        self.pre_entrada = pre_entrada
        #self.temp_entrada = self.entrada.temp

        self.funcao = funcao

    # Método que adiciona a imagem do evaporador na tela principal
    def draw(self, img, x, y):
        evap = f.image(img, self.cont, x, y)  # Imagem do evaporador

        # Ao dar dois clicks na imagem, chama o metodo info_window
        evap.bind('<Double-Button-1>', self.info_window)

    # Método que cria uma nova tela e recebe o valor de temperatura
    def info_window(self, event):
        self.n = Tk()  # Nova tela
        self.n.geometry("300x200+140+300") 
        self.n.title('Aquecedor de reciclo')

        # Conteiners
        cont0 = f.container(self.n)
        cont1 = f.container(self.n)
        cont2 = f.container(self.n)
        #cont3 = f.container(self.n)
        cont4 = f.container(self.n)
        cont5 = f.container(self.n)

        # Recebe o valor de temperatura
        f.text(cont0, 'Temperatura entrada (\u00B0C)', LEFT)
        self.txt0 = f.txt_box(cont0, 10,
                              number_formatter(self.entrada.temp, '.1f'),
                              RIGHT, state=DISABLED)

        # Recebe o valor de temperatura
        f.text(cont1, 'Temperatura sa\u00EDda (\u00B0C)', LEFT)
        self.txt1 = f.txt_box(cont1, 10, self.temp_saida, RIGHT,
                              state='enable')

        f.text(cont2, 'MEG (% m/m*)', LEFT)
        self.txt2 = f.txt_box(cont2, 10, self.megFrac, RIGHT, state=NORMAL)

        f.text(cont4, 'Vazao massa (kg/h)', LEFT)
        self.txt4 = f.txt_box(cont4, 10, self.flow, RIGHT, state=NORMAL)

        # Ao clicar no botao, chama o metodo change_value
        bt1 = f.button(cont5, 'ok', LEFT)
        bt1['command'] = self.change_value

    # Metodo que recebe o valor de temperatura fornecido pelo usuario
    def change_value(self):
                
        self.temp_saida = float(self.txt1.get())
        self.megFrac = float(self.txt2.get())
        self.flow = float(self.txt4.get())

        self.update()
        self.funcao()
        self.n.destroy()  # Fecha a tela info_window
    
    def update(self):

        #self.temp_entrada = self.entrada.temp
        self.saida.temp = self.temp_saida

        self.salConc = Solub(self.entrada.temp, float(self.megFrac)/100)

        resp_entrada = definido_Cs(float(self.entrada.temp),
         float(self.megFrac)/100, 
         float(self.salConc), 
         float(self.flow))
        
        resp_saida = definido_Cs(float(self.saida.temp),
         float(self.megFrac)/100, 
         float(self.salConc), 
         float(self.flow))
        
        self.entrada.atribuicao(resp_entrada)
        self.pre_entrada.atribuicao(resp_entrada)
        self.saida.atribuicao(resp_saida)

        self.entrada.change_label()
        self.saida.change_label()
