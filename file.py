# import tkinter as tk
# from tkinter import ttk
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
# import pandas as pd
# from tkinter.font import Font


# root = tk.Tk()


# def seleccion():
#     global curItem
#     global title
#     curItem = tree.focus()
#     if curItem != "":
#         var.set(tree.item(curItem)['values'][0])
#         print(var.get())
#     else:
#         var.set("ULTIMA VERSION")
#         print(var.get())


# def my_treeview():
#     window = tk.Toplevel()
#     window.configure(bg="#FFFFFF")
#     window.title('VERSIONES LMS 12.2')

#     f_font = "Arial Nova"
#     title_font = Font(family=f_font, size=18)

#     title = tk.Label(window, text="Seleccion de version LMS12.2.prowcapc", font=(
#         title_font), bg="white")
#     title.place(x=90, y=0)

#     ancho_ventana = 620
#     alto_ventana = 350
#     x_ventana = window.winfo_screenwidth() // 2 - ancho_ventana // 2
#     y_ventana = window.winfo_screenheight() // 2 - alto_ventana // 2
#     posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
#         "+" + str(x_ventana) + "+" + str(y_ventana)
#     window.geometry(posicion)

#     versiones = pd.read_html('http://jumxlmsl03/lms/versiones/')
#     versiones = versiones[0].iloc[2:]
#     versiones = versiones.iloc[::, 1:]
#     versiones = versiones.iloc[:-1:]
#     columns = versiones.columns.tolist()
#     columns.pop()
#     columns.pop()

#     # Tabla
#     global tree
#     global var
#     tableframe = tk.Frame(window)
#     tableframe.place(x=100, y=40)

#     tree = ttk.Treeview(tableframe, columns=columns, show='headings')
#     tree.heading('Name', text='Nombre')
#     tree.heading('Last modified', text='Ultima modificacion')
#     tree.grid(row=0, column=0, sticky=tk.NSEW)

#     for x in versiones.index:
#         if x != 29:
#             tree.insert('', tk.END, values=(
#                 versiones["Name"][x][:-1], versiones["Last modified"][x], versiones["Size"][x], versiones["Description"][x]), iid=x)
#         else:
#             tree.insert('', tk.END, values=(
#                 "ULTIMA VERSION", versiones["Last modified"][x], versiones["Size"][x], versiones["Description"][x]), iid=x)

#     scrollbar = ttk.Scrollbar(
#         tableframe, orient=tk.VERTICAL, command=tree.yview)
#     tree.configure(yscroll=scrollbar.set)
#     scrollbar.grid(row=0, column=1, sticky='ns')

#     var = tk.StringVar()
#     var.set("ULTIMA VERSION")

#     # Boton
#     boton = tk.Button(
#         window,
#         text="ACTUALIZAR VERSION",
#         bg="#C13737",
#         fg='#FFFFFF',
#         borderwidth=1,
#         highlightthickness=0,
#         command=seleccion,
#         relief="flat",
#         width=20,
#         height=2)
#     boton.place(x=50, y=290)

#     x_text = 240
#     title_version = tk.Label(window, text="VERSION\nSELECCIONADA:", bg="white")
#     title_version.place(x=x_text, y=280)
#     version = tk.Label(window, textvariable=var, bg="white")
#     version.place(x=x_text, y=320)

#     boton = tk.Button(
#         window,
#         text="ACEPTAR",
#         bg="#C13737",
#         fg='#FFFFFF',
#         borderwidth=1,
#         highlightthickness=0,
#         command=seleccion,
#         relief="flat",
#         width=20,
#         height=2)
#     boton.place(x=360, y=290)


# treeview = tk.Button(root, text="open treeview", command=my_treeview).pack()

# root.mainloop()
