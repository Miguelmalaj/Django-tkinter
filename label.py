from tkinter import *

# Configuración de la raíz
root = Tk()
"""
# Variables dinámicas
texto = StringVar()
texto.set("Un nuevo texto")

Label(root, text="hello world").pack(anchor="nw")
label = Label(root, text="hello world")
label.pack(anchor="center")
Label(root, text="hello world").pack(anchor="se")


label.config(bg="green", fg="blue", font=("Verdana", 24))
label.config(textvariable=texto)
"""

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")

# Finalmente bucle de la aplicación
root.mainloop()