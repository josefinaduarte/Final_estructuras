from Clase_Lista import *
from Clase_Router import *
from Clase_paquete import *
from datetime import *
import matplotlib.pyplot as plt
from collections import deque
from funciones import *

# mensaje1=Paquete(1,"Hola como estas",1,3,"24/03/2023, 11:11:11")
# mensaje2=Paquete(1,"chau",2,3,"24/03/2023, 11:11:11")
# mensaje3=Paquete(1,"bhikuhl",1,2,"24/03/2023, 16:11:11")
# mensajes=[mensaje1,mensaje2,mensaje3]


class RoutingSim():
    def __init__(self,tiempo,paquetes,routers):
        #defina los eventos
        self.tiempo=tiempo
        self.paquetes=paquetes
        self.routers=routers
        #arranca threat

        inicio = datetime.now()
        threading_generarpaq = threading.Thread(target=self.generador_paquetes, args=( inicio,)) #lista de mensajes

    # Lo lanzo

        threading_generarpaq.start()

            ## generar paquetes aleatorios cada tiempo aleatorio

            ## romper router cada tiempo aleatorio
            
        fin = datetime.now()
        timer = (fin- inicio).seconds
        evento=False
        while timer < tiempo:
            while evento == False and  timer < tiempo:
                fin = datetime.now()
                timer = (fin- inicio).seconds
                if len(self.paquetes) > 0:
                    evento = True
            fin = datetime.now()
            timer = (fin- inicio).seconds
            if len(self.paquetes) > 0:
                paq = self.paquetes.pop()
                #soluciono el evento
                #enviar men
                router = routers.buscar_router(paq.origen)

                router.paquete=paq
                
                self.routers.transmitir_msj(router)
                
            evento = False



    # def enviar_paquete(self,r,paquete):
    #     ##espera que se libere el router
    #     while r.estado != 'inactivo'or ocupado:
    #         pass
    #     ## espero por la latencia

    def generador_paquetes(self, inicio):
        fin = datetime.now()
        timer = (fin- inicio).seconds

        if len(self.paquetes) == 0:
            id=0
        else:
            id=int(paquetes[-1].id)+1

        while self.tiempo > timer:
            #tiempo aleatorio
            tiempo_restante = self.tiempo - timer
            tiempo_random = randint(1, min(tiempo_restante, 10))

            time_sleep(tiempo_random)
            ##genero paquete aleatorio
            mensaje=generar_msja()
            
            orig=randint(1,self.routers.len)
            dest=randint(1,self.routers.len)
            fecha=datetime.now()
            paquete=Paquete(id,mensaje,orig,dest,fecha)
            ##agreguo paquete en la lista mensajes
            self.paquetes.append(paquete)
            timer = (fin- inicio).seconds


            fin = datetime.now()
            id +=1



    def mostrar_tasas(self):

        router = self.routers.head

        while router.prox != self.routers.head:
            print("Router "+str(router.posicion)+":")
            print("Tasa de paquetes enviados: "+str(router.enviados/self.tiempo))
            print("Tasa de paquetes recibidos: "+str(router.recibidos/self.tiempo))
            router = router.prox
        print("Router "+str(router.posicion)+":")
        print("Tasa de paquetes enviados: "+str(router.enviados/self.tiempo))
        print("Tasa de paquetes recibidos: "+str(router.recibidos/self.tiempo))

    def grafico(self):
        lista_enviados=[]
        lista_recibidos=[]
        lista_routers=[]
        router = self.routers.head

        while router.prox != self.routers.head:
            lista_routers.append("Router "+str(router.posicion))
            lista_enviados.append(router.enviados)
            lista_recibidos.append(router.recibidos)
            router = router.prox
        lista_routers.append("Router "+str(router.posicion))
        lista_enviados.append(router.enviados)
        lista_recibidos.append(router.recibidos)
        print(lista_routers)
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
    #inicializo un cola vacia
    ##Tiempo de la simulacion
    tiempo=10


    router1=Router(tiempo,1)
    router2=Router(tiempo,2)
    router3=Router(tiempo,3)
    routers=Lista()
    routers.append(router1)
    routers.append(router2)
    routers.append(router3)

    paquetes = deque()
    Simulacion = RoutingSim(tiempo,paquetes,routers)
    Simulacion.mostrar_tasas()
    Simulacion.grafico()
