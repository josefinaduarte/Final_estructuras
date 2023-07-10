from random import *
from time import sleep as time_sleep
from datetime import *
import csv
import threading
 
class Router():
    estados_validos = set(['agregado', 'activo', 'inactivo', 'reset'])
    def __init__(self,tiempo,posicion,estado=None,paquete=None,prox = None):  ##esta bien pasarle el tiempo y el inicio asi?
        
        inicio = datetime.now()
        # if estado not in Router.estados_validos:
        #     raise ValueError("el estado no es valido")
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


    def cambiarestado(self,estado):             #despues habria que hacer bien lo de guardar los datos en el archivo csv
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
        #escribirinfo('C:/Users/Tiziana/Documents/PRACTICA FINAL/PRACTUCA FINAL/cambiosestado.py', contenido)
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
                #archivo=r"C:\Users\Jose\Documents\facultad\Segundo año\pruebas final estructuras\hola.txt"
                
                ar=open(archivo,'a+')
                cadena="Origen: ROUTER_"+str(self.paquete.origen)+"\n"
                ar.write(cadena)
                cadena=str(self.paquete.mensaje)+"\n"
                ar.write(cadena)
                ar.close()
            except IOError:
                print("Hubo un error al abrir el archivo del router "+str(self.posicion))
    

    #creo q estos metodos ya no hacen falta
    def esta_averiado(self):
        x=bool(randint(0,1))
        return x
    
    def reset(self):
        pass

    def analizar_destino_paquete(self):         #El router analiza si el msj tiene como destino ese mismo router (si no lo es se va a transmitir)
        pass

    def transmitir_paquete(self):          #Es un metodo del router o de la lista? deberiamos incluir entre transmision y transmision el tiempo de latencia
        pass

    def cantidad_paquetes_envorec(self):        #para tener el dato de la cantidad de paquetes que recibio y envio para el grafico
        pass

