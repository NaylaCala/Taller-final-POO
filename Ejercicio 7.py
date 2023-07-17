import time

class Vehiculo:
    def __init__(self, id, velocidad, posicion):
        self.id = id
        self.velocidad = velocidad
        self.posicion = posicion
    
    def mover(self):
        self.posicion += self.velocidad
    
    def __str__(self):
        return f"Vehículo {self.id} - Posición: {self.posicion}"
        

class Semáforo:
    def __init__(self, estado):
        self.estado = estado
    
    def cambiar_estado(self):
        if self.estado == "rojo":
            self.estado = "verde"
        else:
            self.estado = "rojo"
    
    def __str__(self):
        return f"Semáforo - Estado: {self.estado}"
        

class Cruce:
    def __init__(self, semaforos):
        self.semaforos = semaforos
    
    def __str__(self):
        return f"Cruce - Semáforos: {', '.join(str(s) for s in self.semaforos)}"

    
def simulador_trafico():
    
    vehiculo1 = Vehiculo(1, 5, 0)
    vehiculo2 = Vehiculo(2, 3, 10)
    
    
    semaforo1 = Semáforo("rojo")
    semaforo2 = Semáforo("verde")
    
    
    cruce = Cruce([semaforo1, semaforo2])
    
    
    for _ in range(10):
        print(vehiculo1)
        print(vehiculo2)
        print(cruce)
        print()
        
        vehiculo1.mover()
        vehiculo2.mover()
        
       
        if semaforo1.estado == "rojo":
            vehiculo1.velocidad = 0
        else:
            vehiculo1.velocidad = 5
        
        if semaforo2.estado == "rojo":
            vehiculo2.velocidad = 0
        else:
            vehiculo2.velocidad = 3
        
        
        if _ % 5 == 0:
            semaforo1.cambiar_estado()
            semaforo2.cambiar_estado()
        
        time.sleep(1)

simulador_trafico()
