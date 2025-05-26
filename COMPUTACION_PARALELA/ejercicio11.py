def procesar_pipeline(datos):
    # etapa1
    etapa1 = []
    for dato in datos:
        resultado = int(dato) * 2
        etapa1.append(resultado)
        print(f"{dato} -> {resultado}")
    print(f"Resultaditos de etapa 1: {etapa1}")

    # etapa2
    etapa2 = []
    for dato in etapa1:
        resultado = dato ** 2
        etapa2.append(resultado)
        print(f"{dato} -> {resultado}")
    print(f"Resultaditos de etapa 2: {etapa2}")

    # etapa3
    etapa3 = []
    for dato in etapa2:
        resultado = f"Resultado: {dato}"
        etapa3.append(resultado)
        print(f"{dato} -> {resultado}")
    print(f"Resultaditos de etapa 3: {etapa3}")
    return etapa3

datos = ["1", "2", "3", "4"]
resultado = procesar_pipeline(datos)
print(resultado)