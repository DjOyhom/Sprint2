import threading

from time import sleep

n_sem = 1
semaforo = threading.Semaphore(n_sem)

class Hilo(threading.Thread):

    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        semaforo.acquire()
        print ("Entro el gato al patio")
        sleep(3)
        print("Salio el gato del patio")
        semaforo.release()
    
    def aa(self):
        semaforo.acquire()
        print ("Entro el canguro al patio")
        sleep(1)
        print("Salio el canguro del patio")
        semaforo.release()

    def aaa(self):
        semaforo.acquire()
        print ("Entro el perro al patio")
        sleep(5)
        print("Salio el perro del patio")
        semaforo.release()

    def aaaa(self):
        semaforo.acquire()
        print ("Entro el pajaro al patio")
        sleep(0.51)
        print("Salio el pajaro del patio")
        semaforo.release()
    

hilos = [Hilo(1), Hilo(2), Hilo(3)]
for h in hilos:
    h.start()
    h.aa()
    h.aaa()
    h.aaaa()