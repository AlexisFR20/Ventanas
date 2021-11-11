import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.font import Font
from pathlib import Path
import rutines
import ctypes
import os
from sys import exit
import json
import shutil


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def test():
    print("hola mundo")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.configure(bg="#FFFFFF")
ancho_ventana = 1000
alto_ventana = 1000
x_ventana = window.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = window.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
    "+" + str(x_ventana) + "+" + str(y_ventana)
window.geometry(posicion)

# Configuraciones de botones a utilizar
flag_wClient = True
flag_lmsp = True
flag_fzip = True
flag_fecha = True
flag_fnumber = True
flag_lenguaje = True
flag_wrap = True
ajuste_x_btn = 400


# Fuente a utilizar
f_font = "Arial Nova"
title_font = Font(family=f_font, size=18)
sbtl_font = Font(family=f_font, size=14)
gnrl_font = Font(family=f_font, size=10)

on = PhotoImage(file="assets/on24.png")
off = PhotoImage(file="assets/off24.png")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1000,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    36.0,
    70.0,
    image=image_image_1
)

canvas.create_text(
    400.0,
    57.0,
    anchor="nw",
    text="INSTALACION LMS",
    fill="#000000",
    font=(title_font)
)

canvas.create_text(
    36.0,
    117.0,
    anchor="nw",
    text="VERIFICACION DE PERMISOS",
    fill="#000000",
    font=(sbtl_font)
)


checkframe = tk.Frame(window, bg="white", )
checkframe.place(x=60, y=158)


def is_disabled():
    try:
        rutines.editHost()
        c2.select()
    except:
        c2.deselect()


def is_admin():
    is_admin = False
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if(is_admin):
        c1.select()
    else:
        c1.deselect()


def check():
    is_disabled()
    is_admin()


vc1 = tk.IntVar(checkframe)
vc2 = tk.IntVar(checkframe)

c1 = tk.Checkbutton(checkframe, text='El usuario es administrador', font=gnrl_font,
                    variable=vc1, state="disabled", bg="white")
c1.grid(column=1, row=2)

c2 = tk.Checkbutton(checkframe, text='User Account Control: Run all administrators \nin Admin Approval Mode: [Disable]', font=gnrl_font,
                    variable=vc2, state="disabled", bg="white")
c2.grid(column=2, row=2)

button_1 = Button(
    text="Verificacion",
    borderwidth=0,
    highlightthickness=0,
    command=check,
    relief="flat",
    bg="#C13737",
    fg='#FFFFFF'
)

button_1.place(
    x=560,
    y=170,
    width=150,
    height=20
)

button_2 = Button(
    text="Instalacion",
    borderwidth=0,
    highlightthickness=0,
    # command=installLMS,
    relief="flat",
    bg="#C13737",
    fg='#FFFFFF'
)

button_2.place(
    x=720,
    y=170,
    width=150,
    height=20
)

canvas.create_text(
    36.0,
    258.0,
    anchor="nw",
    text="OBTENCION DE ARCHIVOS A UTILIZAR",
    fill="#000000",
    font=(sbtl_font)
)



canvas.create_text(
    114.0,
    291.0,
    anchor="nw",
    text="WebClient",
    fill="#000000",
    font=(gnrl_font)
)
def Switch(btn):
    global flag_wClient
    global flag_lmsp
    global flag_fzip
    global flag_fecha
    global flag_fnumber
    global flag_lenguaje
    global flag_wrap
    if btn == "wClient":
        if flag_wClient:
            btn_wClient.config(image=off)
            flag_wClient = False
        else:
            btn_wClient.config(image=on)
            flag_wClient = True
    if btn == "lmsp":
        if flag_lmsp:
            btn_lmsp.config(image=off)
            flag_lmsp = False
        else:
            btn_lmsp.config(image=on)
            flag_lmsp = True
    if btn == "gzip":
        if flag_gzip:
            btn_gzip.config(image=off)
            flag_gzip = False
        else:
            btn_gzip.config(image=on)
            flag_gzip = True
    if btn == "fecha":
        if flag_fecha:
            btn_fecha.config(image=off)
            flag_fecha = False
        else:
            btn_fecha.config(image=on)
            flag_fecha = True
    if btn == "fnumber":
        if flag_fnumber:
            btn_fnumber.config(image=off)
            flag_fnumber = False
        else:
            btn_fnumber.config(image=on)
            flag_fnumber = True
    if btn == "lenguaje":
        if flag_lenguaje:
            btn_lenguaje.config(image=off)
            flag_lenguaje = False
        else:
            btn_lenguaje.config(image=on)
            flag_lenguaje = True
    if btn == "wrap":
        if flag_wrap:
            btn_wrap.config(image=off)
            flag_wrap = False
        else:
            btn_wrap.config(image=on)
            flag_wrap = True


