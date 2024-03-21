#CANDIA NAVARRO IVAN 6CV2

from arbol import Nodo

def evaluar_distancia(nodo):
    costo = 0
    datos = nodo.get_datos()  
    for i in range(0, len(datos)):
        if datos[i] == (i+1):
            costo += 1
    return costo

def solucionar_puzzle(estado_inicial, meta):
    objetivo_alcanzado = False
    visitados = []
    frontera = []
    nodo_raiz = Nodo(estado_inicial)
    frontera.append(nodo_raiz)
    
    while not objetivo_alcanzado and frontera:
        nodo_actual = frontera.pop()
        print("Nodo actual:", nodo_actual.get_datos())   
        visitados.append(nodo_actual)

        if nodo_actual.get_datos() == meta:
            objetivo_alcanzado = True
            return nodo_actual
        else:
            datos_nodo = nodo_actual.get_datos()
            
            # Generar nodos hijo
            hijo_izq = [datos_nodo[1], datos_nodo[0], datos_nodo[2], datos_nodo[3]]
            nodo_izq = Nodo(hijo_izq)
            nodo_izq.set_coste(evaluar_distancia(nodo_izq))
            
            hijo_medio = [datos_nodo[0], datos_nodo[2], datos_nodo[1], datos_nodo[3]]
            nodo_medio = Nodo(hijo_medio)
            nodo_medio.set_coste(evaluar_distancia(nodo_medio))
            
            hijo_der = [datos_nodo[0], datos_nodo[1], datos_nodo[3], datos_nodo[2]]
            nodo_der = Nodo(hijo_der)
            nodo_der.set_coste(evaluar_distancia(nodo_der))
            
            for hijo in [nodo_izq, nodo_medio, nodo_der]:
                if not hijo.en_lista(visitados) and not hijo.en_lista(frontera):
                    frontera.append(hijo)

            nodo_actual.set_hijos([nodo_izq, nodo_medio, nodo_der])
            
            print("Frontera actual: ", [n.get_datos() for n in frontera])

            frontera.sort(key=lambda x: x.get_coste(), reverse=False)

            print("Frontera ordenada: ", [n.get_datos() for n in frontera])

if __name__ == "__main__":
    inicio = [4, 3, 2, 1]
    objetivo = [1, 2, 3, 4]
    solucion_nodo = solucionar_puzzle(inicio, objetivo)
    camino = []
    while solucion_nodo.get_padre() is not None:
        camino.append(solucion_nodo.get_datos())
        solucion_nodo = solucion_nodo.get_padre()

    camino.append(inicio)
    camino.reverse()
    print("Inicio:", inicio)
    print("Objetivo:", objetivo)
    print("Solución:", camino)