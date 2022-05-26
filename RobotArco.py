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
                    print("El robot en el escenario en la noche acerto el tiro con arco") #El robot acierta el tiro
            else:
                print("Todas las flechas han sido lanzadas")  #No hay mas flechas que lanzar , por lo tanto ahi termina el proceso
                print("El costo o esfuerzo es : "+str(esfuerzo)) #Mostramos el valor total del esfuerzo
        
        if estado_tiroT == '1': # En caso de que sea  1 el robot acierta el tiro con arco
            print("El robot ha acertado el tiro en el escenario en la tarde ")
            #Aqui como es 0 falla el tiro con arco en la mañana
            if estado_tiroM =='0': 
                #Decimos que el robot ha fallado 
                print("El robot en el escenario en la mañana ha fallado")
                #Lanzamos la felcha otra vez
                print("Lanzando flecha")
                esfuerzo+=1 #aumenta el esfuerzo al cambiar de estado
                print("Valor del esfuerzo o costo actual =" +str(esfuerzo))
                #Cuando haya aceertado se cambia el estado pasando a un estado acertado
                estados_objetivos['M']='1' #El tiro es acertado
                esfuerzo+=1 #Aumentamos el esfuerzo porque hizo un cambio
                print("El robot en el escenario de la mañana ha acertado el tiro") #El robot en el escenario de la mañana acierta el tiro
                print("Valor del esfuerzo o costo actual =" +str(esfuerzo)) #Actualizamos el costo o esfuerzo
                if estado_tiroN =='0': #Pasamos al escenario de tiro en la noche
                   print("El robot en el escenario de tiro en la noche ha fallado") #El robot falla el tiro en la noche
                   print("Lanzando flecha") #Lanzanmos la flecha ya que el robot ha fallado
                   esfuerzo+=1 #aumentamos el costo o esfuerzo
                   print("Valor del esfuerzo o costo actual =" +str(esfuerzo)) #Actualizamos el costo o esfuerzo
                   estados_objetivos['N']='1' #En caso de que sea 1 el tiro en la noche sera acertado
                   esfuerzo+=1 #El costo va aumentar por el cambio realziado
                   print("El robot en el escenario de la Noche ha acertado el tiro") #Decimos que el robot ha acertado el tiro
                   print("Valor del esfuerzo o costo actual =" +str(esfuerzo)) #Actualizamos el costo o esfuerzo
            #Si el robot en el escenario de la mañana y noche acerto los tiros, el proceso temrina.
            else: 
                print("El proceso de tiro ha terminado"+str(esfuerzo))
                print("Valor del esfuerzo o costo actual =" +str(esfuerzo)) #Actualizamos el costo o esfuerzo
                #Decimos que el escenario de la mañana y noche, el robot acerto los tiros
                print("El robot en los escenarios de mañana y noche acerto los tiros")
        
        
        
        #Realizamos la programacion para el escenario de la mañana M
    elif escenario_tiro == 'M': # mediante elif controlamos el flujo del agente y los bloques de datos especificos
        print("El robot de tiro con arco esta en el escenario de tiro en Mañana")
        estado_tiroM = input("Escriba el estado del escenario o locacion :" +escenario_tiro) #Aqui se ingresa el estado del robot de tiro con arco
        # Ingreso del estado de escenario tiro T
        estado_tiroT= input("Escriba el estado del escenario o locacion  T")
        #Ingreso del estado para el escenario de tiro N
        estado_tiroN = input("Escriba el estado del escenario o locacion N ")
        print("Valor del esfuerzo o costo actual =" +str(esfuerzo)) #Actualizamos el costo o esfuerzo
        #En caso de que sea 0 el tiro es fallido
        if estado_tiroM =='0': 
            print("En el escenario: "+escenario_tiro + ", el robot ha fallado el tiro con arco")
            #Ahora vamos a cambiar el estado porque si va a atinar los tiros
            estados_objetivos['M'] ='1'
            #Avisamos que el robot acerto el tiro con arco
            print("Lanzando flecha")
            #verificamos el estado del tiro con arco
            print("En el escenario: "+escenario_tiro+ ", el robot ha acertado el tiro con arco")
            esfuerzo +=1 #aumentamos el esfuerzo o costo ya que cambio el valor
            #mostramos el valor del esfuerzo.
            print("Valor del esfuerzo o costo =" +str(esfuerzo))
            if estado_tiroT =='0': # El estado de la locacion T es igual a 0 es un tiro fallido
                #En caso de que sea 0 el tiro es fallido
                print("En el escenario: "+estado_tiroT + ", el robot ha fallado el tiro con arco")
                #El robot va a lanzar la flecha
                print("Lanzando felcha")
                esfuerzo+=1 #aumenta el esfuerzo o costo ya que cambio el valor
                #vamos a mostrar el valor del esfuerzo
                print("Valor del esfuerzo o costo actual =" +str(esfuerzo))
                #afirmamos que el robot en el escenario en la Tarde acerto el tiro con arco
                print("El robot en el escenario en la tarde acerto el tiro con arco")
                
                #Ahora vamos a realizar lo mismo para la locacion de tiro en la Noche
                if estado_tiroN =='0':
                    print("En el escenario: "+estado_tiroN + ", el robot ha fallado el tiro con arco")
                    #El robot va a lanzar la flecha
                    print("Lanzando felcha")
                    esfuerzo+=1 #aumenta el esfuerzo o costo ya que cambio el valor
                     #vamos a mostrar el valor del esfuerzo
                    print("Valor del esfuerzo o costo actual =" +str(esfuerzo))
                    print("El robot en el escenario en la noche acerto el tiro con arco") #El robot acierta el tiro
            else:
                print("El robot en el escenario de tiro en la tarde ha acertado los tiros")  
                print("El robot en el escenario de tiro en la noche ha acertado los tiros ") 
        
        if estado_tiroM == '1': # En caso de que sea  1 el robot acierta el tiro con arco
            print("El robot ha acertado el tiro en el escenario en la mañana")
            #Aqui como es 0 falla el tiro con arco en la mañana
            if estado_tiroT =='0': 
                #Decimos que el robot ha fallado 
                print("El robot en el escenario en la tarde ha fallado")
                #Lanzamos la felcha otra vez
                print("Lanzando flecha")
                esfuerzo+=1 #aumenta el esfuerzo al cambiar de estado
                print("Valor del esfuerzo o costo actual =" +str(esfuerzo))
                #Cuando haya aceertado se cambia el estado pasando a un estado acertado
                estados_objetivos['T']='1' #El tiro es acertado
                esfuerzo+=1 #Aumentamos el esfuerzo porque hizo un cambio
                print("El robot en el escenario de la tarde ha acertado el tiro") #El robot en el escenario de la tarde acierta el tiro
                print("Valor del esfuerzo o costo actual =" +str(esfuerzo)) #Actualizamos el costo o esfuerzo
                if estado_tiroN =='0': #El robot falla el tiro con arco
                   print("El robot del escenario de tiro en la noche ha fallado") #Lanzanmos la flecha ya que el robot ha fallado
                   esfuerzo+=1 #aumentamos el costo o esfuerzo
                   print("Valor del esfuerzo o costo actual =" +str(esfuerzo)) #Actualizamos el costo o esfuerzo
                   estados_objetivos['N']='1' #En caso de que sea 1 el tiro en la noche sera acertado
                   esfuerzo+=1 #El costo va aumentar por el cambio realziado
                   print("El robot en el escenario de la Noche ha acertado el tiro") #Decimos que el robot ha acertado el tiro
                   print("Valor del esfuerzo o costo actual =" +str(esfuerzo)) #Actualizamos el costo o esfuerzo
            #Si el robot en el escenario de la mañana y noche acerto los tiros, el proceso temrina.
            else: 
                print("El robot en el escenario de tiro en la tarde ha acertado todos los tiros  ") #Decimos que el robot acerto en el escenario de tiro en la tarde
                print("El robot en el escenario de tiro en la noche ha acertado todos los tiros  ")#Decimos que el robot acerto en el escenario de tiro en la noche
        
        
    elif escenario_tiro =='N':
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
                    print("El robot en el escenario en la noche acerto el tiro con arco") #El robot acierta el tiro
            else:
                print("Todas las flechas han sido lanzadas")  #No hay mas flechas que lanzar , por lo tanto ahi termina el proceso
                print("El costo o esfuerzo es : "+str(esfuerzo)) #Mostramos el valor total del esfuerzo
        
        if estado_tiroT == '1': # En caso de que sea  1 el robot acierta el tiro con arco
            print("El robot ha acertado el tiro en el escenario en la tarde ")
            #Aqui como es 0 falla el tiro con arco en la mañana
            if estado_tiroM =='0': 
                #Decimos que el robot ha fallado 
                print("El robot en el escenario en la mañana ha fallado")
                #Lanzamos la felcha otra vez
                print("Lanzando flecha")
                esfuerzo+=1 #aumenta el esfuerzo al cambiar de estado
                print("Valor del esfuerzo o costo actual =" +str(esfuerzo))
                #Cuando haya aceertado se cambia el estado pasando a un estado acertado
                estados_objetivos['M']='1' #El tiro es acertado
                esfuerzo+=1 #Aumentamos el esfuerzo porque hizo un cambio
                print("El robot en el escenario de la mañana ha acertado el tiro") #El robot en el escenario de la mañana acierta el tiro
                print("Valor del esfuerzo o costo actual =" +str(esfuerzo)) #Actualizamos el costo o esfuerzo
                if estado_tiroN =='0': #Pasamos al escenario de tiro en la noche
                   print("El robot en el escenario de tiro en la noche ha fallado") #El robot falla el tiro en la noche
                   print("Lanzando flecha") #Lanzanmos la flecha ya que el robot ha fallado
                   esfuerzo+=1 #aumentamos el costo o esfuerzo
                   print("Valor del esfuerzo o costo actual =" +str(esfuerzo)) #Actualizamos el costo o esfuerzo
                   estados_objetivos['N']='1' #En caso de que sea 1 el tiro en la noche sera acertado
                   esfuerzo+=1 #El costo va aumentar por el cambio realziado
                   print("El robot en el escenario de la Noche ha acertado el tiro") #Decimos que el robot ha acertado el tiro
                   print("Valor del esfuerzo o costo actual =" +str(esfuerzo)) #Actualizamos el costo o esfuerzo
            #Si el robot en el escenario de la mañana y noche acerto los tiros, el proceso temrina.
            else: 
                print("El proceso de tiro ha terminado"+str(esfuerzo))
                print("Valor del esfuerzo o costo actual =" +str(esfuerzo)) #Actualizamos el costo o esfuerzo
                #Decimos que el escenario de la mañana y noche, el robot acerto los tiros
                print("El robot en los escenarios de mañana y noche acerto los tiros")
        
        
        #Realizamos la programacion para el escenario de la Noche N
    elif escenario_tiro == 'N':  # mediante elif controlamos el flujo del agente y los bloques de datos especificos
        print("El robot de tiro con arco esta en el escenario de tiro en Noche")
        # Aqui se ingresa el estado del robot de tiro con arco
        estado_tiroN = input(
            "Escriba el estado del escenario o locacion :" + escenario_tiro)
        # Ingreso del estado de escenario tiro T
        estado_tiroT = input("Escriba el estado del escenario o locacion  T")
        #Ingreso del estado para el escenario de tiro M
        estado_tiroM = input("Escriba el estado del escenario o locacion N ")
        # Actualizamos el costo o esfuerzo
        print("Valor del esfuerzo o costo actual =" + str(esfuerzo))
        #En caso de que sea 0 el tiro es fallido
        if estado_tiroN == '0':
            print("En el escenario: "+escenario_tiro +
                  ", el robot ha fallado el tiro con arco")
            #Ahora vamos a cambiar el estado porque si va a atinar los tiros
            estados_objetivos['N'] = '1'
            #Avisamos que el robot acerto el tiro con arco
            print("Lanzando flecha")
            #verificamos el estado del tiro con arco
            print("En el escenario: "+escenario_tiro +
                  ", el robot ha acertado el tiro con arco")
            esfuerzo += 1  # aumentamos el esfuerzo o costo ya que cambio el valor
            #mostramos el valor del esfuerzo.
            print("Valor del esfuerzo o costo =" + str(esfuerzo))
            if estado_tiroT == '0':  # El estado de la locacion T es igual a 0 es un tiro fallido
                #En caso de que sea 0 el tiro es fallido
                print("En el escenario: "+estado_tiroT +
                      ", el robot ha fallado el tiro con arco")
                #El robot va a lanzar la flecha
                print("Lanzando felcha")
                esfuerzo += 1  # aumenta el esfuerzo o costo ya que cambio el valor
                #vamos a mostrar el valor del esfuerzo
                print("Valor del esfuerzo o costo actual =" + str(esfuerzo))
                #afirmamos que el robot en el escenario en la Tarde acerto el tiro con arco
                print("El robot en el escenario en la tarde acerto el tiro con arco")

                #Ahora vamos a realizar lo mismo para la locacion de tiro en la Mañana
                if estado_tiroM == '0':
                    print("En el escenario: "+estado_tiroM +
                          ", el robot ha fallado el tiro con arco")
                    #El robot va a lanzar la flecha
                    print("Lanzando felcha")
                    esfuerzo += 1  # aumenta el esfuerzo o costo ya que cambio el valor
                    #vamos a mostrar el valor del esfuerzo
                    print("Valor del esfuerzo o costo actual =" + str(esfuerzo))
                    # El robot acierta el tiro
                    print(
                        "El robot en el escenario en la mañana acerto el tiro con arco")
            else:
                print(
                    "El robot en el escenario de tiro en la tarde ha acertado los tiros")
                print(
                    "El robot en el escenario de tiro en la mañana ha acertado los tiros ")

        if estado_tiroN == '1':  # En caso de que sea  1 el robot acierta el tiro con arco
            print("El robot ha acertado el tiro en el escenario en la noche")
            #Aqui como es 0 falla el tiro con arco en la mañana
            if estado_tiroT == '0':
                #Decimos que el robot ha fallado
                print("El robot en el escenario en la tarde ha fallado")
                #Lanzamos la felcha otra vez
                print("Lanzando flecha")
                esfuerzo += 1  # aumenta el esfuerzo al cambiar de estado
                print("Valor del esfuerzo o costo actual =" + str(esfuerzo))
                #Cuando haya aceertado se cambia el estado pasando a un estado acertado
                estados_objetivos['T'] = '1'  # El tiro es acertado
                esfuerzo += 1  # Aumentamos el esfuerzo porque hizo un cambio
                # El robot en el escenario de la tarde acierta el tiro
                print("El robot en el escenario de la tarde ha acertado el tiro")
                # Actualizamos el costo o esfuerzo
                print("Valor del esfuerzo o costo actual =" + str(esfuerzo))
                if estado_tiroM == '0':  # El robot falla el tiro con arco
                   # Lanzanmos la flecha ya que el robot ha fallado
                   print("El robot del escenario de tiro en la mañana ha fallado")
                   esfuerzo += 1  # aumentamos el costo o esfuerzo
                   # Actualizamos el costo o esfuerzo
                   print("Valor del esfuerzo o costo actual =" + str(esfuerzo))
                   # En caso de que sea 1 el tiro en la noche sera acertado
                   estados_objetivos['M'] = '1'
                   esfuerzo += 1  # El costo va aumentar por el cambio realziado
                   # Decimos que el robot ha acertado el tiro
                   print("El robot en el escenario de la mañana ha acertado el tiro")
                   # Actualizamos el costo o esfuerzo
                   print("Valor del esfuerzo o costo actual =" + str(esfuerzo))
            #Si el robot en el escenario de la mañana y noche acerto los tiros, el proceso temrina.
            else:
                # Decimos que el robot acerto en el escenario de tiro en la tarde
                print(
                    "El robot en el escenario de tiro en la tarde ha acertado todos los tiros  ")
                # Decimos que el robot acerto en el escenario de tiro en la mañana
                print(
                    "El robot en el escenario de tiro en la mañana ha acertado todos los tiros  ")
    #PArte final
    print("Estado objetivo:")
    print(estados_objetivos)#imprimimos el estado objetivo
    print("Costo total  ") 
    print(esfuerzo)#Mostramos el valor total del costo


RobotArco()  # Etiqueta final
