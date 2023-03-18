####=========== DEFINICION FUNCION LAMBDA ===============####################
maximo = lambda a,b,c: print(f"El maximo de {a} {b} {c} es {max(a,b,c)}") #FUNCIONA ANONIMA QUE PERMITE LLLAMAR OTRAS FUNCIONES DE PYTHON
#LLAMANDO A LA FUNCION LAMBDA: MAXIMO
num1 = maximo(2,3,4)
num2 = maximo ( 1,100,99)
# ------------> f"El maximo de {a} {b} {c} es {max(a,b,c)}" es un formato tipo STRING

def ponerPrefijo(prefijo):
    return lambda nombre: f"{prefijo} {nombre}"  #RETORNA UNA VARIABLE TIPO (LAMBDA)

####===== COMBINACION DE LA FUNCION LAMBDA DENTRO DE OTRA FUNCION

#
if __name__ == "__main__":
    #creamos varias funciones con los prefijos cargados 
    add1 = ponerPrefijo("Pequeño")
    add2 = ponerPrefijo("Gran ")
    add3 = ponerPrefijo("Don ")
    print(type(add1), type(add2), type(add3)) #ES UNA CLASE FUNCION

    #cargamos los valores a las funciones para conseguir una variable tipo STRING
    persona1 = add1("Alejandro ")
    persona2 = add2("Julian ")
    persona3 = add3("Juan ")
    print(persona1, type(persona1))
    print(persona2,type(persona2))
    print(persona3, type(persona3))