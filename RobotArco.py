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
    #Las locaciones o escenarios de nuestro robot son:
    print("Locaciones del agente robot con arco ")
    print("Tiro con arco en la tarde = T")
    print("Tiro con arco en la mañana = M")
    print("Tiro con arco en la noche = N")
    
    #Print para ingresar la locacion del robot tiro con arco
    escenario_tiro=input("Ingrese el escenario o locaicon del robot de tiro con arco : ")
    #Empezamos a realizar los if correspondientes, empezamos con la T
    #Si el escenario_tiro es T entonces el robot esta en la locacion de tiro en la tarde.
    if escenario_tiro == 'T':
        print("El robot de tiro con arco esta en el escenario de tiro en la tarde")
        estado_tiroT = input("Escriba el estado del escenario o locacion :" +escenario_tiro) #Aqui se ingresa el estado del robot de tiro con arco
        # Ingreso del estado de escenario tiro M
        estado_tiroM= input("Escriba el estado del escenario o locacion  M")
        #Ingreso del estado para el escenario de tiro N
        estado_tiroN = input("Escriba el estado del escenario o locacion N ")
        #En caso de que sea 0 el tiro es fallido
        if estado_tiroT =='0': 
            print("En el escenario: "+escenario_tiro + ", el robot ha fallado el tiro con arco")
            #Ahora vamos a cambiar el estado porque si va a atinar los tiros
            estados_objetivos['T'] ='1'
            #Avisamos que el robot acerto el tiro con arco
            print("Lanzando flecha")
            #verificamos el estado del tiro con arco
            print("En el escenario: "+escenario_tiro+ ", el robot ha acertado el tiro con arco")
            esfuerzo +=1 #aumentamos el esfuerzo o costo ya que cambio el valor
            #mostramos el valor del esfuerzo.
            print("Valor del esfuerzo o costo =" +str(esfuerzo))
            if estado_tiroM =='0': # El estado de la locacion M es igual a 0 es un tiro fallido
                #En caso de que sea 0 el tiro es fallido
                print("En el escenario: "+estado_tiroM + ", el robot ha fallado el tiro con arco")
                print("Nos pasamos al escenario de tiro en la Mañana ") #Nos pasamos a la locacion de la mañana.
                #El robot va a lanzar la flecha
                print("Lanzando felcha")
                esfuerzo+=1 #aumenta el esfuerzo o costo ya que cambio el valor
                #vamos a mostrar el valor del esfuerzo
                print("Valor del esfuerzo o costo actual =" +str(esfuerzo))
                #afirmamos que el robot en el escenario en la Mañana acerto el tiro con arco
                print("El robot en el escenario en la mañana acerto el tiro con arco")
                
                #Ahora vamos a realizar lo mismo para la locacion de tiro en la Noche
                if estado_tiroN =='0':
                    print("En el escenario: "+estado_tiroN + ", el robot ha fallado el tiro con arco")
                    print("Nos pasamos al escenario de tiro en la Noche ") #Nos pasamos a la locacion de la noche.
                    #El robot va a lanzar la flecha
                    print("Lanzando felcha")
                    esfuerzo+=1 #aumenta el esfuerzo o costo ya que cambio el valor
                     #vamos a mostrar el valor del esfuerzo
                    print("Valor del esfuerzo o costo actual =" +str(esfuerzo))
                    print("El robot en el escenario en la noche acerto el tiro con arco")
            else:
                print("Todas las flechas han sido lanzadas")  
                print("El costo o esfuerzo es : "+str(esfuerzo)) 
            
            
             
            