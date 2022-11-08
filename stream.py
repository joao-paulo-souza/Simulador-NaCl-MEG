# Classe que contêm funções do tkinter
import func as f
from calculos import definido_Cs
from auxiliar import number_formatter
from constantes_tela import prop_list, stream_props, texto, formato, tela_props

# Biblioteca gráfica
from tkinter import *

# Classe principal
class Stream:

    # Método inicializador
    # Inicializa os parametros da classe
    def __init__(self, cont, prop_dict, funcao=None, enabled=None, ok_button=FALSE):

        self.prop_dict_keys = prop_dict.keys()
        self.cont = cont  # Conteiner princial
        self.enabled = enabled
        
        for prop in prop_list:
            if prop in prop_dict:
                setattr(self, prop, prop_dict[prop])
            else:
                setattr(self, prop, '')

        self.state = {}  # Estado que habilita editar os campos de texto
        self.posicao = {}
        self.others_props = []

        for i, prop in enumerate(tela_props):
            self.posicao[prop] = i
            self.state[prop] = DISABLED
            if prop not in prop_dict:
                self.others_props.append(prop)

        if self.enabled is not None:
            for prop in enabled: 
                self.state[prop] = NORMAL

        self.funcao = funcao
        self.ok_button = ok_button
        self.texto_corrente = '\n\nNaCl - mg/kg'

    # Método que coloca na tela o texto do stream
    def draw(self, txt, x, y, anchor='center'):
        self.window_name = txt
        self.x = x
        self.y = y
        self.texto = txt
        self.label = Label(self.cont, text=txt)
        self.label.place(x=x, y=y, anchor=anchor)  # Recebe a posição xy

        # Ao receber dois clicks chama o metodo info_window
        self.label.bind('<Double-Button-1>', self.info_window)

        # Método que abre uma nova tela

    def info_window(self, event):
        self.n = Tk()  # Nova tela
        self.n.geometry("300x500+50+70")
        self.n.title(self.window_name)

        cont = []
        for i in range(14):
            cont.append(f.container(self.n))

        contBt = f.container(self.n)

        self.txt = {}
        for i, item in enumerate(stream_props):
            prop = item[0]
            f.text(cont[i], texto[prop], LEFT)
            valor_txt = number_formatter(getattr(self, prop), formato[prop])
            self.txt[prop] = f.txt_box(
                                cont[i], 
                                10, 
                                valor_txt, 
                                RIGHT, 
                                self.state[prop])

        if self.enabled is not None:
            for enabled_prop in self.enabled:
                self.txt[enabled_prop].bind("<KeyRelease>", self.on_key_pressing)

        if self.ok_button:
            bt1 = f.button(contBt, 'ok', LEFT)  # Botão
            # Ao receber um click chama a o método change_value
            bt1['command'] = self.change_value
            # bt1.bind('<Return>', self.change_value)

    # Método que recebe os valores dos campos de texto e atualiza 
    # os valores de Pressão, temperatura e fração molar
    def change_value(self):

        self.temp = float(self.txt['temp'].get())
        self.pres = float(self.txt['pres'].get())
        self.megFrac = float(self.txt['megFrac'].get())
        self.salConc = float(self.txt['salConc'].get())
        self.flow = float(self.txt['flow'].get())

        props_calc = definido_Cs(
                        self.temp,
                        self.megFrac/100,
                        self.salConc,
                        self.flow)

        self.atribuicao(props_calc)
        self.change_label()
        self.funcao()
                        
        # Fecha a tela info_window
        self.n.destroy()
    
    def change_label(self):
        parte1 = '\n\nTemp {:.1f} \u00B0C'.format(self.temp)
        parte2 = '\nMEG* {:.2f} %'.format(self.megFrac)
        parte3 = '\nNaCl* {:.0f} mg/kg'.format(self.salConc)
        parte4 = '\nSólidos {:.2f} kg/h'.format(self.vazMasSalSoli)
        self.texto_corrente = parte1 + parte2 + parte3 + parte4
        
        if self.salConc > 0:
            
            self.label['text'] = self.texto + self.texto_corrente
        

    # Método test
    def on_key_pressing(self, event):

        check_valores = True
        valores = []
        for prop in self.enabled:
            try:
                valor = float(self.txt[prop].get())
                valores.append(valor)
                setattr(self, prop, valor)
            except:
                check_valores = False
                break

        if check_valores and all([valor >= 0 for valor in valores]):

            props_calc = definido_Cs(
                                self.temp,
                                self.megFrac/100,
                                self.salConc,
                                self.flow)

            self.atribuicao(props_calc)

            for prop in self.others_props:
                valor = props_calc[prop]
                self.txt[prop].configure(state='enable')
                self.txt[prop].delete(0, END)
                valor_txt = '{0:{1}}'.format(valor, formato[prop])
                self.txt[prop].insert(END, valor_txt)
                self.txt[prop].configure(state='disabled')                    

        else:

            for prop in self.others_props:
                self.txt[prop].configure(state='enable')
                self.txt[prop].delete(0, END)
                self.txt[prop].insert(END, '')
                self.txt[prop].configure(state='disabled')
    
    def atribuicao(self, props_calc):

        for prop, valor in props_calc.items():
            setattr(self, prop, valor)

        self.megFrac = 100*self.megFrac
