from random import *
from time import sleep as time_sleep
from datetime import *
import csv
import threading
 
class Router():
    
    def __init__(self,tiempo,posicion,estado=None,paquete=None,prox = None):  ##esta bien pasarle el tiempo y el inicio asi?
        
        inicio = datetime.now()
        self.posicion=posicion
        self.estado=estado
        self.paquete=paquete
        self.recibidos=0
        self.enviados=0
        self.prox=prox

        #arrancas el threath que lo rompe cada tanto
        threading_caidas = threading.Thread(target=self.caidas, args=(tiempo,inicio))
        threading_caidas.start()

    def caidas(self,tiempo,inicio):
        fin = datetime.now()
        while tiempo > (fin- inicio).seconds:
            #tiempo aleatorio
            tiempo_restante = (tiempo - (fin- inicio).seconds)-10 # por el timepo maximo que tarda en resetearse
            if tiempo_restante > 0:
                time_sleep(randint(0,min(0,tiempo_restante)))
                if self.paquete==None:
                    self.cambiarestado('reset')
                fin = datetime.now()


    def __str__(self):
        if self.paquete==None:
            paq="vacio"
        else:
            paq=self.paquete.mensaje
        if self.estado==None:
            est="-"
        else:
            est=self.estado
        if self.posicion==None:
            pos="-"
        else:
            pos=self.posicion
        return 'La posicion del Router es {} , su estado es {}, su paquete es {}'.format(pos,est,paq)


    def cambiarestado(self,estado):             
        self.estado=estado
        fecha=date.today()
        hora=datetime.now().strftime("%H:%M:%S")
        contenido=['Router_{}'.format(self.posicion),fecha,hora,self.estado]
        try:
            with open('system_log.csv', 'a+', newline='') as archivo_csv:
                writer = csv.writer(archivo_csv)
                writer.writerow(contenido)
        except:
            print("Hubo un error con el archivo")
        
        if estado=='reset':
            seg=randint(5,10)
            time_sleep(seg)
            estado='activo'
            self.cambiarestado(estado)
        if estado=='inactivo':
            time_sleep(0.1)
            estado='activo'
            self.cambiarestado(estado)

    def guardar_datospaquete(self):     #guardar los msjs de los paquetes que pasaron por el router
        if self.paquete!=None:
            try:
                archivo="Router_"+str(self.posicion)+".txt"
               
                
                ar=open(archivo,'a+')
                cadena="Origen: ROUTER_"+str(self.paquete.origen)+"\n"
                ar.write(cadena)
                cadena=str(self.paquete.mensaje)+"\n"
                ar.write(cadena)
                ar.close()
            except IOError:
                print("Hubo un error al abrir el archivo del router "+str(self.posicion))
    

    
   