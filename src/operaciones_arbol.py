# Funciones para operaciones básicas en un árbol implementado con listas anidadas
# Primer versión cruda de operaciones básicas
# Resta implementar otros tipos de búsquedas que se listan en pseudo código
# Resta mejorar otras funciones como validaciones, balanceo de árbol, etc.

def crear_arbol():
    """
    Crea un árbol vacío representado como una lista anidada.
    La lista contiene el valor del nodo raíz y una lista de sus hijos.
    """
    return [None, []]  # El primer elemento es el valor del nodo, el segundo es la lista de hijos

def crear_nodo(valor):
    """
    Crea un nodo hoja con un valor y sin hijos.
    """
    return [valor, []]

def insertar_hijo(arbol, padre, hijo):
    """
    Inserta un hijo en el árbol bajo el nodo especificado por 'padre'.
    Si el padre no existe, no se realiza ninguna acción.
    """
    # Árbol vacío, no se puede insertar
    if arbol[0] is None:
        return  
    if arbol[0] == padre:
        arbol[1].append(crear_nodo(hijo)) # Si el nodo actual es el padre, insertamos el hijo
    else: 
        for hijo_nodo in arbol[1]:   # Recorremos los hijos para buscar al padre  
            insertar_hijo(hijo_nodo, padre, hijo)

def buscar_profundidad(arbol, valor):
    """
    Búsqueda en profundidad (DFS - Depth First Search).
    Busca un valor en el árbol recorriéndolo en profundidad.
    Devuelve True si se encuentra, False en caso contrario.
    """
    if arbol[0] is None:
        return False 
    if arbol[0] == valor:
        return True  
    for hijo_nodo in arbol[1]:
        if buscar_profundidad(hijo_nodo, valor):
            return True
    return False

# Otras formas de búsqueda en árboles (pseudocódigo):

# def buscar_anchura(arbol, valor):
#     """
#     Búsqueda en anchura (BFS - Breadth First Search).
#     Utiliza una cola para recorrer el árbol nivel por nivel.
#     1. Crear una cola e insertar el nodo raíz.
#     2. Mientras la cola no esté vacía:
#         a. Sacar el primer nodo de la cola.
#         b. Si el valor del nodo es igual al buscado, retornar True.
#         c. Insertar todos los hijos del nodo en la cola.
#     3. Si termina el recorrido y no se encontró el valor, retornar False.
#     """

# def buscar_preorden(arbol, valor):
#     """
#     Búsqueda en preorden.
#     1. Visitar el nodo actual y comparar su valor.
#     2. Recorrer recursivamente cada hijo en orden.
#     3. Retornar True si se encuentra el valor, False si no.
#     """

# def buscar_postorden(arbol, valor):
#     """
#     Búsqueda en postorden.
#     1. Recorrer recursivamente todos los hijos.
#     2. Visitar el nodo actual y comparar su valor.
#     3. Retornar True si se encuentra el valor, False si no.
#     """

# def buscar_inorden(arbol, valor):
#     """
#     Búsqueda en inorden (solo para árboles binarios).
#     1. Recorrer el hijo izquierdo.
#     2. Visitar el nodo actual y comparar su valor.
#     3. Recorrer el hijo derecho.
#     4. Retornar True si se encuentra el valor, False si no.
#     """

def mostrar_arbol(arbol, nivel=0):
    """
    Muestra el árbol de forma estructurada, indentando según el nivel de profundidad.
    """
    # Si el árbol está vacío, no hay acción
    if arbol[0] is None:
        return  
    print("  " * nivel + str(arbol[0]))  # Se imprime valor de nodo actual
    for hijo_nodo in arbol[1]:
        mostrar_arbol(hijo_nodo, nivel + 1)  # Uso de recursividad para mostrar los hijos

# Algunos tests para ejecutar de forma aislada el codigo y validar su funcionmiento
if __name__ == "__main__":
    raiz = crear_nodo("A")
    insertar_hijo(raiz, "A", "B")
    insertar_hijo(raiz, "A", "C")
    insertar_hijo(raiz, "B", "D")
    insertar_hijo(raiz, "B", "E")
    insertar_hijo(raiz, "C", "F")

    print("Árbol representado:")
    mostrar_arbol(raiz)

    print("\n¿Está 'E' en el árbol?", buscar_profundidad(raiz, "E"))
    print("¿Está 'Z' en el árbol?", buscar_profundidad(raiz, "Z"))
