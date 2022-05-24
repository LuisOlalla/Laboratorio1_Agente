#Nombre: Luis Olalla
#Tema: Agente Robot de tiro con arco y flecha
#Curso: 6to A
#Asignatura: Inteligencia Artificial

#Creamos la función del robot de tiro con arco
def RobotArco():
    #Colocamos el objetivo o meta de nuestro agente
    estados_objetivos = {'T':'1','M':'1','N':'1'}
    esfuerzo = 0 #Esto es el esfuerzo que realiza el robot al cambiar de estado se podria decir que es el costo.
    #Definimos los estados de nuestro agente.
    print("Estados del robot de tiro con arco")
    print("Tiro con arco acertado = 1")
    print("Tiro con arco fallido = 0 ")
    #Las locaciones de nuestro robot son:
    print("Locaciones del agente robot con arco ")
    print("Tiro con arco en la tarde = T")
    print("Tiro con arco en la mañana = M")
    print("Tiro con arco en la noche = N")
    