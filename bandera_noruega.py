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
ventana_principal.geometry("700x500")

# deshabilitar botón de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg="white")

# ---------------------
# Frame entrada datos
# ---------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="red",width=175, height=175)
frame_entrada.place(x=0,y=0)

# ---------------------
# Frame entrada datos
# ---------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="red",width=175, height=175)
frame_entrada.place(x=0,y=325)

# ---------------------
# Frame entrada datos
# ---------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="red",width=375, height=175)
frame_entrada.place(x=325,y=0)

# ---------------------
# Frame entrada datos
# ---------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="red",width=375, height=175)
frame_entrada.place(x=325,y=325)

# ---------------------
# Frame operaciones
# ---------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="navy",width=700, height=75)
frame_operaciones.place(x=0,y=213)

# ---------------------
# Frame operaciones
# ---------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="navy",width=75, height=500)
frame_operaciones.place(x=213,y=0)



# Run
# Se ejecuta la función (metodo) mainloop de la clase Tk() a traves de la instancia ventana_principal. Este
# metodo despliega una ventana simple en la pantalla y queda a la espera de lo que el usuario haga. Esta
# acción del usuario se conoce como evento. El mainloop() es un bucle "infinito".
ventana_principal.mainloop()