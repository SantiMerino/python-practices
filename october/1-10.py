tareas_pendientes = ['Prueba1', 'Prueba2', 'Prueba3']
tareas_finalizadas = ['Hecha1', 'Hecha2']

while True:
    print("\033[1m====== Menú de Tareas ======\033[0m")
    print("\033[1m1. Agregar tarea\033[0m")
    print("\033[1m2. Mostrar tareas\033[0m")
    print("\033[1m3. Marcar tarea como finalizada\033[0m")
    print("\033[1m4. Mostrar tareas pendientes\033[0m")
    print("\033[1m5. Mostrar las ultimas 3 tareas agregadas\033[0m")
    print("\033[1m6. Mostrar tareas alfabeticamente\033[0m")
    print("\033[1m7. Salir\033[0m")
    print("\033[1m============================\033[0m")
    opcion = input("\033[1mSeleccione una opción (1-7):\033[0m ")

    if opcion == '1':
        tarea = input("Ingrese la tarea: ")
        tareas_pendientes.append(tarea)
        print("\033[92mTarea agregada.\033[0m")

    elif opcion == '2':
        print("\033[91mTareas Pendientes:\033[0m")
        # index, task in [(1, 'a'), (2, 'b'), (3, 'c')] par ordenado
        # enumerate(list, starter)
        for idx, tarea in enumerate(tareas_pendientes, 1):
            print(f"{idx}. {tarea}")
        print("\033[94m\nTareas Finalizadas:\033[0m")
        for idx, tarea in enumerate(tareas_finalizadas, 1):
            print(f"{idx}. {tarea}")

    elif opcion == '3':
        if not tareas_pendientes:
            print("No hay tareas pendientes para marcar como finalizadas.")
        else:
            print("\033[91mTareas Pendientes:\033[0m")
            for idx, tarea in enumerate(tareas_pendientes, 1):
                print(f"{idx}. {tarea}")
            # Al momento de ingresar el número de tarea, se resta 1 para obtener el índice correcto
            tarea_idx = int(input("Ingrese el número de la tarea que desea marcar como finalizada: ")) - 1
            if 0 <= tarea_idx < len(tareas_pendientes):
                # pop(index) elimina y retorna el elemento en la posición index
                tarea_finalizada = tareas_pendientes.pop(tarea_idx)
                tareas_finalizadas.append(tarea_finalizada)
                print("Tarea marcada como finalizada.")
            else:
                print("Número de tarea inválido.")
    elif opcion == '4':
        pend = input("Ingrese el nombre de la tarea pendiente a buscar:")
        if pend in tareas_pendientes:
            print(f"La tarea '{pend}' está en la lista de tareas pendientes.")
        else:
            print(f"La tarea '{pend}' no se encuentra en la lista de tareas pendientes.")

    elif opcion == '5':
        print("\033[91mÚltimas 3 tareas pendientes:\033[0m")
        # sublista de los ultimos 3 elementos
        if len(tareas_pendientes) < 3:
            for tarea in tareas_pendientes:
                print(f"- {tarea}")
        else:
            for tarea in tareas_pendientes[-3:]:
                print(f"- {tarea}")
    elif opcion == '6':
        print("Tareas Pendientes en orden alfabético:")
        for idx, tarea in enumerate(sorted(tareas_pendientes), 1):
            print(f"{idx}- {tarea}")

    elif opcion == '7':
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor seleccione una opción del 1 al 7.")