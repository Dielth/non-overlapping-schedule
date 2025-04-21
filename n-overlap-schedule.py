# Función para elegir actividades sin choques de horario
def elegir_actividades(lista_actividades):
    # Ordenamos por hora de finalización (la que termina primero va primero)
    actividades_ordenadas = sorted(lista_actividades, key=lambda x: x["fin"])

    if not actividades_ordenadas:
        return []

    seleccionadas = [actividades_ordenadas[0]]  # Siempre tomamos la primera
    ultima_hora = actividades_ordenadas[0]["fin"]  # Hora en que termina

    # Vamos comparando con las demás
    for act in actividades_ordenadas[1:]:
        if act["inicio"] >= ultima_hora:  # Si no choca
            seleccionadas.append(act)
            ultima_hora = act["fin"]  # Actualizamos la hora de fin

    return [act["nombre"] for act in seleccionadas]  # Solo los nombres


# Actividades iniciales (las que vienen por defecto)
actividades = [
    {"nombre": "A1", "inicio": 1, "fin": 4},
    {"nombre": "A2", "inicio": 3, "fin": 5},
    {"nombre": "A3", "inicio": 0, "fin": 6},
    {"nombre": "A5", "inicio": 5, "fin": 7},
    {"nombre": "A6", "inicio": 5, "fin": 9}
]

# Mostramos las actividades que hay
print("\n--- Horario Actual ---")
for act in actividades:
    print(f"{act['nombre']}: de {act['inicio']} a {act['fin']}")

# Preguntamos si quiere cambiar algo
cambiar = input("\n¿Quieres cambiar algún horario? (s/n): ").lower()
while cambiar == "s":
    cual = input("¿Cuál actividad? (ej: A1): ")
    # Buscamos la actividad
    for act in actividades:
        if act["nombre"] == cual:
            nuevo_inicio = int(input(f"Nuevo inicio para {cual}: "))
            nuevo_fin = int(input(f"Nuevo fin para {cual}: "))
            if nuevo_inicio >= nuevo_fin:
                print("¡El inicio debe ser ANTES del fin!⚠️")
            else:
                act["inicio"] = nuevo_inicio
                act["fin"] = nuevo_fin
            break
    else:
        print("¡Esa actividad no existe!⚠️")
    cambiar = input("¿Cambiar otra? (s/n): ").lower()

# Preguntamos si quiere añadir más actividades
añadir_mas = input("\n¿Quieres añadir más actividades? (s/n): ").lower()
while añadir_mas == "s":
    nombre = input("Nombre (ej: A7): ")
    # Verificamos que no exista
    if any(act["nombre"] == nombre for act in actividades):
        print("Nombre en uso")
        continue

    inicio = int(input("Hora inicio: "))
    fin = int(input("Hora fin: "))
    if inicio >= fin:
        print("¡El inicio debe ser antes del fin!")
        continue

    actividades.append({"nombre": nombre, "inicio": inicio, "fin": fin})
    print(f"✅  {nombre} añadida!")
    añadir_mas = input("¿Añadir otra? (s/n): ").lower()

# Mostramos el resultado final
resultado = elegir_actividades(actividades)
print("\n--- Actividades que puedes hacer sin chocar ---")
print(", ".join(resultado))