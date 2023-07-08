from Clase_Lista import *
from Clase_Router import *
from Clase_paquete import *
from datetime import *

mensaje1=Paquete(1,"Hola como estas",1,3,"24/03/2023, 11:11:11")
mensaje2=Paquete(1,"chau",2,3,"24/03/2023, 11:11:11")
mensaje3=Paquete(1,"bhikuhl",1,2,"24/03/2023, 16:11:11")
mensajes=[mensaje1,mensaje2,mensaje3]
router1=Router(1)
router2=Router(2)
router3=Router(3)
routers=[router1,router2,router3]

class RoutingSim():
    def __init__(self,tiempo,mensajes,routers):
        self.tiempo=tiempo
        self.mensajes=mensajes
        self.routers=routers

    def mostrar_tasas():
        pass

    def grafico():
        pass

    def crear_archivos_routers():
        pass

    def crear_archivo_cambioa_estado():
        pass
    
    def baipass():
        pass

if __name__=="__main__":
    pass