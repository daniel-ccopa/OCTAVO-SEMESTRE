
import time

def proceso_secuencial(datos):
    resultados=[]
    for dato in datos:
        #primera etapa: duplicar el número
        etapa1=dato*2
        print(f"Etapa 1: {dato} -> {etapa1}")
        #segunda etapa: sumar 10 al número de la etapa anterior
        etapa2= etapa1 + 10
        print(f"Etapa 2: {etapa1} -> {etapa2}")
        #tercera etapa: calcular el cuadrado del resultado de la etapa anterior
        etapa3= etapa2**2
        print(f"Etapa 3: {etapa2} -> {etapa3}")
        #cuarta etapa: dividir el resultado por 5
        etapa4= etapa3/5
        print(f"Etapa 3: {etapa3} -> {etapa4}")
        resultados.append(etapa4)
    return resultados

def proceso_pipeline(datos):
    # ETAPA 1
    etapa1=[]
    for dato in datos:
        resultado=dato*2
        etapa1.append(resultado)
        print(f"{dato} -> {resultado}")
    print(f"Resultados etapa 1: {etapa1}")
    # ETAPA 2
    etapa2=[]
    for dato in etapa1:
        resultado=dato + 10
        etapa2.append(resultado)
        print(f"{dato} -> {resultado}")
    print(f"Resultados etapa 2: {etapa2}")
    # ETAPA 3
    etapa3=[]
    for dato in etapa2:
        resultado=dato**2
        etapa3.append(resultado)
        print(f"{dato} -> {resultado}")
    print(f"Resultados etapa 3: {etapa3}")
    # ETAPA 4
    etapa4=[]
    for dato in etapa3:
        resultado=dato/5
        etapa4.append(resultado)
        print(f"{dato} -> {resultado}")
    print(f"Resultados etapa 4: {etapa4}")
    return etapa4

def comparar_rendimiento(datos):
    # Medir el proceso secuencial
    inicio=time.time()
    resultado_secuencial=proceso_secuencial(datos)
    tiempo_secuencial=time.time() -inicio

    # Medir el proceso pipeline
    inicio=time.time()
    resultado_pipeline=proceso_pipeline(datos)
    tiempo_pipeline=time.time() -inicio

    print(f"Secuencial: {tiempo_secuencial:.6f}s")
    print(f"Pipeline: {tiempo_pipeline:.6f}s")

    return tiempo_secuencial, tiempo_pipeline

def main():
    datos=[3,7,2,9,5]
    comparar_rendimiento(datos)

if __name__ == "__main__":
    main()

