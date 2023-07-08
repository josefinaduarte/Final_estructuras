from random import *
import time
from datetime import *

class Router():
    def __init__(self,posicion=None,estado="agregado",paquete=None,prox = None):
        self.posicion=posicion
        self.estado=estado
        self.paquete=paquete
        self.recibidos=0
        self.enviados=0
        self.prox=prox

    def __str__(self):
        pass

    def cambiarestado(self,estado):             #despues habria que hacer bien lo de guardar los datos en el archivo csv
        self.estado=estado
        fecha=date.today()
        hora=datetime.now().strftime("%H:%M:%S")
        contenido='Router_{},{}, {},{}'.format(self.posicion,fecha,hora,self.estado)
        print(contenido)
        #escribirinfo('C:/Users/Tiziana/Documents/PRACTICA FINAL/PRACTUCA FINAL/cambiosestado.py', contenido)
        if estado=='reset':
            seg=randint(5,10)
            time.sleep(seg)
            estado='activo'
            self.cambiarestado(estado)
        if estado=='inactivo':
            time.sleep(0.1)
            estado='activo'
            self.cambiarestado(estado)

    def reset(self):
        pass

    def analizar_destino_paquete(self):         #El router analiza si el msj tiene como destino ese mismo router (si no lo es se va a transmitir)
        pass

    def transmitir_paquete(self):          #Es un metodo del router o de la lista? deberiamos incluir entre transmision y transmision el tiempo de latencia
        pass

    def guardar_datospaquete(self):     #guardar los msjs de los paquetes que pasaron por el router
        pass

    def cantidad_paquetes_envorec(self):        #para tener el dato de la cantidad de paquetes que recibio y envio para el grafico
        pass