from tkinter import *
from manual_text import *
from constantes_tela import pasta

def manual(root):

    global count_titles
    count_titles = 0

    def title(text):
        global count_titles
        count_titles = count_titles + 1
        text = '\n' + str(count_titles) + ' - ' + text + '\n'
        index1 = 'insert - {} chars'.format(len(text) - 1)
        font = ('Helvetica', '26', 'bold')
        text_wid.configure(state=NORMAL)
        text_wid.insert('insert', text)
        text_wid.tag_add('title', index1, 'insert')
        text_wid.tag_config('title', font=font, background='yellow')
        text_wid.configure(state=DISABLED)

    def bodytext(text):
        font = ('Liberation', '12')
        text = text + '\n'
        index1 = 'insert - {} chars'.format(len(text))
        text_wid.configure(state=NORMAL)
        text_wid.insert('insert', text)
        text_wid.tag_add('bodytext', index1, 'insert')
        text_wid.tag_config('bodytext', font=font)
        text_wid.configure(state=DISABLED)

    def figure(fig):
        font = ('Liberation', '12')
        text_wid.configure(state=NORMAL)
        text_wid.insert('insert', '\n')
        text_wid.image_create('insert', image=fig)
        text_wid.insert('insert', '\n')
        text_wid.tag_add('figure', 'insert - 2 lines' , 'insert')
        text_wid.tag_config('figure', font=font, justify=CENTER)
        text_wid.configure(state=DISABLED)

    #root = Tk()
    #root.geometry('695x660+650+10')
    #root.title('Manual')

    arquivo1 = pasta + 'figuras/' + 'tela_inicial_red.gif'
    arquivo2 = pasta + 'figuras/' + 'tela_detalhe_red.gif'
    arquivo3 = pasta + 'figuras/' + 'tela_corrente_red.gif'
    arquivo4 = pasta + 'figuras/' + 'demais_telas_red.gif'
    arquivo5 = pasta + 'figuras/' + 'tela_salsolido_red.gif'
    arquivo6 = pasta + 'figuras/' + 'tela_tabela_red.gif'
    fig1 = PhotoImage(file=arquivo1)
    fig2 = PhotoImage(file=arquivo2)
    fig3 = PhotoImage(file=arquivo3)
    fig4 = PhotoImage(file=arquivo4)
    fig5 = PhotoImage(file=arquivo5)
    fig6 = PhotoImage(file=arquivo6)

    text_wid = Text(root, width=93, height=45, wrap=WORD, padx=10)
    text_wid.grid(row=0, column=0)
    text_wid.image = [fig1, fig2, fig3, fig4, fig5, fig6]

    scroll = Scrollbar(root, command=text_wid.yview, width=17)
    scroll.grid(row=0, column=1, sticky=N + S)
    text_wid.configure(yscrollcommand=scroll.set)

    title('Apresentação')
    bodytext(apresentacao)
    title('Instalação')
    bodytext(instalacao)
    title('Utilização')
    bodytext(utilizacao)
    bodytext(util_telainicial)
    figure(fig1)
    bodytext(util_teladetalhe)
    figure(fig2)
    title('Simulação')
    bodytext(corrente1)
    figure(fig3)
    bodytext(demais_valores)
    bodytext(valores_precarregados)
    figure(fig4)
    bodytext(indicacao_solido)
    figure(fig5)
    title('Menu do programa')
    bodytext(botoes)
    figure(fig6)
    bodytext(botoes2)

    #root.mainloop()
