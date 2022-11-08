# Classe que contem funções do tkinter
import func as f
# Biblioteca tkinter
from tkinter import *
from evap_atm import balanco_evap_atm

# Classe principal
class AtmosfericEvaporator:

    # Método inicializador
    # Inicializa os atributos da classe
    def __init__(self, cont, temp, megFrac, entrada, vapor, liquido,
                 funcao):
        self.cont = cont # Conteiner princial
        self.temp = temp # Temperatura
        self.megFrac = megFrac
        self.entrada = entrada
        self.vapor = vapor
        self.liquido = liquido
        self.resp_vapor = None
        self.resp_liquido = None

        self.funcao = funcao
         
    # Método que adiciona a imagem do evaporador na tela principal
    def draw(self, img, x, y):
        
        evap = f.image(img, self.cont, x, y) # Imagem do evaporador

        # Ao dar dois clicks na imagem, chama o metodo info_window
        evap.bind('<Double-Button-1>', self.info_window)

    # Método que cria uma nova tela e recebe o valor de temperatura
    def info_window(self, event):
        self.n = Tk() # Nova tela
        self.n.geometry("200x150+140+300")
        self.n.title('Evaporador Atmosf\u00E9rico')

        # Conteiners
        cont1 = f.container(self.n)
        cont2 = f.container(self.n)
        cont3 = f.container(self.n)
        cont4 = f.container(self.n)

        # Recebe o valor de temperatura
        f.text(cont1, 'Temperatura (\u00B0C)', LEFT)
        self.txt1 = f.txt_box(cont1, 10, self.temp, RIGHT, state=NORMAL)
        
        # Recebe o valor de meg
        f.text(cont2, 'MEG Saida (% m/m*)', LEFT)
        self.txt2 = f.txt_box(cont2, 10, self.megFrac, RIGHT, 
            state=NORMAL)

        # Ao clicar no botão, chama o método change_value
        bt1 = f.button(cont4, 'ok', LEFT)
        bt1['command'] = self.change_value

    # Metodo que recebe o valor de temperatura fornecido pelo usuario
    def change_value(self):
        self.temp = float(self.txt1.get())
        self.megFrac = float(self.txt2.get())

        self.update()
        self.funcao()
        self.n.destroy() # Fecha a tela info_window
    
    def update(self):
        self.vapor.temp = self.liquido.temp = self.temp

        resp = balanco_evap_atm(self.temp,
                                self.megFrac/100, 
                                self.entrada.fracMasMEG, 
                                self.entrada.fracMasAgua,
                                self.entrada.fracMasSal, 
                                self.entrada.flow)

        self.resp_vapor, self.resp_liquido = resp
        self.vapor.atribuicao(self.resp_vapor)
        self.liquido.atribuicao(self.resp_liquido)
        self.liquido.change_label()
