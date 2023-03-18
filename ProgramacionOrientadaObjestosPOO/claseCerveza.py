#CLASE SIN ATRIBUTOS PROTEGIDOS (PUBLICO)
#================================================================================================================================
class Drink1:
    def __init__(self, name):
        self.name = name
    def getDetail(self):
        return "la bebida es:" +  self.name
    
##drink = Drink("Cerveza")    
#print(drink.name)
#print(drink.getDetail())

#===============================================================================================================================
#CLASE CON ATRIBUTOS PROTEGIDOS (PRIVADOS)
class Drink2:
    #Constructor
    def __init__(self, name):
        self.__name = name
    #Metodos propios
    def getDetail(self):
        return "la bebida tiene nombre: " +  self.__name + "\n"

drink2 = Drink2("Cerveza_2")
#print(drink2.name)             # NO SE PUEDE ACCEDER A NAME
#print(Drink2.getDetail())
#=========================================================================================================
class Product():
    def __init__(self,cost,price):
        self.cost = cost
        self.price = price
    def getGain(self):
        return self.price - self.cost
#============================================================================================================
#HERENCIA DE LA CLASE BEBIDA ( DRINK ) y DE LA CLASE PRODUCTO ESTE ES UNA MULTI-CLASE HIJA  
class Beer(Drink2, Product): 
    #ELENTOS PROPIOS DE LA CLASE Y NO DEL OBJECTO (ESTATICOS)
    count = 0

    def __init__(self, name, brand, alcohol, cost, price):
        #super().__init__(name) #<<<--------- Para herencia de una sola clase
        Drink2.__init__(self,name) #CONSTRUCTOR SUPER PARA LA PRIMER CLASE PADRE
        Product.__init__(self,cost, price) #CONSTRUCTOR SUPER PARA LA SEGUNDA CLASE PADRE  
        self.__brand = brand #marca
        self.__alcohol = alcohol
        Beer.count += 1   #cada vez se crea un objeto se incrementa el contador
    #SOBREESCRITURA DE METODO PROPIO (es decir no utilizamos el del padre sino el propio)
    def getDetail(self):
        return "soy un hijo con metodo sobreescrito "
    def getDetail2(self): #el metodo super().getDetail() llama al padre para obtener su metodo de clase y no de objeto <-----
        return super().getDetail()  + "soy un hijo llamando el metodo super().getDetail() del padre" + " de la marca " + self.__brand + " con alcohol " + str(self.__alcohol) + " tiene un costo de fabricación = " + str(self.cost)  + ", precio de = " + str(self.price)
    #METODOS ESTATICOS  (SON PROPIOS DE LA CLASE Y NO DEL OBJECTO)
    @staticmethod
    def getClassInfo():
        return "Se han creado " +str(Beer.count)+ " objetos"
    
beer1 = Beer("POKER", "Bavaria", 4.5, 15, 20)
print(beer1.getDetail(), beer1.getDetail2())

beer2 = Beer("AGUILA", "Bavaria", 5.6, 12 , 28)
print(beer1.getDetail(),beer2.getDetail2())
print(Beer.count, Beer.getClassInfo(),  "\n"+ "Ganancia de: " + str(beer2.getGain()))