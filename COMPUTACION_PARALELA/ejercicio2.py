def pipeline_secuencial(datos):
    resultados = []
    for numero in datos:
        print(f"\nNúmero original: {numero}")
        # Etapa 1: duplicar el número
        etapa1 = numero * 2
        print(f"Etapa 1: {numero} * 2 = {etapa1}")
        # Etapa 2: sumar 10
        etapa2 = etapa1 + 10
        print(f"Etapa 2: {etapa1} + 10 = {etapa2}")
        # Etapa 3: elevar al cuadrado
        etapa3 = etapa2 ** 2
        print(f"Etapa 3: {etapa2} ** 2 = {etapa3}")
        # Etapa 4: dividir entre 5
        etapa4 = etapa3 / 5
        print(f"Etapa 4: {etapa3} / 5 = {etapa4}")
        resultados.append(etapa4)
    return resultados

# Datos de entrada
datos = [3, 7, 2, 9, 5]

# Ejecutar función
resultados = pipeline_secuencial(datos)
print("\nResultados finales:", resultados)