import threading
import time

# Función que se ejecutará de forma asíncrona

def saluda(nombre,lista):
    # Espera 2 segundos
#AGREGUE PAQUETE
    while True:
        time.sleep(2) #tiempo aleatorio
        lista.append(nombre)





# Declaro un hilo de ejecución
lista = []
threading_emails = threading.Thread(target=saluda, args=("Snake",lista))

# Lo lanzo

threading_emails.start()

# Resto de mi código que se ejecutará de forma paralela


while  True:
    print(len(lista))
    time.sleep(1)