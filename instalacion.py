from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.font import Font



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def test():
    print("hola mundo")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1440x980")
window.configure(bg="#FFFFFF")

# Fuente a utilizar
f_font = "Arial Nova"

title_font = Font(family=f_font, size=18)
sbtl_font = Font(family=f_font, size=14)
gnrl_font = Font(family=f_font, size=10)

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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    36.0,
    70.0,
    image=image_image_1
)

canvas.create_text(
    590.0,
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

vc1 = tk.IntVar(checkframe)
vc2 = tk.IntVar(checkframe)

c1 = tk.Checkbutton(checkframe, text='El usuario es administrador', font=gnrl_font,
                    variable=vc1, state="disabled", bg="white")
c1.grid(column=1, row=2)

c2 = tk.Checkbutton(checkframe, text='User Account Control: Run all administrators \nin Admin Approval Mode: [Disable]', font=gnrl_font,
                    variable=vc2, state="disabled", bg="white")
c2.grid(column=2, row=2)


canvas.create_text(
    36.0,
    258.0,
    anchor="nw",
    text="OBTENCION DE ARCHIVOS A UTILIZAR",
    fill="#000000",
    font=(sbtl_font)
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
    text="Formato de fecha",
    fill="#000000",
    font=(gnrl_font)
)

canvas.create_text(
    114.0,
    508.0,
    anchor="nw",
    text="Formato No Wrap en WordPad",
    fill="#000000",
    font=(gnrl_font)
)

canvas.create_text(
    115.0,
    472.0,
    anchor="nw",
    text="Formato de numero",
    fill="#000000",
    font=(gnrl_font)
)

canvas.create_text(
    114.0,
    291.0,
    anchor="nw",
    text="WebClient",
    fill="#000000",
    font=(gnrl_font)
)

canvas.create_text(
    114.0,
    327.0,
    anchor="nw",
    text="LMS 12.2.prowcapc",
    fill="#000000",
    font=(gnrl_font)
)

canvas.create_text(
    115.0,
    359.0,
    anchor="nw",
    text="Gunzip",
    fill="#000000",
    font=(gnrl_font)
)
window.resizable(False, False)
window.mainloop()
