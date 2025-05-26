def proceso_secuencial(datos):
    resultados=[]
    for dato in datos:
        # primera etapa convertir a entero y multiplicar por 2
        etapa1 = int(dato) * 2
        print(f"Etapa 1: {dato} -> {etapa1}")
        # segunda etapa elevar al cuadrado
        etapa2 = etapa1 ** 2  # CORREGIDO: operador de potencia
        print(f"etapa2: {etapa1} -> {etapa2}")
        # tercera etapa añadir prefijo
        etapa3 = f"Resultado: {etapa2}"
        print(f"etapa3: {etapa2} -> {etapa3}")
        resultados.append(etapa3)
    return resultados

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

import time
#crear la funcion que compara los resultados
def comparar_resultados(datos):
    #medir el proceso secuencial8
    inicio = time.time()
    resultados_secuencial = proceso_secuencial(datos)
    tiempo_secuencial = time.time() - inicio

    #medir proceso en pipeline
    inicio = time.time()
    resultados_pipeline = procesar_pipeline(datos)
    tiempo_pipeline = time.time() - inicio
    
    print(f"Resultados Secuencial: {tiempo_secuencial:.6f}s")
    print(f"Resultados Pipeline: {tiempo_pipeline:.6f}s")

    return resultados_secuencial, resultados_pipeline
def main():
    datos = ["1", "2", "3", "4"]
    comparar_resultados(datos)

if __name__ == "__main__":
    main()

