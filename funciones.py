import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta función devuelve la lista de palabras que empiezan por una letra que alfabéticamente está antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """
    resultado=[]#la lista se tiene que crear fuera del bucle
    for clave in diccionario:
        #for palabra in diccionario[clave]: #este bucle no tenia sentido, ya que palabra era un simple numero que empezaba por 0 para contar cada vuelta del bucle
        palabra = diccionario[clave]#lo que se tiene que hacer es que la palabra sea igual a la palabra de la posicion del diccionario que queremos comprobar
        if palabra[0] < letra:
            resultado.append(palabra)
    return resultado

def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta función inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    clients_list[nif] = {#yo diria que esta función es correcta
        nif: {'name': name,
              'address': address,
              'phone': phone,
              'email': email
        }
    }

def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un número de repeticiones, esta función selecciona 5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """    
    combinaciones={}
    for i in range(1,repeticiones+1):
        cartas_aleatorias = cartas_iniciales 
        combinaciones["repeticion"+str(i)]={}# para un diccionario se pone este simbolo y no este []
        for j in range(0,5):
            carta=random.choice(cartas_aleatorias)
            combinaciones["repeticion"+str(i)] = carta#en un diccionario se añaden de esta forma los nuevos valores
            cartas_aleatorias.remove(carta)

    return combinaciones

    
