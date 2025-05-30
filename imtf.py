def improved_move_to_front(lista, secuencia):
    historial = []
    costo_total = 0
    n = len(secuencia)

    for i in range(n):
        solicitud = secuencia[i]
        idx = lista.index(solicitud)
        costo = idx + 1
        costo_total += costo
        historial.append({
            "lista_antes": lista.copy(),
            "solicitud": solicitud,
            "costo": costo
        })

        lookahead = secuencia[i + 1:i + 1 + (idx)]
        if solicitud in lookahead:
            lista.remove(solicitud)
            lista.insert(0, solicitud)

        historial[-1]["lista_despues"] = lista.copy()

    return costo_total, historial
