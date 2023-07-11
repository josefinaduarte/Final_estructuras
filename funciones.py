from Clase_Router import *
from Clase_paquete import *
from random import *
import threading


def generar_msja():
    cadena="qwertyuiopasdfghjklñzxcvbnm QWERTYUIOPASDFGHJKLÑZXCVBNM"
    mensaje=""
    long=randint(10,30)
    for i in range(long):
        pos=randint(0,len(cadena)-1)
        mensaje+=cadena[pos]
    return mensaje