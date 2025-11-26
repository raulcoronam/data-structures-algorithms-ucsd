# 🚀 Módulo 2: Algorithmic Warmup (Análisis de Complejidad)

Este documento sirve como base teórica para entender la eficiencia algorítmica. Aquí aprendemos a medir la calidad de un algoritmo mediante matemáticas y lógica, independiente del hardware.

---

## ⏱️ 1. La Ilusión del Tiempo Real (Runtimes)

### El problema de medir con segundos
Podríamos pensar: *"Para saber cuál algoritmo es mejor, los corro ambos y cronometro cuál termina primero"*.
Esto **NO** es fiable por estas razones:

1.  **Hardware variable:** Tu laptop es más rápida hoy que una computadora de hace 10 años.
2.  **Compilador:** Python, C++ y Java ejecutan la misma lógica a velocidades muy distintas.
3.  **Carga del sistema:** Si tienes muchas apps abiertas, tu algoritmo correrá más lento.

### 🧠 Concepto Clave: Jerarquía de Memoria
Uno de los factores ocultos que más afecta el tiempo real es **dónde están los datos**.
* **Registros CPU / Caché L1/L2:** Es como tener la información en tu mano. Extremadamente rápido.
* **RAM:** Es como tener que levantarte a buscar un libro al estante. Lento.
* **Disco Duro:** Es como tener que ir a la biblioteca pública. Eterno.

> **Conclusión:** No podemos confiar en el tiempo de reloj. Necesitamos una medida que sea **independiente de la máquina**.

---

## 📈 2. Notación Asintótica (El estándar de la industria)

La palabra **"Asintótica"** se refiere al comportamiento de una curva a medida que avanza al infinito.

En algoritmos, nos interesa el **comportamiento a gran escala (Scaling)**.
* No nos importa si el algoritmo es rápido con 10 datos.
* Nos importa: **¿Qué pasa si le metemos 1 millón de datos?** ¿El tiempo se duplica (lineal) o explota (exponencial)?

### La falacia de las "Líneas de Código"

# Caso A: 3 líneas, pero LENTO (Cuadrático)
for i in range(n):
    for j in range(n):
        print(i, j)  # Se ejecuta n*n veces

# Caso B: 1 línea, pero RÁPIDO (Constante)
result = 500 * 1000  # Se ejecuta 1 vez

> **Lección:** Un bucle for vale por $n$ operaciones. Un bucle anidado vale por $n^2$. No cuentes líneas; cuenta operaciones en función de la entrada $N$.

## 🅾️ 3. Big-O Notation ($O$)

Big-O es la herramienta matemática para clasificar algoritmos según su tasa de crecimiento en el peor escenario posible (**Upper Bound**).

### 🤓 Definición Matemática (Traducida)

$$f(n) \le c \cdot g(n)$$

*(para todo $n \ge N$)*

* **$f(n)$:** El tiempo real y "sucio" de tu algoritmo (ej. $3n^2 + 50n + 9$).
* **$g(n)$:** La versión simplificada (ej. $n^2$).
* **$c$ (La constante):** Un "factor de ajuste". No importa si tu PC es 10 veces más lenta ($c=10$); la curva de crecimiento sigue siendo cuadrática. Big-O ignora esto.
* **$N$ (El umbral):** El punto donde el tamaño de la entrada es lo suficientemente grande como para que la clasificación sea válida.

---

## ⚡ 4. Big-O Cheatsheet: Jerarquía de Poder

Ordenado de **Mejor (Rápido)** a **Peor (Lento)**.



[Image of Big O complexity chart]


| Notación | Nombre | Analogía del Mundo Real | Ejemplo Técnico |
| :--- | :--- | :--- | :--- |
| $O(1)$ | Constante | Saber el nombre de la primera persona en una fila. Tardas lo mismo si hay 10 o 1 millón. | `array[index]` |
| $O(\log n)$ | Logarítmico | Buscar en una guía telefónica (o diccionario). Cortas el problema a la mitad en cada paso. | Binary Search |
| $O(n)$ | Lineal | Leer un libro página por página. Si el libro es el doble de grueso, tardas el doble. | Bucle `for` simple |
| $O(n \log n)$ | Linealíthmico | Ordenar una baraja de cartas usando una estrategia eficiente (Merge). | Merge Sort, Quick Sort |
| $O(n^2)$ | Cuadrático | En una fiesta, saludar a cada persona y presentarla con todas las demás. | Bucles anidados |
| $2^n$ | Exponencial | Intentar adivinar una contraseña probando todas las combinaciones posibles. Intratable. | Fibonacci Recursivo |

---

## 🧮 5. Reglas para Simplificar (Math Rules)

Usa estas reglas para encontrar el Big-O de cualquier código rápidamente.

### Regla 1: El rey manda (Dominancia)
Si tu algoritmo hace varias cosas, solo importa la parte más lenta.

$$n^2 + n + 1000 \rightarrow O(n^2)$$

> **Por qué:** Si $n = 1,000,000$, entonces $n^2$ es un billón, mientras que $n$ es solo un millón. El término lineal se vuelve insignificante.

### Regla 2: Ignora las constantes

$$5n^3 \rightarrow O(n^3)$$

> **Por qué:** Nos interesa la forma de la curva, no su pendiente exacta. Un algoritmo cúbico siempre perderá contra uno cuadrado a la larga, sin importar las constantes.

### Regla 3: Jerarquía de Clases

$$\log n < \sqrt{n} < n < n \log n < n^2 < 2^n$$

---

## 🚦 6. Diferencias: $O$, $\Omega$, $\Theta$

En entrevistas o textos académicos verás otros símbolos:

* **Big-O ($O$): El Techo (Peor caso)**
    * "Mi algoritmo nunca tardará más que esto".
    * Es una garantía. Es la más usada en ingeniería de software.
* **Big-Omega ($\Omega$): El Suelo (Mejor caso)**
    * "Mi algoritmo tardará al menos esto".
    * *Ejemplo:* Para encontrar el mínimo en una lista desordenada, al menos debes ver todos los elementos una vez ($\Omega(n)$).
* **Big-Theta ($\Theta$): El Ajuste Exacto**
    * Cuando el techo y el suelo coinciden.
    * "Mi algoritmo siempre se comporta así".

> 💡 **Tip Pro:** Si en una entrevista te preguntan la complejidad, asume que preguntan por **Big-O (Tiempo)** y **Complejidad Espacial (Memoria RAM)**.