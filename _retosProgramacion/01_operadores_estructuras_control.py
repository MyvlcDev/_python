""" /*
 * EJERCICIO:
 *  1 - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 *  2 - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 *  3 - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 *  4 - Crea un programa que imprima por consola todos los números comprendidos
 *   entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */ """

""" /*
* 1 - Ejemplo de tipos de operadores del lenguaje python """

import math
from datetime import datetime


# Obtener la fecha y hora actual
fecha_actual = datetime.now()

# Formatear la fecha y hora
fecha_formateada = fecha_actual.strftime("%Y-%m-%d")


# Mostrar la fecha
print("\n\n Fecha:", fecha_formateada)


# * Operaciones Aritmeticas


print("\n## * Operaciones Aritmeticas\n")



var1 =50
var2 =25 

print(f"Suma              :  { var1 }+{ var2 } = {var1+var2}") 
print(f"Resta             :  { var1 }-{ var2 } = {var1-var2}") 
print(f"Producto          :  { var1 }*{ var2 } = {var1+var2}") 
print(f"División          :  { var1 }/{ var2 } = {var1+var2}") 
print(f"Potencia          :  { var1 }**{ var2 } = {var1**var2}") 
print(f"Raiz Cuadrada     :  √{ var1 } = {math.sqrt(var1)}") 
print(f"Modulo            :  { var1 }%{ var2 } = {var1%var2}") 

## * Operaciones Logicas


print("\n## * Operaciones Logicas\n")


# Definir valores booleanos
a = True
b = False

# Operación AND lógico (y)
resultado_and = a and b
print(f'{a} AND {b} = {resultado_and}')

# Operación OR lógico (o)
resultado_or = a or b
print(f'{a} OR {b} = {resultado_or}')

# Operación NOT lógico (no)
resultado_not_a = not a
resultado_not_b = not b
print(f'NOT {a} = {resultado_not_a}')
print(f'NOT {b} = {resultado_not_b}')

# Operaciones de comparación

print("\n# Operaciones de comparación\n")

x = 45
y = 15

# Mayor que
mayor_que = x > y
print(f'{x} > {y} = {mayor_que}')

# Menor que
menor_que = x < y
print(f'{x} < {y} = {menor_que}')

# Igual a
igual_a = x == y
print(f'{x} == {y} = {igual_a}')

# Diferente de
diferente_de = x != y
print(f'{x} != {y} = {diferente_de}')

# Mayor o igual que
mayor_o_igual_que = x >= y
print(f'{x} >= {y} = {mayor_o_igual_que}')

# Menor o igual que
menor_o_igual_que = x <= y
print(f'{x} <= {y} = {menor_o_igual_que}')


# * Operaciones Asignación


print("\n## * Operaciones Asignación\n")

# Asignación simple
x = 5
print (x)
# Asignación con suma
x += 3  # Equivalente a x = x + 3
print (x)

# Asignación con resta
x -= 2  # Equivalente a x = x - 2

# Asignación con multiplicación
x *= 4  # Equivalente a x = x * 4

# Asignación con división
x /= 2  # Equivalente a x = x / 2

# Asignación con módulo
x %= 3  # Equivalente a x = x % 3

# Asignación con división entera
x //= 2  # Equivalente a x = x // 2

# Asignación con exponenciación
x **= 3  # Equivalente a x = x ** 3

# Asignación con AND bit a bit
x &= 2  # Equivalente a x = x & 2

# Asignación con OR bit a bit
x |= 2  # Equivalente a x = x | 2

# Asignación con XOR bit a bit
x ^= 2  # Equivalente a x = x ^ 2

# Asignación con desplazamiento a la derecha
x >>= 1  # Equivalente a x = x >> 1

# Asignación con desplazamiento a la izquierda
x <<= 1  # Equivalente a x = x << 1



