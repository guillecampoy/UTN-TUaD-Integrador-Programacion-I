# 🌳 Proyecto Integrador: Árboles en Python con Listas

Bienvenidos al proyecto integrador de la materia **Programación I** de la UTN.  
Este proyecto fue desarrollado por Luis Cisneros y Guillermo Campoy como parte del proyecto final integrador de la materia, parte de la currícula de la **Tecnicatura Universitaria en Programación**.

El enfoque principal de este trabajo es representar estructuras de **árboles** utilizando **listas anidadas**, evitando el uso de clases u objetos. Esta decisión busca facilitar la comprensión de los conceptos fundamentales, sin la complejidad de la POO.

---

## 📁 Estructura del Repositorio

```
/Documentacion       → Documentos de apoyo, criterios de evaluación y entrega 
/src                 → Código fuente en Python  
README.md            → Este archivo
```

---

## 📚 Documentos y Entregables 

- 📄 [Criterios de Evaluación](./Documentación/Rúbrica_trabajo_integrador-Programación_I.pdf)
- 📄 [Material de apoyo presentación](./Documentación/Arboles_implementados_con_listas_soporte_introducción.pdf)  
- 📄 [Guía Enunciado](./Documentación/Consigna-Trabajo_Integrador-Programación_I.pdf)
- 📄 [Material docente](./Documentación/Material_docente-Implementacion-de-Arboles-en-Python-Utilizando-Listas.pdf)
- 📄 [Entregable de del trabajo](./Documentación/Programación-I_Trabajo-Integrador_Luis-Cisneros_Guillermo-Campoy.pdf)


---

## 🔧 Cómo Ejecutar

1. Cloná el repositorio:  
   ```bash
   git clone https://github.com/guillecampoy/UTN-TUaD-Integrador-Programacion-I
   ```

2. Ejecutá el archivo principal:  
   ```bash
   python src/arbol.py
   ```

> ⚠️ Este proyecto no requiere librerías externas para su lógica principal, pero sí se necesitan algunas para las visualizaciones opcionales.

---

## 🖥️ Visualización del Árbol

### Vista en consola (ASCII)

Usamos la librería `anytree` para imprimir el árbol de forma jerárquica con símbolos ASCII:

```bash
pip install anytree
```

```python
A
├── B
│   ├── D
│   └── E
└── C
    └── F
```

### Exportar a PNG o SVG

Para exportar el árbol como imagen, usamos `graphviz` y `pydot`.

```bash
pip install graphviz pydot
sudo apt install graphviz  # en Linux
```
#### Además, instalá Graphviz según tu sistema:

- **Windows**:
  1. Descargá el instalador desde [https://graphviz.org/download](https://graphviz.org/download)
  2. Instalá y agregá la ruta de `dot.exe` al PATH (usualmente `C:\Program Files\Graphviz\bin`)

- **macOS**:
  ```bash
  brew install graphviz
  ```

- **Linux (Debian/Ubuntu)**:
  ```bash
  sudo apt install graphviz
  ```

> Verificá que el comando `dot` esté disponible con:
> ```bash
> dot -V
> ```

El gráfico se guarda en ./graficos:
- 📄 `arbol.png`
- 📄 `arbol.svg`

---

## 🧠 ¿Qué Aprendimos?

- Representar estructuras no lineales sin objetos
- Realizar operaciones de construcción y búsqueda en árboles implementados con listas anidadas
- Dividir el problema en funciones pequeñas y reutilizables
- Trabajar colaborativamente con control de versiones

---

## ✍️ Autores

- [Luis Cisneros](https://github.com/luiscisneros356)
- [Guillermo Campoy](https://github.com/guillecampoy)

---

## 🏫 Universidad Tecnológica Nacional  
Programación I - Tecnicatura Universitaria en Programación a Distancia  
Año 2025
