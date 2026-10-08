# 1. FUNCIÓN BÁSICA
# Emily Barraza NC = 0025
def saludar():
    print("¡Hola, mundo!")

saludar()

# ----------------------------------------

# 2. FUNCIÓN CON PARÁMETROS
def calcular_area_rectangulo(ancho, alto):
    area = ancho * alto
    return area

resultado = calcular_area_rectangulo(5, 10)
print(resultado)

# ----------------------------------------

# 3. FUNCIÓN CON RETURN
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)

# ----------------------------------------

# 4. FUNCIÓN CON VALOR POR DEFECTO
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"

print(saludar("María"))
print(saludar("Pedro", "Buenos días"))

# ----------------------------------------

# 5. FUNCIÓN CON *ARGS
def sumar_todos(*numeros):
    total = 0

    for num in numeros:
        total += num

    return total

print(sumar_todos(1, 2, 3))
print(sumar_todos(10, 20, 30, 40))
print("Emily Barraza NC = 0025")