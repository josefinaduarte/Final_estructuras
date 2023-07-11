class Paquete():
    def __init__(self,id,mensaje,origen,destino,fecha_crea):
        self.id=id
        self.mensaje=mensaje
        self.origen=origen
        self.destino=destino
        self.fecha_crea=fecha_crea

    def __str__(self):
        return 'El mensaje del paquete es {} , su origen es {}, y su destino es {}'.format(self.mensaje,self.origen,self.destino,self.fecha_crea)



