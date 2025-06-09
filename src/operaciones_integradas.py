#def crear_nodo(valor):
#    return [valor, None, None]

#def insertar_nodo(arbol, nuevo_valor):
#    detener_ciclo = False 
#    while not detener_ciclo:
#        print(f"Nodo actual: {arbol[0]}")
#        lado = input(f"¿Insertar {nuevo_valor} a la izquierda o derecha de {arbol[0]}? (i/d): ").lower()
#        if lado == 'i':
#            if arbol[1] is None:
#                arbol[1] = crear_nodo(nuevo_valor)
#                detener_ciclo = True
#                return
#            else:
#                arbol = arbol[1]
#        elif lado == 'd':
#            if arbol[2] is None:
#                arbol[2] = crear_nodo(nuevo_valor)
#                detener_ciclo = True
#                return
#            else:
#                arbol = arbol[2]
#        else:
#            print("Opción inválida. Usa 'i' para izquierda o 'd' para derecha.")

#def pedir_numero(mensaje):
#    detener_ciclo = False 
#    while not detener_ciclo:
#        entrada = input(mensaje)
#        if entrada.isdigit():
#            detener_ciclo = True
#            return int(entrada)
#        else:
#            print("⚠️ Por favor, ingresa solo números enteros.")
#
##def imprimir_arbol(arbol, nivel=0):
#    if arbol is not None:
#        imprimir_arbol(arbol[2], nivel + 1)
#        print('   ' * nivel + f"-> {arbol[0]}")
#        imprimir_arbol(arbol[1], nivel + 1)
#
## Funciones de búsqueda por tipo de recorrido
##def buscar_preorden(arbol, valor):
#    if arbol is None:
#        return False
#    if arbol[0] == valor:
#        return True
#    if buscar_preorden(arbol[1], valor):
#        return True
#    return buscar_preorden(arbol[2], valor)
#
##def buscar_inorden(arbol, valor):
#    if arbol is None:
#        return False
#    if buscar_inorden(arbol[1], valor):
#        return True
#    if arbol[0] == valor:
#        return True
#    return buscar_inorden(arbol[2], valor)
#
##def buscar_postorden(arbol, valor):
#    if arbol is None:
#        return False
#    if buscar_postorden(arbol[1], valor):
#        return True
#    if buscar_postorden(arbol[2], valor):
#        return True
#    return arbol[0] == valor
#
##def pedir_tipo_recorrido():
#    opciones = {'p': 'preorden', 'i': 'inorden', 'o': 'postorden'}
#    while True:
#        entrada = input("Selecciona tipo de búsqueda: (p=preorden, i=inorden, o=postorden): ").lower()
#        if entrada in opciones:
#            return opciones[entrada]
#        else:
#            print("❌ Opción inválida. Usa solo 'p', 'i' o 'o'.")
#
##def buscar_por_recorrido(arbol, valor, tipo):
#    if tipo == "preorden":
#        encontrado = buscar_preorden(arbol, valor)
#        
#    elif tipo == "inorden":
#        encontrado = buscar_inorden(arbol, valor)
#    
#    elif tipo == "postorden":
#        encontrado = buscar_postorden(arbol, valor)
#          
#    if encontrado:
#        print(f"✅ Valor {valor} encontrado con búsqueda en {tipo}.")
#    else:
#        print(f"❌ Valor {valor} NO encontrado con búsqueda en {tipo}.")
#
# Programa principal
#if __name__ == "__main__":
#    valor_raiz = pedir_numero("Ingresa el valor numérico del nodo raíz: ")
#    arbol = crear_nodo(valor_raiz)
#
#    while True:
#        respuesta = input("¿Deseas insertar un nuevo nodo? (s/n): ").lower()
#        if respuesta == 's':
#            nuevo = pedir_numero("Ingresa el valor numérico del nuevo nodo: ")
#            insertar_nodo(arbol, nuevo)
#        elif respuesta == 'n':
#            print("\nÁrbol binario final:")
#            imprimir_arbol(arbol)
#
#            tipo = pedir_tipo_recorrido()
#            valor_buscar = pedir_numero("Ingresa el valor numérico a buscar: ")
#            buscar_por_recorrido(arbol, valor_buscar, tipo)
#            break
#        else:
#            print("Opción inválida.")
#