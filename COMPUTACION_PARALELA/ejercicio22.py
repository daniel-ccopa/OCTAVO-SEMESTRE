def pipeline_etapas(datos):
    print("\nEtapa 1: Duplicar los números")
    etapa1 = [x * 2 for x in datos]
    print("Resultado etapa 1:", etapa1)

    print("\nEtapa 2: Sumar 10")
    etapa2 = [x + 10 for x in etapa1]
    print("Resultado etapa 2:", etapa2)

    print("\nEtapa 3: Elevar al cuadrado")
    etapa3 = [x ** 2 for x in etapa2]
    print("Resultado etapa 3:", etapa3)

    print("\nEtapa 4: Dividir entre 5")
    etapa4 = [x / 5 for x in etapa3]
    print("Resultado etapa 4:", etapa4)

    return etapa4

# Datos de entrada
datos = [3, 7, 2, 9, 5]

# Ejecutar función
resultados = pipeline_etapas(datos)
print("\nResultados finales:", resultados)