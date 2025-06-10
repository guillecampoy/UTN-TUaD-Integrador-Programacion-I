from anytree import Node, RenderTree
import pydot

def crear_nodo(valor):
    """
    Crea un nodo de árbol binario con valor y sin hijos.
    """
    return [valor, None, None]  # valor, hijo izquierdo, hijo derecho

def insertar_hijo(arbol, nuevo_valor):
    detener_ciclo = False
    while not detener_ciclo:
        print(f"Nodo actual: {arbol[0]}")
        lado = input(f"¿Insertar {nuevo_valor} a la izquierda o derecha de {arbol[0]}? (i/d): ").lower()
        if lado == 'i':
            if arbol[1] is None:
                arbol[1] = crear_nodo(nuevo_valor)
                detener_ciclo = True
                return
            else:
                arbol = arbol[1]
        elif lado == 'd':
            if arbol[2] is None:
                arbol[2] = crear_nodo(nuevo_valor)
                detener_ciclo = True
                return
            else:
                arbol = arbol[2]
        else:
            print("Opción inválida. Usa 'i' para izquierda o 'd' para derecha.")

def buscar_preorden(arbol, valor):
    if arbol is None:
        return False
    if arbol[0] == valor:
        return True
    if buscar_preorden(arbol[1], valor):
        return True
    return buscar_preorden(arbol[2], valor)

def buscar_inorden(arbol, valor):
    if arbol is None:
        return False
    if buscar_inorden(arbol[1], valor):
        return True
    if arbol[0] == valor:
        return True
    return buscar_inorden(arbol[2], valor)

def buscar_postorden(arbol, valor):
    if arbol is None:
        return False
    if buscar_postorden(arbol[1], valor):
        return True
    if buscar_postorden(arbol[2], valor):
        return True
    return arbol[0] == valor

def mostrar_arbol(arbol, nivel=0):
    if arbol is not None:
        mostrar_arbol(arbol[2], nivel + 1)
        print("   " * nivel + f"-> {arbol[0]}")
        mostrar_arbol(arbol[1], nivel + 1)

def pedir_numero(mensaje):
    detener_ciclo = False
    while not detener_ciclo:
        entrada = input(mensaje)
        if entrada.isdigit():
            detener_ciclo = True
            return int(entrada)
        else:
            print("⚠️ Por favor, ingresa solo números enteros.")

def pedir_tipo_recorrido():
    opciones = {'p': 'preorden', 'i': 'inorden', 'o': 'postorden'}
    detener_ciclo = False
    while not detener_ciclo:
        entrada = input("Selecciona tipo de búsqueda: (p=preorden, i=inorden, o=postorden): ").lower()
        if entrada in opciones:
            detener_ciclo = True
            print(f"✅ Búsqueda seleccionada: {opciones[entrada]}")
            return opciones[entrada]
        else:
            print("❌ Opción inválida. Usa solo 'p', 'i' o 'o'.")

def buscar_por_recorrido(arbol, valor, tipo):
    if tipo == "preorden":
        encontrado = buscar_preorden(arbol, valor)
    elif tipo == "inorden":
        encontrado = buscar_inorden(arbol, valor)
    elif tipo == "postorden":
        encontrado = buscar_postorden(arbol, valor)
    
    if encontrado:
        print(f"✅ Valor {valor} encontrado con búsqueda en {tipo}.")
    else:
        print(f"❌ Valor {valor} NO encontrado con búsqueda en {tipo}.")

# --- Visualización ---

def convertir_a_anytree(arbol, padre=None):
    """Convierte el árbol binario en listas a formato anytree para impresión en consola"""
    if arbol is None:
        return None
    nodo = Node(arbol[0], parent=padre)
    if arbol[1] is not None:
        convertir_a_anytree(arbol[1], nodo)
    if arbol[2] is not None:
        convertir_a_anytree(arbol[2], nodo)
    return nodo

def imprimir_ascii(arbol):
    """Imprime el árbol usando caracteres ASCII con anytree"""
    print("Representación visual del árbol (ASCII):")
    anytree_raiz = convertir_a_anytree(arbol)
    for pre, _, node in RenderTree(anytree_raiz):
        print(f"{pre}{node.name}")

def convertir_a_dot(arbol, parent_name=None, graph=None):
    """Convierte el árbol binario a formato pydot para exportar a PNG o SVG"""
    if arbol is None:
        return graph
    if graph is None:
        graph = pydot.Dot(graph_type='graph')

    node_name = str(arbol[0])
    graph.add_node(pydot.Node(node_name))

    if parent_name:
        graph.add_edge(pydot.Edge(parent_name, node_name))

    # Recorrer hijos izquierdo y derecho
    if arbol[1] is not None:
        convertir_a_dot(arbol[1], node_name, graph)
    if arbol[2] is not None:
        convertir_a_dot(arbol[2], node_name, graph)

    return graph

def guardar_grafico(arbol, filename="arbol.png"):
    """Guarda el árbol como imagen (formato depende del filename)"""
    graph = convertir_a_dot(arbol)
    if filename.endswith(".svg"):
        graph.write_svg(filename)
    else:
        graph.write_png(filename)

# Programa principal
if __name__ == "__main__":
    valor_raiz = pedir_numero("Ingresa el valor numérico del nodo raíz: ")
    arbol = crear_nodo(valor_raiz)
    detener_ciclo = False

    while not detener_ciclo:
        respuesta = input("¿Deseas insertar un nuevo nodo? (s/n): ").lower()
        if respuesta == 's':
            nuevo = pedir_numero("Ingresa el valor numérico del nuevo nodo: ")
            insertar_hijo(arbol, nuevo)
            
        elif respuesta == 'n':
            print("\nÁrbol binario final:")
            mostrar_arbol(arbol)
            print("\nRepresentación visual del árbol:")
            imprimir_ascii(arbol)
            guardar_grafico(arbol, "arbol.png")
            print("✅ Árbol guardado como 'arbol.png'.")
            tipo = pedir_tipo_recorrido()
            valor_buscar = pedir_numero("Ingresa el valor numérico a buscar: ")
            buscar_por_recorrido(arbol, valor_buscar, tipo)
            detener_ciclo = True
        else:
            print("Opción inválida.")