btn_wClient = Button(
    image=on,
    bd=0,
    command=Switch("wClient"),
    bg="#FFFFFF",
    fg='#FFFFFF',
    width=22,
    height=12
)
btn_wClient.place(
    x=ajuste_x_btn,
    y=291
)

canvas.create_text(
    114.0,
    327.0,
    anchor="nw",
    text="LMS 12.2.prowcapc",
    fill="#000000",
    font=(gnrl_font)
)

btn_lmsp = Button(
    image=on,
    bd=0,
    command=Switch("lmsp"),
    bg="#FFFFFF",
    fg='#FFFFFF',
    width=22,
    height=12
)
btn_lmsp.place(
    x=ajuste_x_btn,
    y=327
)


canvas.create_text(
    115.0,
    359.0,
    anchor="nw",
    text="Gunzip",
    fill="#000000",
    font=(gnrl_font)
)

btn_gzip = Button(
    image=on,
    bd=0,
    command=Switch("gzip"),
    bg="#FFFFFF",
    fg='#FFFFFF',
    width=22,
    height=12
)
btn_gzip.place(
    x=ajuste_x_btn,
    y=359
)

canvas.create_text(
    32.0,
    407.0,
    anchor="nw",
    text="CONFIGURACIONES DE SISTEMA",
    fill="#000000",
    font=(sbtl_font)
)

canvas.create_text(
    114.0,
    441.0,
    anchor="nw",
    text="Ajuste en Formato de fecha",
    fill="#000000",
    font=(gnrl_font)
)

btn_fecha = Button(
    image=on,
    bd=0,
    command=Switch("fecha"),
    bg="#FFFFFF",
    fg='#FFFFFF',
    width=22,
    height=12
)
btn_fecha.place(
    x=ajuste_x_btn,
    y=441
)

canvas.create_text(
    115.0,
    472.0,
    anchor="nw",
    text="Ajuste en Formato de numero",
    fill="#000000",
    font=(gnrl_font)
)
btn_fnumber = Button(
    image=on,
    bd=0,
    command=Switch("fnumber"),
    bg="#FFFFFF",
    fg='#FFFFFF',
    width=22,
    height=12
)
btn_fnumber.place(
    x=ajuste_x_btn,
    y=472
)

canvas.create_text(
    114.0,
    508.0,
    anchor="nw",
    text="Ajuste en Lenguaje",
    fill="#000000",
    font=(gnrl_font)
)

btn_lenguaje = Button(
    image=on,
    bd=0,
    command=Switch("lenguaje"),
    bg="#FFFFFF",
    fg='#FFFFFF',
    width=22,
    height=12
)
btn_lenguaje.place(
    x=ajuste_x_btn,
    y=508.0
)


canvas.create_text(
    114.0,
    542.0,
    anchor="nw",
    text="Ajuste en Formato No Wrap en WordPad",
    fill="#000000",
    font=(gnrl_font)
)

btn_wrap = Button(
    image=on,
    bd=0,
    command=Switch("wrap"),
    bg="#FFFFFF",
    fg='#FFFFFF',
    width=22,
    height=12
)
btn_wrap.place(
    x=ajuste_x_btn,
    y=542
)


window.resizable(False, False)
window.mainloop()
