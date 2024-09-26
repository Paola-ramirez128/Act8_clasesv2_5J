print("Clases v2 Paola Ramirez 22308051281284 ")
# Zona de clases 
class Datos:
    # El constructor es una funcion
    def __init__(self, estatura, peso ):
        self.estatura = estatura
        self.peso = peso
    def mostrar_datos(self):
      print(f"Tu estatura es de: {self.estatura}mts, su peso {self.peso}kg")
    def mi_lista1284(self):
        Bandas=[ "Slipknot", "Mago de oz", "PXNDX", "Zoe"]
        print(Bandas)
        for x in Bandas:
            print(x)
    def mi_tupla1284(self):
        Canciones =("Labios rotos", "Aquelarre", "3+1")
        for c in Canciones:
            print(c)
    def mi_set1284(self):
        Dias = {"Lunes", "Martes", "Miercoles", "Jueves"}
        for d in Dias:
            print(d)
    def mi_diccionario1284(self):
        Tela = { "Color:" : "Verde", "Tipo:": "Seda", "Patron:": "Ninguno"}
        for t, a in Tela.items():
            print(t,a)
#Creacion de objeto
info = Datos(1.56, 63)

# Utilizando el objeto e informacion
info.mostrar_datos()
print("Lista de Bandas -Paola Ramirez 1284")
info.mi_lista1284()
print("Lista de canciones-Paola Ramiez 1284")
info.mi_tupla1284()
print("Dias de la semanas-Paola Ramirez 1284")
info.mi_set1284()
print("Tipos de telas-Paola Ramirez 1284")
info.mi_diccionario1284()