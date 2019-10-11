import threading

from time import sleep

n_sem = 1
semaforo = threading.Semaphore(n_sem)

animals = ["el perro", "la gata", "el canguro"]

class Hilo(threading.Thread):

    def __init__(self, id):
        threading.Thread.__init__(self)   
        self.id = id

    def run(self):
        semaforo.acquire()
        print ("Entro " + animals[self.id -1] + " al patio")
        sleep(3)
        print("Salio " + animals[self.id -1] + " del patio")
        semaforo.release()


hilos = [Hilo(1), Hilo(2), Hilo(3)]
for h in hilos:
    h.start()
