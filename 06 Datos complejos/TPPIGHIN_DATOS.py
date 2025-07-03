
# TP 6 - Estructuras de Datos Complejas - SIN OBJETOS

# 1) Crear el diccionario inicial y agregar frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Actualizar precios de frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Crear una lista con solo los nombres de las frutas
lista_frutas = list(precios_frutas.keys())

# 4) Agenda de contactos telefónicos
contactos = {}
for _ in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    contactos[nombre] = numero

buscar = input("Ingrese el nombre para buscar el número: ")
if buscar in contactos:
    print(f"El número de {buscar} es {contactos[buscar]}")
else:
    print("Contacto no encontrado.")

# 5) Análisis de frase
frase = input("Ingrese una frase: ").lower()
palabras = frase.split()
palabras_unicas = set(palabras)

conteo_palabras = {}
for palabra in palabras:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Cantidad de cada palabra:", conteo_palabras)

# 6) Notas de alumnos
notas_alumnos = {}
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese la nota {i+1} de {nombre}: ")) for i in range(3))
    notas_alumnos[nombre] = notas

for alumno, notas in notas_alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {alumno}: {promedio:.2f}")

# 7) Análisis de aprobados
parcial1 = {101, 102, 103, 104}
parcial2 = {103, 104, 105}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# 8) Inventario de productos
stock = {'lapiz': 10, 'cuaderno': 5}
producto = input("Ingrese el producto a consultar o modificar: ")

if producto in stock:
    cantidad = int(input("Ingrese la cantidad a agregar: "))
    stock[producto] += cantidad
    print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    cantidad = int(input("Producto nuevo. Ingrese el stock inicial: "))
    stock[producto] = cantidad
    print(f"{producto} agregado con stock: {cantidad}")

# 9) Agenda con tuplas
agenda = {
    ('lunes', '10:00'): 'Reunión de equipo',
    ('martes', '14:00'): 'Llamada con cliente'
}
dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (hh:mm): ")

evento = agenda.get((dia, hora))
if evento:
    print(f"Actividad programada: {evento}")
else:
    print("No hay actividad programada para ese horario.")

# 10) Invertir diccionario de países y capitales
paises = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Francia': 'París',
    'Italia': 'Roma'
}

capitales = {capital: pais for pais, capital in paises.items()}
print("Diccionario invertido:", capitales)
