from tkinter import *
from constantes_tela import *


def global_2(exibir, tela, largura, altura, area):

	bot = []
	equip = []
	for item in exibir:

		x = item.x/100*largura
		y = item.y/100*altura

		bot.append(Button(tela, image=item.imagem))
		# Devido ao Garbage-Collector do Python, deve-se manter uma 
		# referencia extra da imagem obtida no PhotoImage
		# Uma maneira simples de fazer isso é criar um atributo dessa 
		# imagem para o widget em questao
		bot[-1].imagem = item.imagem
		
		larg, alt = bot[-1].winfo_reqwidth(), bot[-1].winfo_reqheight()
		equip.append(area.create_window(x, y, window=bot[-1]))
		#equip[-1].pack()

		xcanvas, ycanvas = area.canvasx(x), area.canvasy(y)
		item.ponto.update(posicoes(xcanvas, ycanvas, larg, alt)) 


def global_img(exibir, tela, largura, altura, area):

	bot = []
	equip = []
	imagem = []
	for item in exibir:

		x = item.x/100*largura
		y = item.y/100*altura

		imagem.append(PhotoImage(file=item.imagem))
		bot.append(Button(tela, image=imagem[-1]))
		# Devido ao Garbage-Collector do Python, deve-se manter uma 
		# referencia extra da imagem obtida no PhotoImage
		# Uma maneira simples de fazer isso é criar um atributo dessa 
		# imagem para o widget em questao
		bot[-1].imagem = imagem[-1]
		
		larg, alt = bot[-1].winfo_reqwidth(), bot[-1].winfo_reqheight()
		equip.append(area.create_window(x, y, window=bot[-1]))
		#equip[-1].pack()

		xcanvas, ycanvas = area.canvasx(x), area.canvasy(y)
		item.ponto = posicoes(xcanvas, ycanvas, larg, alt)


def unidade_img(item, tela, largura, altura, area):
	x = item.x/100*largura
	y = item.y/100*altura

	imagem = PhotoImage(file=item.imagem)
	bot = Button(tela, image=imagem)
	larg, alt = bot.winfo_reqwidth(), bot.winfo_reqheight()

	equip = area.create_window(x, y, window=bot)
	xcanvas, ycanvas = area.canvasx(x), area.canvasy(y)

	item.ponto = posicoes(xcanvas, ycanvas, larg, alt)


def unidade_tex(item, tela, largura, altura, area):
	x = item.x/100*largura
	y = item.y/100*altura

	bot = Button(tela, text=item.tagid)
	larg, alt = bot.winfo_reqwidth(), bot.winfo_reqheight()

	equip = area.create_window(x, y, window=bot)
	xcanvas, ycanvas = area.canvasx(x), area.canvasy(y)

	item.ponto = posicoes(xcanvas, ycanvas, larg, alt)


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


def lconex(eq1, lado1, eq2, lado2, area, inicio=horizontal):
	x0, y0 = eq1.ponto[lado1]
	x1, y1 = eq2.ponto[lado2]

	curva_horiz = (x1, y0)
	curva_vert = (x0, y1)

	if inicio == horizontal:
		area.create_line((x0, y0), curva_horiz, (x1, y1),
		                 fill='darkblue', arrow=LAST)
	else:
		area.create_line((x0, y0), curva_vert, (x1, y1),
		                 fill='darkblue', arrow=LAST)


def sconex(eq1, lado1, eq2, lado2, area, inicio=horizontal, quebra=0.5):
	x0, y0 = eq1.ponto[lado1]
	x1, y1 = eq2.ponto[lado2]
	dist_h = int(quebra*(x1 - x0))
	dist_v = int(quebra*(y1 - y0))

	if inicio == horizontal:
		curva_1 = (x0 + dist_h, y0)
		curva_2 = (x0 + dist_h, y1)
	else:
		curva_1 = (x0, y0 + dist_v)
		curva_2 = (x1, y0 + dist_v)

	area.create_line((x0, y0), curva_1, curva_2, (x1, y1),
	                 fill='darkblue', arrow=LAST)


def cconex(eq1, lado1, eq2, lado2, area, inicio=horizontal,
           seta=LAST, excesso=25):
	x0, y0 = eq1.ponto[lado1]
	x1, y1 = eq2.ponto[lado2]
	dist = int(excesso)

	if inicio == horizontal:
		curva_1 = (x0 + dist, y0)
		curva_2 = (x0 + dist, y1)
	else:
		curva_1 = (x0, y0 + dist)
		curva_2 = (x1, y0 + dist)
	
	area.create_line((x0, y0), curva_1, curva_2, (x1, y1),
	                 fill='darkblue', arrow=seta)


def rconex(eq1, lado1, area, eq2=NONE, lado2=NONE, direcao=horizontal,
           seta=LAST, distancia=50):
	x0, y0 = eq1.ponto[lado1]

	if eq2 == NONE or lado2 == NONE:

		if direcao == horizontal:
			x1, y1 = x0 + distancia, y0
		else:
			x1, y1 = x0, y0 + distancia

	else:
		x1, y1 = eq2.ponto[lado2]

	area.create_line((x0, y0), (x1, y1), fill='darkblue', arrow=seta)
