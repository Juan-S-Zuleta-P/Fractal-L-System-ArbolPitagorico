import turtle # Importamos la librería turtle para dibujar gráficos

# Definimos el axioma y las reglas de producción
axioma = "0"
reglas = {"1": "11", "0": "1[0]0"}

# Número de iteraciones
iteraciones = 6

# Aplicamos las reglas de producción iterativamente
cadena = axioma
for i in range(iteraciones): # Se itera el número de veces especificado por la variable 'iteraciones'
    nueva_cadena = "" # Se crea una nueva cadena vacía 'nueva_cadena'
    for caracter in cadena: # Se recorre cada símbolo de la cadena actual 'cadena'
        if caracter in reglas: # Se verifica si ese símbolo tiene una regla de producción definida en el diccionario 'reglas'
            nueva_cadena += reglas[caracter] # Si tiene regla de producción definida, se reemplaza el símbolo con la cadena correspondiente definida en 'reglas'
        else:
            nueva_cadena += caracter # Si no tiene regla de producción definida, simplemente se agrega el mismo símbolo a la nueva cadena
    cadena = nueva_cadena # Se actualiza la variable 'cadena' con la nueva cadena generada en esta iteración

# Dibujamos el árbol de Pitágoras utilizando turtle
t = turtle.Turtle()
t.speed("fastest")
t.left(90) # Orientamos la tortuga hacia arriba
t.penup() # Levantamos el lápiz
t.pendown() # Bajamos el lápiz
stack = [] # Creamos una pila vacía para almacenar las posiciones de la tortuga y su dirección

for caracter in cadena:
    if caracter == "0" or caracter == "1": # Si el caracter es 0 o 1
        t.forward(5) # Avanzamos 5 píxeles hacia adelante
    elif caracter == "[":
        stack.append((t.position(), t.heading())) # Guardamos la posición y la dirección actual de la tortuga en la pila
        t.left(45) # Giramos a la izquierda 45 grados
    elif caracter == "]":
        position, heading = stack.pop() # Recuperamos la última posición y dirección guardadas en la pila
        t.penup() # Levantamos el lápiz
        t.goto(position) # Nos movemos a la última posición guardada en la pila
        t.setheading(heading) # Establecemos la dirección de la tortuga a la última dirección guardada en la pila
        t.pendown() # Bajamos el lápiz
        t.right(45) # Giramos a la derecha 45 grados

turtle.done() # Espera a que el usuario cierre la ventana de dibujo
