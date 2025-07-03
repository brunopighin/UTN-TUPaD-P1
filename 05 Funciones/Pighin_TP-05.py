
# Practico 2: Funciones en Python
# Alumno: Bruno Pighin


# 1. imprimir_hola_mundo
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Llamada a la funcion
imprimir_hola_mundo()

# 2. saludar_usuario(nombre)
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal
nombre = input("Ingresá tu nombre: ")
print(saludar_usuario(nombre))

# 3. informacion_personal(nombre, apellido, edad, residencia)
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# 4. calcular_area_circulo y calcular_perimetro_circulo
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
radio = float(input("Ingresa el radio del circulo: "))
print(f"area: {calcular_area_circulo(radio):.2f}")
print(f"Perimetro: {calcular_perimetro_circulo(radio):.2f}")

# 5. segundos_a_horas(segundos)
def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segundos = int(input("Ingresa la cantidad de segundos: "))
print(f"Equivalente en horas: {segundos_a_horas(segundos):.2f}")

# 6. tabla_multiplicar(numero)
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
num = int(input("Ingresa un numero: "))
tabla_multiplicar(num)

# 7. operaciones_basicas(a, b)
def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b if b != 0 else "Division por cero")

# Programa principal
a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}, Resta: {resultados[1]}, Multiplicacion: {resultados[2]}, Division: {resultados[3]}")

# 8. calcular_imc(peso, altura)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
print(f"Tu IMC es: {calcular_imc(peso, altura):.2f}")

# 9. celsius_a_fahrenheit(celsius)
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Programa principal
celsius = float(input("Ingresa la temperatura en grandos c: "))
print(f"Temperatura en Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}°F")

# 10. calcular_promedio(a, b, c)
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
a = float(input("Primer numero: "))
b = float(input("Segundo numero: "))
c = float(input("Tercer numero: "))
print(f"Promedio: {calcular_promedio(a, b, c):.2f}")
