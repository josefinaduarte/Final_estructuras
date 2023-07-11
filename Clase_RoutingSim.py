from Clase_Lista import *
from Clase_Router import *
from Clase_paquete import *
from datetime import *
import matplotlib.pyplot as plt
from collections import deque
from funciones import *

class RoutingSim():
    def __init__(self,tiempo,paquetes,routers):
        self.tiempo=tiempo
        self.paquetes=paquetes
        self.routers=routers
        #arranca threat

        inicio = datetime.now()
        threading_generarpaq = threading.Thread(target=self.generador_paquetes, args=( inicio,)) #lista de mensajes

    # Lo lanzo

        threading_generarpaq.start()
        
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
            tiempo_random = randint(1, min(tiempo_restante, 7))

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

    


if __name__=="__main__": 
    
    try:
        tiempo=int(input("Ingrese por cuanto tiempo quiere correr la simulacion: "))
        while tiempo<=0:
            tiempo=int(input("Ingrese por cuanto tiempo quiere correr la simulacion: "))
    except ValueError:
        print("El tiempo ingresado no es valido")
        tiempo=int(input("Ingrese por cuanto tiempo quiere correr la simulacion: "))
               


    router1=Router(tiempo,1)
    router2=Router(tiempo,2)
    router3=Router(tiempo,3)
    router4=Router(tiempo,4)
    router5=Router(tiempo,5)
    router6=Router(tiempo,6)
    routers=Lista()
    routers.append(router1)
    routers.append(router2)
    routers.append(router3)
    routers.append(router4)
    routers.append(router5)
    routers.append(router6)

    paquetes = deque()
    Simulacion = RoutingSim(tiempo,paquetes,routers)
    Simulacion.mostrar_tasas()
    Simulacion.grafico()
