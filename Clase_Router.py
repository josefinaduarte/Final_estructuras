class Router():
    def __init__(self,posicion,estado,paquete):
        self.posicion=posicion
        self.estado=estado
        self.paquete=paquete

    def __str__(self):
        pass

    def cambiar_estado(self):           ##es el mismo para activar, agregar, inactivar y reset?
        pass

    def transmitir_paquete(self):          #Es un metodo del router o de la lista?
        pass

    def analizar_destino_paquete(self):
        pass

    def guardar_datospaquete(self):     #guardar los msjs de los paquetes que pasaron por el router
        pass

    def guardar_datoscambioestado(self):
        pass

    def cantidad_paquetes_envorec(self):        #para tener el dato de la cantidad de paquetes que recibio y envio para el grafico
        pass