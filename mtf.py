def move_to_front(lista, secuencia):
    historial = []
    costo_total = 0

    for solicitud in secuencia:
        costo = lista.index(solicitud) + 1
        costo_total += costo
        historial.append({
            "lista_antes": lista.copy(),
            "solicitud": solicitud,
            "costo": costo
        })

        lista.remove(solicitud)
        lista.insert(0, solicitud)

        historial[-1]["lista_despues"] = lista.copy()

    return costo_total, historial
