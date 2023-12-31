from Clase_Router import *
from Clase_paquete import *
from random import *
import threading


class Lista():
    def __init__(self):
        self.head = None
        self.len = 0
    def agregarinicio(self, nodo=Router):
        if(self.len==0): #averiguamos la longitud de mi lista. Si es =0 quiere decir que la lista esvacia, por lo que el head estará direccionada al nodo
            self.head=nodo
            
        else:
            nodo.prox=self.head
            self.head=nodo
            
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
            nodo.prox=self.head  #conectar el final con la cabeza
        else:
            
            nodomov=self.head
            while(nodomov.prox!=self.head):
                nodomov=nodomov.prox
            nodomov.prox=nodo
            nodo.prox=self.head      #conectar el final con la cabeza
        self.len+=1
        nodo.cambiarestado('agregado')
        nodo.cambiarestado('activo')
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
            if  nodosiguiente.estado!="inactivo" and nodosiguiente.estado!="reset" and nodosiguiente.estado!="agregado":
                
                if router.estado=="activo":
                    router.guardar_datospaquete()
                    nodosiguiente.paquete=router.paquete
                    router.paquete=None
                    router.enviados+=1
                    threading_cambiarestado = threading.Thread(target=router.cambiarestado, args=("inactivo",))
                    threading_cambiarestado.start()
                    router=router.prox
                else:

                    nodosiguiente.paquete=router.paquete
                    router.paquete=None
                    router=nodosiguiente
            
            elif (nodosiguiente.estado=="reset" or  nodosiguiente.estado=="inactivo" or nodosiguiente.estado=="agregado") and nodosiguiente.posicion==router.paquete.destino:
                
                while nodosiguiente.estado=="reset" or  nodosiguiente.estado=="inactivo"or nodosiguiente.estado=="agregado":
                    pass
                ## envio
                
                if router.estado=="activo":
                    
                    router.guardar_datospaquete()
                    nodosiguiente.paquete=router.paquete
                    router.paquete=None
                    router.enviados+=1
                    threading_cambiarestado = threading.Thread(target=router.cambiarestado, args=("inactivo",))
                    threading_cambiarestado.start()
                    router=nodosiguiente
                else:
                    
                    nodosiguiente.paquete=router.paquete
                    router.paquete=None
                    router=nodosiguiente


            elif nodosiguiente.estado=="inactivo" or nodosiguiente.estado=="reset"or nodosiguiente.estado=="agregado":
                
                while nodosiguiente.prox.estado=="inactivo" or nodosiguiente.prox.estado=="reset" or nodosiguiente.prox.estado=="agregado" or nodosiguiente.posicion!=router.paquete.destino:
                    nodosiguiente=nodosiguiente.prox
                while( nodosiguiente.estado=="reset" or  nodosiguiente.estado=="inactivo"or nodosiguiente.estado=="agregado")and nodosiguiente.posicion!=router.paquete.destino:
                    pass
                
                if router.estado=="activo" and nodosiguiente.posicion != router.posicion:
                    
                    router.guardar_datospaquete()
                    nodosiguiente.paquete=router.paquete
                    router.paquete=None
                    router.enviados+=1
                    
                    threading_cambiarestado = threading.Thread(target=router.cambiarestado, args=("inactivo",))
                    threading_cambiarestado.start()
                    router=nodosiguiente
                elif nodosiguiente.posicion != router.posicion:
                    
                    nodosiguiente.paquete=router.paquete
                    router.paquete=None
                    router=nodosiguiente
                
                
                
            # si el nodo siguiente esta apagado o inactivo, y es el nodo de destino
            

        
        router.recibidos+=1
        router.guardar_datospaquete()

    def buscar_router(self,pos):
        nodo=self.head
        while nodo.posicion!=pos:
            nodo=nodo.prox
        return nodo



