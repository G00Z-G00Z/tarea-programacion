# Quick Sort vs. Bubble Sort

En este documento, vamos a comparar dos algoritmos de ordenamiento ampliamente utilizados: Quick Sort y Bubble Sort.

## Quick Sort

El Quick Sort es un algoritmo de ordenamiento eficiente y ampliamente utilizado que sigue el paradigma de "divide y vencerás". Fue desarrollado por Tony Hoare en 1960 y es conocido por su velocidad y rendimiento en la mayoría de los casos. Aquí hay una descripción básica del algoritmo:

1. **Dividir:** Se elige un elemento pivot de la lista y se reorganizan los elementos de manera que los elementos menores que el pivot estén a su izquierda y los elementos mayores a su derecha.

2. **Conquistar:** Se aplica el mismo proceso de manera recursiva a las dos sublistas generadas, una a la izquierda del pivot y otra a la derecha, hasta que todas las sublistas estén ordenadas.

3. **Combinar:** No es necesario combinar explícitamente, ya que las sublistas se ordenan de manera recursiva.

El Quick Sort tiene una complejidad promedio de tiempo de O(n log n) y es muy eficiente en la práctica.

## Bubble Sort

El Bubble Sort es un algoritmo de ordenamiento simple y fácil de entender, pero no es eficiente en comparación con otros algoritmos. Funciona de la siguiente manera:

1. Compara cada par de elementos adyacentes en la lista y los intercambia si están en el orden incorrecto.

2. Repite este proceso para cada par de elementos en la lista, pasando por la lista varias veces hasta que ningún intercambio sea necesario.

3. El algoritmo se detiene cuando la lista está completamente ordenada.

El Bubble Sort tiene una complejidad promedio de tiempo de O(n^2), lo que lo hace ineficiente para grandes conjuntos de datos. Es principalmente utilizado para propósitos educativos o en situaciones en las que la simplicidad es más importante que la eficiencia.

## Comparación

| Algoritmo     | Eficiencia promedio | Peor caso     | Mejor caso   | Espacio adicional | Estabilidad |
|---------------|----------------------|--------------|--------------|--------------------|-------------|
| Quick Sort    | O(n log n)          | O(n^2)       | O(n log n)  | O(log n)           | No          |
| Bubble Sort   | O(n^2)               | O(n^2)       | O(n)         | O(1)               | Sí          |

En resumen, el Quick Sort es un algoritmo de ordenamiento más eficiente que el Bubble Sort en la mayoría de los casos, especialmente para grandes conjuntos de datos. Mientras que el Quick Sort utiliza la estrategia "divide y vencerás" para ordenar eficientemente, el Bubble Sort es más simple pero menos eficiente y se utiliza principalmente con fines educativos o en situaciones con conjuntos de datos pequeños.