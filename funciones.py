from Clase_Router import *
from Clase_paquete import *
from random import *
import threading

def accion_pasarpaq(router,nodosiguiente):
    if router.estado=="activo":
                    router.guardar_datospaquete()
                    nodosiguiente.paquete=router.paquete
                    router.paquete=None
                    router.enviados+=1
                    #pondria threath para cambiar estado
                    threading_cambiarestado = threading.Thread(target=router.cambiarestado, args=("inactivo",))
                    threading_cambiarestado.start()

def generar_msja():
    cadena="qwertyuiopasdfghjklñzxcvbnm QWERTYUIOPASDFGHJKLÑZXCVBNM"
    mensaje=""
    long=randint(10,30)
    for i in range(long):
        pos=randint(0,len(cadena)-1)
        mensaje+=cadena[pos]
    return mensaje