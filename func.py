from tkinter import *
from tkinter.ttk import *
from constantes_tela import pasta
# from PIL import Image, ImageTk


def container(r):
    Style().configure("TFrame") #background="#333"
    c = Frame(master=r)
    c.pack(fill=BOTH, expand=1)

    return c


def button(cont, txt, side):
    bt = Button(cont, text=txt)
    bt.pack(side=side)

    return bt


def text(cont, txt, side):
    txt = Label(cont, text=txt)
    txt.pack(side=side)

    return txt


def txt_box(cont, w, txt, side, state):
    box = Entry(cont, width=w)
    box.insert(END, txt)
    box.pack(side=side)
    box.configure(state=state)
    return box


def box_value(box):
    value = box.get()

    return value


def canvas(r, w, h, x, y):
    c = Canvas(master=r, highlightthickness=0,  width=w, height=h)
    c.place(x=x, y=y)

    return c


def image(img, c, x, y):
    #img_open = Image.open(img)
    #photo = ImageTk.PhotoImage(img_open)
    photo = PhotoImage(file=pasta + 'figuras/' + img)
    p = photo.subsample(2, 2)
    label = Label(c, image=p) # background='#333'
    label.image = p
    label.place(x=x, y=y)

    return label

