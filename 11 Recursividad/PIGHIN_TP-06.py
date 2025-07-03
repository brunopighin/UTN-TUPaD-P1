# Función recursiva para calcular el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Función recursiva para imprimir una frase n veces
def repetir_frase(num, frase):
    if num > 0:
        print(frase)
        repetir_frase(num - 1, frase)

# Función recursiva para sumar los n primeros números
def suma_recursiva(num):
    if num == 0:
        return 0
    else:
        return num + suma_recursiva(num - 1)

# Función recursiva para calcular el n-ésimo número de Fibonacci (corregida)
def fibonacci_recursivo(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)