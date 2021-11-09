# Librerias a utilizar
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.font import Font
# from instalacion import ventana

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# -----------------------> FUNCIONES <-----------------------


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def installLMS():
    # ventana(OUTPUT_PATH, ASSETS_PATH)
    print("INSTALACION")


def confDRP():
    print("DRP")


def resetLMS():
    print("RESET LMS")


# -----------------------> VENTANA PRINCIPAL <-----------------------
# Declaracion de la ventana
window = Tk()
# Medidas y color de la ventana
window.geometry("1440x980")
window.configure(bg="#FFFFFF")

# Fuente a utilizar
f_font = "Arial Nova"
btn_font = Font(family=f_font, size=14)

# Fondo blanco de la ventana en general
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=980,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Boton de INSTALACION
button_1 = Button(
    text="RESET LMS",
    borderwidth=0,
    highlightthickness=0,
    command=resetLMS,
    relief="flat",
    font=btn_font,
    background="#C13737",
    fg='#FFFFFF'
)
button_1.place(
    x=784.0,
    y=613.0,
    width=300.0,
    height=43.0
)

# Boton de CONFIGURACION DRP
button_2 = Button(
    text="CONFIGURACION DRP",
    borderwidth=0,
    highlightthickness=0,
    command=confDRP,
    relief="flat",
    font=btn_font,
    background="#C13737",
    fg='#FFFFFF'
)
button_2.place(
    x=784.0,
    y=512.0,
    width=300.0,
    height=43.0
)


# Boton de RESET LMS
button_3 = Button(
    text="INSTALACION",
    borderwidth=0,
    highlightthickness=0,
    command=installLMS,
    relief="flat",
    font=btn_font,
    bg="#C13737",
    fg='#FFFFFF'


)
button_3.place(
    x=784.0,
    y=411.0,
    width=300.0,
    height=43.0
)

# LADO ROJO DE LA VENTANA PRINCIPAL
canvas.create_rectangle(
    0.0,
    0.0,
    720.0,
    980.0,
    fill="#B70000",
    outline="")
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    756.0,
    90.0,
    image=image_image_1
)

# Titulo CONFIGURACION LMS de la ventana
canvas.create_text(
    881.0,
    245.0,
    anchor="nw",
    text="CONFIGURACION LMS",
    fill="#000000",
    font=(f_font, 36 * -1)
)

# Se desactiva el ajuste del tamaño de la ventana
window.resizable(False, False)

# Se ejecuta y abre la ventana
window.mainloop()
