# Se importa la libreria tkinter con todas las funciones
from tkinter import *

# ---------------------
# Funciones de la app
# ---------------------

# ---------------------
# Ventana principal
# ---------------------

# Se declara una variable llamada ventana principal, que adquiere las caracteristicas de un objeto TK
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Sistemas UIS Socorro")

# tamaño de la ventada
ventana_principal.geometry("500x500")

# deshabilitar botón de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg="thistle4")

# ---------------------
# Frame entrada datos
# ---------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="yellow",width=500, height=250)
frame_entrada.place(x=0,y=0)

# ---------------------
# Frame operaciones
# ---------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="blue",width=500, height=125)
frame_operaciones.place(x=0,y=250)

# ---------------------
# Frame resultados
# ---------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="red",width=500, height=125)
frame_resultados.place(x=0,y=375)

# Run
# Se ejecuta la función (metodo) mainloop de la clase Tk() a traves de la instancia ventana_principal. Este
# metodo despliega una ventana simple en la pantalla y queda a la espera de lo que el usuario haga. Esta
# acción del usuario se conoce como evento. El mainloop() es un bucle "infinito".
ventana_principal.mainloop()