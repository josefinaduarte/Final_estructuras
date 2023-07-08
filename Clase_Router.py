class Router():
    def __init__(self,posicion,estado="agregado",paquete=None,prox = None):
        self.posicion=posicion
        self.estado=estado
        self.paquete=paquete
        self.prox=prox

    def __str__(self):
        pass

    def reset(self):
        pass

    def analizar_destino_paquete(self):         #El router analiza si el msj tiene como destino ese mismo router (si no lo es se va a transmitir)
        pass

    def transmitir_paquete(self):          #Es un metodo del router o de la lista? deberiamos incluir entre transmision y transmision el tiempo de latencia
        pass

    def guardar_datospaquete(self):     #guardar los msjs de los paquetes que pasaron por el router
        pass

    def cambiar_guardar_datoscambioestado(self):             ##es el mismo para activar, inactivar (agregar se hace cin lista enlazada)
        pass

    def cantidad_paquetes_envorec(self):        #para tener el dato de la cantidad de paquetes que recibio y envio para el grafico
        pass