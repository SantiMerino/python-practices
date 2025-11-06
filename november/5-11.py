ph_rio = []

ph_rio = [
    [7.2, 7.4, 7.1, 7.3, 7.0, 6.9],  
    [6.8, 7.0, 6.9, 7.1, 7.2, 6.8], 
    [7.5, 7.6, 7.4, 7.3, 7.5, 7.4], 
    [6.9, 7.1, 7.0, 7.2, 7.1, 7.0]]


def ingresar_datos():
    """
    Solicita al usuario ingresar valores de pH para 4 ríos durante 6 días.

    El usuario ingresa los datos mediante la función `input()`. 
    Los valores se agregan a la lista global `ph_rio`.

    Returns:
        None
    """
    for j in range(4):
        data = []
        for i in range(6):
            dato = float(input(f'Rio {j+1}: Ingrese valor de ph del día {i+1}: '))
            data.append(dato)
        ph_rio.append(data)
    print(f'Datos ingresados: {ph_rio}')


def calcular_promedio_por_rio():
    """
    Calcula el promedio semanal de pH para cada río y el promedio general.

    Utiliza la lista global `ph_rio` para realizar los cálculos.
    Imprime:
        - Promedio semanal por río (lista)
        - Promedio general (float)

    Returns:
        None
    """
    promedio_semanal = []
    for rio in ph_rio:
        promedio_semanal.append(round(sum(rio)/6, 2))
    print(f'Promedio semanal por río: {promedio_semanal}')
    print(f'Promedio general: {round(sum(promedio_semanal)/4, 2)}')


def generar_analisis_de_estabilidad():
    """
    Analiza la estabilidad del pH en cada río según su variabilidad.

    Criterio:
        - Estable: variabilidad <= 0.3
        - Inestable: variabilidad > 0.3

    Imprime:
        - Variabilidad por río
        - Clasificación (Estable/Inestable)
        - Porcentaje de ríos estables

    Returns:
        None
    """
    variabilidad_general = []
    for rio in ph_rio:
        variabilidad_rio = round(max(rio) - min(rio), 2)
        variabilidad_general.append(variabilidad_rio)
    print(f'Variabilidad por río: {variabilidad_general}')

    estabilidad_general = []
    for valor in variabilidad_general:
        if valor <= 0.3:
            estabilidad_general.append('Estable')
        else:
            estabilidad_general.append('Inestable')
    print(f'Clasificación: {estabilidad_general}')

    cantidad_estable = estabilidad_general.count("Estable")
    porcentaje = round((cantidad_estable / 4) * 100, 2)
    print(f'Porcentaje de ríos estables: {porcentaje} %')


def verificar_alertas_de_riesgo():
    """
    Verifica si hay valores de pH fuera del rango seguro (6.5 - 8.5).

    Imprime:
        - Cantidad total de valores fuera de rango
        - Río con más alertas (o 'ninguno' si no hay alertas)

    Returns:
        None
    """
    fuera_rango = 0
    total_alertas_rio = []
    for rio in ph_rio:
        alertas_rio = 0
        for i in range(len(rio)):
            if rio[i] < 6.5 or rio[i] > 8.5:
                fuera_rango += 1
                alertas_rio += 1
        total_alertas_rio.append(alertas_rio)

    print(f'Valores fuera de rango: {fuera_rango}')
    if sum(total_alertas_rio) == 0:
        print(f'Río con más alertas: ninguno')
    else:
        max_alertas = max(total_alertas_rio)
        rio_peligroso = total_alertas_rio.index(max_alertas)
        print(f'Río con más alertas: {rio_peligroso+1}')
    # Verificar si existe un riesgo de contaminación
    if sum(total_alertas_rio) > 0.2:
        print('Existen alertas de riesgo de contaminación')
    else:
        print('No existen alertas de riesgo de contaminación')


def menu_principal():
    """
    Muestra el menú principal y gestiona las opciones del usuario.

    Imprime:
        - Menú principal
        - Opciones del menú
        - Resultados de las opciones
        - Salida del programa
    Returns:
        None
    """
    is_active_app = True
    while is_active_app:
        print('1. Ingresar datos')
        print('2. Calcular promedio por río y general')
        print('3. Generar análisis de estabilidad')
        print('4. Verificar alertas de riesgo')
        print('5. Salir')
        opcion = int(input('Ingrese opción: '))
        if opcion == 1:
            ingresar_datos()
        elif opcion == 2:
            calcular_promedio_por_rio()
        elif opcion == 3:
            generar_analisis_de_estabilidad()
        elif opcion == 4:
            verificar_alertas_de_riesgo()
        elif opcion == 5:
            print('Saliendo del programa... ¡hasta luego!')
            is_active_app = False

menu_principal()
