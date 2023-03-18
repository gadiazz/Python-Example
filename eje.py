def miF(a=None,b=None,c=None):
    print("Dentro de funcion")
    def miF_1():
        print("Dentro de subFuncion_1: a or b or c >=0")
    def miF_2():
        print("Dentro de subFuncion_2: a or b or c <0")
    def miF_3():
        print("Funcion de subFuncion_3: None (Sin parametros)")
    try:
        if a==None or b==None or c==None:
            miF_3()
        if a>=0 or b>=0 or c >=0:
            miF_1()
        else:
            miF_2()
    except TypeError or NameError or ValueError:
        print("Error corregido:" , TypeError)
    finally:
        print("Fin del programa...Linea FINALLY")

 