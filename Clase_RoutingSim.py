from Clase_Lista import *
from Clase_Router import *
from Clase_paquete import *
from datetime import *
import matplotlib.pyplot as plt

mensaje1=Paquete(1,"Hola como estas",1,3,"24/03/2023, 11:11:11")
mensaje2=Paquete(1,"chau",2,3,"24/03/2023, 11:11:11")
mensaje3=Paquete(1,"bhikuhl",1,2,"24/03/2023, 16:11:11")
mensajes=[mensaje1,mensaje2,mensaje3]
router1=Router(1)
router2=Router(2)
router3=Router(3)
routers=Lista()

class RoutingSim():
    def __init__(self,tiempo,mensajes,routers):
        #defina los eventos
        self.tiempo=tiempo
        self.mensajes=mensajes
        self.routers=routers
        #arranca threat

        inicio = datetime.now

        threading_emails = threading.Thread(target=self.generador_paquetes, args=(lista, inicio)) #lista de mensajes

    # Lo lanzo

        threading_emails.start()

            ## generar paquetes aleatorios cada tiempo aleatorio

            ## romper router cada tiempo aleatorio
            
        fin = datetime.now()
        timer = (fin- inicio)
        while timer < tiempo:
            while evento == False and  timer < tiempo:

                if len(self.mensajes) > 0:
                    evento = True

            men = self.mensajes.pop(0)
            #soluciono el evento
            #enviar men
            Lista.transmitir_msj(men)
            evento = False



    def enviar_paquete(self,r,paquete):
        ##espera que se libere el router
        while r.estado != 'inactivo'or ocupado:
            pass
        ## espero por la latencia

    def generador_paquetes(self , lista, inicio):
        fin = datetime.now()
        while tiempo > fin- inicio:
            #tiempo aleatorio
            time_sleep(randint((fin- inicio),tiempo))
            ##genero paquete aleatorio

            ##agreguo paquete en la lista mensajes



            fin = time.now()



    def mostrar_tasas(self):
        for router in self.routers:
            print("Router "+str(router.posicion)+":")
            print("Tasa de paquetes enviados: "+str(router.enviados/self.tiempo))
            print("Tasa de paquetes recibidos: "+str(router.recibidos/self.tiempo))

    def grafico(self):
        lista_enviados=[]
        lista_recibidos=[]
        lista_routers=[]
        for router in self.routers:
            lista_routers.append("Router "+str(router.posicion))
            lista_enviados.append(router.enviados)
            lista_recibidos.append(router.recibidos)
        print(routers)
        print(lista_enviados,lista_recibidos)
        plt.title(label="Cantidad de paquetes enviados por router")
        plt.xlabel("Routers")
        plt.ylabel("Cantidad de paquetes enviados")
        plt.bar(lista_routers,lista_enviados,color="green",width=0.5)
        plt.show()
        plt.title(label="Cantidad de paquetes recibidos por router")
        plt.xlabel("Routers")
        plt.ylabel("Cantidad de paquetes recibidos")
        plt.bar(lista_routers,lista_recibidos,color="blue",width=0.5)
        plt.show()

    def crear_archivos_routers():
        pass

    def crear_archivo_cambioa_estado():
        pass
    
    def baipass():
        pass

if __name__=="__main__":
    pass