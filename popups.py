from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()

def test():
    # MessageBox.showinfo("Hola!","Hola mundo")
    # MessageBox.showwarning("Alerta","Sección sólo para administradores.")
    # MessageBox.showerror("Error!","Ha ocurrido un error inesperado.")
    # resultado = MessageBox.askquestion("Salir","salir?")
    # if resultado == "yes": # "no"
    # root.destroy()
    # resultado = MessageBox.askquestion("Salir", "desea salir sin guardar?")
    # if resultado == "yes":
    # root.destroy()
    # resultado = MessageBox.askokcancel("Salir", "sobrescribir le fichero actual?")
    # resultado = MessageBox.askyesno("Salir", "sobrescribir le fichero actual?")
    # if resultado:
    # root.destroy()

    # resultado = MessageBox.askretrycancel("Reintentar", "No se puede contectar")
    # if resultado:
    # root.destroy()

    # color = ColorChooser.askcolor(title="Elige un color")
    # print(color)
    # fichero = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:",
    #     filetypes=(
    #         ("Fichero de texto", "*.txt"), 
    #         ("Fichero de texto avanzado", "*.txt2"),
    #         ("Todos los ficheros", "*.*"),
    #         ))
    # print(fichero)

    fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        fichero.write("this is a test")
        fichero.close()

Button(root, text="Clic", command=test).pack()


root.mainloop()

