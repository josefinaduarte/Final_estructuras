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