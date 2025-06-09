
def crear_nodo(valor):
    return [valor, None, None]

def insertar_nodo(arbol, nuevo_valor):
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

def pedir_numero(mensaje):
    detener_ciclo = False 
    while not detener_ciclo:
        entrada = input(mensaje)
        if entrada.isdigit():
            detener_ciclo = True
            return int(entrada)
        else:
            print("⚠️ Por favor, ingresa solo números enteros.")

def imprimir_arbol(arbol, nivel=0):
    if arbol is not None:
        imprimir_arbol(arbol[2], nivel + 1)
        print('   ' * nivel + f"-> {arbol[0]}")
        imprimir_arbol(arbol[1], nivel + 1)

# Recorridos
def preorden(arbol, recorrido=None):
    if recorrido is None:
        recorrido = []
    if arbol is not None:
        recorrido.append(arbol[0])
        preorden(arbol[1], recorrido)
        preorden(arbol[2], recorrido)
    return recorrido

def inorden(arbol, recorrido=None):
    if recorrido is None:
        recorrido = []
    if arbol is not None:
        inorden(arbol[1], recorrido)
        recorrido.append(arbol[0])
        inorden(arbol[2], recorrido)
    return recorrido

def postorden(arbol, recorrido=None):
    if recorrido is None:
        recorrido = []
    if arbol is not None:
        postorden(arbol[1], recorrido)
        postorden(arbol[2], recorrido)
        recorrido.append(arbol[0])
    return recorrido

def pedir_tipo_recorrido():
    opciones = {'p': 'preorden', 'i': 'inorden', 'o': 'postorden'}
    detener_ciclo = False 
    while not detener_ciclo:
        entrada = input("Selecciona tipo de recorrido: (p=preorden, i=inorden, o=postorden): ").lower()
        if entrada in opciones:
            detener_ciclo = True
            return opciones[entrada]
        else:
            print("❌ Opción inválida. Usa solo 'p', 'i' o 'o'.")

def buscar_por_recorrido(arbol, valor, tipo):
    if tipo == "preorden":
        recorrido = preorden(arbol)
    elif tipo == "inorden":
        recorrido = inorden(arbol)
    elif tipo == "postorden":
        recorrido = postorden(arbol)

    print(f"\nRecorrido {tipo.capitalize()}: {recorrido}")
    if valor in recorrido:
        print(f"✅ Valor {valor} encontrado en el recorrido.")
    else:
        print(f"❌ Valor {valor} NO encontrado en el recorrido.")

# Programa principal
if __name__ == "__main__":
    valor_raiz = pedir_numero("Ingresa el valor numérico del nodo raíz: ")
    arbol = crear_nodo(valor_raiz)
    detener_ciclo = False 

    while not detener_ciclo:
        respuesta = input("¿Deseas insertar un nuevo nodo? (s/n): ").lower()
        if respuesta == 's':
            nuevo = pedir_numero("Ingresa el valor numérico del nuevo nodo: ")
            insertar_nodo(arbol, nuevo)
        elif respuesta == 'n':
            print("\nÁrbol binario final:")
            imprimir_arbol(arbol)

            tipo = pedir_tipo_recorrido()
            valor_buscar = pedir_numero("Ingresa el valor numérico a buscar: ")
            buscar_por_recorrido(arbol, valor_buscar, tipo)
            detener_ciclo = True
            break
        else:
            print("Opción inválida.")
