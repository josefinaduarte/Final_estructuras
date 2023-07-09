from Clase_Router import *
from Clase_paquete import *
from random import *
import threading
##en este clase deberia ir algo del pasaje del paquete?

class Lista():
    def __init__(self):
        self.head = None
        self.len = 0
    def agregarinicio(self, nodo=Router):
        if(self.len==0): #averiguamos la longitud de mi lista. Si es =0 quiere decir que la lista esvacia, por lo que el head estará direccionada al nodo
            self.head=nodo
            #self.len+=1
        else:
            nodo.prox=self.head
            self.head=nodo
            #self.len+=1
        self.len+=1
    def __str__(self):
        nodo=self.head
        cadena=''
        if self.len==0:
            return('Lista Vacia')
        else:
            while nodo!=None:
                cadena+=str(nodo.posicion)+'\t'+str(nodo.estado)+'\t'+str(nodo.recibidos)+'\t'+str(nodo.enviados)+'\t'
                if nodo.paquete==None:
                    cadena+="vacio"+'\n'
                else:
                    cadena+=str(nodo.paquete.mensaje)+'\n'
                nodo=nodo.prox
            return cadena
    def append(self,nodo=Router):
        if(self.len==0):
            self.head=nodo
        else:
            nodomov=Router()
            nodomov=self.head
            while(nodomov.prox!=None):
                nodomov=nodomov.prox
            nodomov.prox=nodo
        self.len+=1
        nodo.cambiarestado('agregado')
    def pop(self,pos=None):
        nodo=Router()
        nodo=self.head
        if pos==None:
            final=self.len-2
            for i in range(final):
                nodo=nodo.prox
            nodo.prox=None
        else:
            for i in range(pos-1):
                nodo=nodo.prox
            nodo.prox=nodo.prox.prox
        self.len-=1
    def transmitir_msj(self,router:Router):
        while router.paquete.destino!=router.posicion:
            nodosiguiente=router.prox
            if router.paquete.destino!=router.posicion and nodosiguiente.estado!="inactivo" and nodosiguiente.estado!="reset":
                if router_activo:
                    router.guardar_datospaquete()
                    nodosiguiente.paquete=router.paquete
                    router.paquete=None
                    router.enviados+=1
                    #pondria threath para cambiar estado
                    threading_emails = threading.Thread(target=router.cambiarestado, args=("inactivo",))
                    threading_emails.start()
                    # router.cambiarestado('inactivo')

                    # if router.esta_averiado==True:
                    #     router.cambiarestado('reset')
                router=router.prox
            elif nodosiguiente.estado=="inactivo":
                pass
            elif nodosiguiente.estado=="reset":
                pass
            # si el nodo siguiente esta apagado o inactivo, y es el nodo de destino
            elif (nodosiguiente.estado=="reset" or  nodosiguiente.estado=="inactivo") and nodosiguiente.estado==router.paquete.destino:
                while nodosiguiente.estado=="reset" or  nodosiguiente.estado=="inactivo":
                    pass
                ## envio

        router.recibidos+=1
        router.guardar_datospaquete()

[1,2,3,4,5,6]

mensaje1=Paquete(1,"Hola como estas",1,3,"24/03/2023, 11:11:11")
mensaje2=Paquete(2,"chau",2,3,"24/03/2023, 11:11:11")
mensaje3=Paquete(3,"bhikuhl",1,2,"24/03/2023, 16:11:11")
mensajes=[mensaje1,mensaje2,mensaje3]
# router1=Router(1)
# router2=Router(2)
# router3=Router(3)
router1=Router(1)
router2=Router(2)
router3=Router(3)
routers=[router1,router2,router3]
if __name__=="__main__":
    lista=Lista()
    lista.append(router1)
    lista.append(router2)
    lista.append(router3)
    router1.paquete=mensaje1
    print(lista)
    lista.transmitir_msj(router1)
    print(lista)

# router1=Router(1,'agregado', None,None,None,None,None)
# router2=Router(2,None,None,None,None,None,None)
# router3=Router(3,None,None,None,None,None,None)