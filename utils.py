def imprimir_resultado(historial, costo_total):
    print(f"{'Lista antes':<25} {'Solicitud':<10} {'Costo':<6} {'Lista después'}")
    print("-" * 70)

    for paso in historial:
        antes = str(paso['lista_antes'])
        solicitud = paso['solicitud']
        costo = paso['costo']
        despues = str(paso['lista_despues'])

        print(f"{antes:<25} {solicitud:<10} {costo:<6} {despues}")

    print("-" * 70)
    print(f"Costo total de acceso: {costo_total}\n")
