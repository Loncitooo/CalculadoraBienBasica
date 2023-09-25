from tkinter import *
import tkinter as tk
#Creamos una ventana con su titulo
ventana = Tk()
ventana.title("Calculdora Chida")
#ventana.iconbitmap('C:\\Users\\lonci\\Downloads\\CalculadoraBasica\\gatolente.ico')
#ventana.configure(bg='white')

#Creamos un indice
i = 0

#Creamos una entrada de texto, entry nos permite ingresar cualquier texto de la linea
entrada_T = Entry(ventana, font=("arial 20"))

#Para mostrarlo en pantalla usamos nuestro elemento "grid", el "padx" es el espacio que va a existir entre la ventana y el widget
entrada_T.grid(row = 0, column = 0, columnspan = 4, padx =30, pady = 30)

#Añadimos las funciones para cada boton
#Agregamos una funcion de click boton para cuando le demos click nos de el valor.

def click_boton (valor):
    #accesamos la variable
    global i
    entrada_T.insert(i, valor)
    #cada vez que se meta un valor lo aumentamos por 1
    i += 1

    #definimos la variable de borrar
def borrar():
    #para borrar utilizamos nuestro comando "delete"
    #Lo que hace esta función es borra desde el indice "0" hasta el final que en este caso utilizamos la variable "end"
    #Entonces con esto lo que hacemos es resetear nuestro "i" a "0" para cuando queramos ingresar nuestros valores sean desde el inicio
    
    entrada_T.delete(0, END)
    i = 0
    
    #definimos variables para hacer las operaciones
def hacer_operacion():
    ecuacion = entrada_T.get()
    resultado = eval(ecuacion)
    entrada_T.delete(0, END)
    entrada_T.insert(0,resultado)
    i = 0

#en tkinter si queremos conectar nuestro boton a una función usamos "command" para ello.
#el problema del command es que para pasar la función debe de quedar sin parentesis, entonces para solucionarlo usamos "lambda"
#Lambda nos permite escribir una función en una linea
#Creamos nuestros botones
label1=Label(ventana, text="Ingresa Los numeros a desear")
label1.place(x=100, y=5)
boton1 = Button(ventana, text= "1", width= 5, height= 2, command= lambda: click_boton(1))
boton2 = Button(ventana, text= "2", width= 5, height= 2, command= lambda: click_boton(2))
boton3 = Button(ventana, text= "3", width= 5, height= 2, command= lambda: click_boton(3))
boton4 = Button(ventana, text= "4", width= 5, height= 2, command= lambda: click_boton(4))
boton5 = Button(ventana, text= "5", width= 5, height= 2, command= lambda: click_boton(5))
boton6 = Button(ventana, text= "6", width= 5, height= 2, command= lambda: click_boton(6))
boton7 = Button(ventana, text= "7", width= 5, height= 2, command= lambda: click_boton(7))
boton8 = Button(ventana, text= "8", width= 5, height= 2, command= lambda: click_boton(8))
boton9 = Button(ventana, text= "9", width= 5, height= 2, command= lambda: click_boton(9))
boton0 = Button(ventana, text= "0", width= 13, height= 2, command= lambda: click_boton(0))

boton_borrar = Button(ventana, text= "AC", width= 5, height= 2, command= lambda: borrar())
boton_parentesis1 = Button(ventana, text= "(", width= 5, height= 2, command= lambda: click_boton("("))
boton_parentesis2 = Button(ventana, text= ")", width= 5, height= 2, command= lambda: click_boton(")"))
boton_punto = Button(ventana, text= ".", width= 5, height= 2, command= lambda: click_boton("."))

boton_division = Button(ventana, text= "/", width= 5, height= 2, command= lambda: click_boton("/"))
boton_multiplicacion = Button(ventana, text= "x", width= 5, height= 2, command= lambda: click_boton("*"))
boton_suma = Button(ventana, text= "+", width= 5, height= 2, command= lambda: click_boton("+"))
boton_resta = Button(ventana, text= "-", width= 5, height= 2, command= lambda: click_boton("-"))
boton_igual = Button(ventana, text= "=", width= 5, height= 2, command= lambda: hacer_operacion())

#Agregaremos los botones en pantalla
boton_borrar.grid(row = 1, column= 0, padx= 5, pady= 5 )
boton_parentesis1.grid(row = 1, column= 1, padx= 5, pady= 5 )
boton_parentesis2.grid(row = 1, column= 2, padx= 5, pady= 5 )
boton_division.grid(row = 1, column= 3, padx= 5, pady= 5 )

boton7.grid(row = 2, column= 0, padx= 5, pady= 5 )
boton8.grid(row = 2, column= 1, padx= 5, pady= 5 )
boton9.grid(row = 2, column= 2, padx= 5, pady= 5 )
boton_multiplicacion.grid(row = 2, column= 3, padx= 5, pady= 5 )

boton4.grid(row = 3, column= 0, padx= 5, pady= 5 )
boton5.grid(row = 3, column= 1 , padx= 5, pady= 5 )
boton6.grid(row = 3, column= 2, padx= 5, pady= 5 )
boton_suma.grid(row = 3, column= 3, padx= 5, pady= 5 )

boton1.grid(row = 4, column= 0, padx= 5, pady= 5 )
boton2.grid(row = 4, column= 1, padx= 5, pady= 5 )
boton3.grid(row = 4, column= 2, padx= 5, pady= 5 )
boton_resta.grid(row = 4, column= 3, padx= 5, pady= 5 )

boton0.grid(row = 5, column= 0, columnspan = 2,  padx= 5, pady= 5 )
boton_punto.grid(row = 5, column= 2, padx= 5, pady= 5 )
boton_igual.grid(row = 5, column= 3, padx= 5, pady= 5 )



#Creamos un mainloop este funciona para, reconoce todo los eventos que sucedan
ventana.mainloop()
