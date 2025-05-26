'''
Enunciado: Desarrolla un programa en Python que implemente un
pipeline de procesamiento para transformar una serie de valores de
entrada. El pipeline debe constar de tres etapas:
1 Etapa 1: Convertir el dato a entero y multiplicarlo por 2
2 Etapa 2: Elevar al cuadrado el resultado de la etapa anterior
3 Etapa 3: Convertir el resultado a string y a ̃nadir el texto ”Resultado:
” como prefijo
Implementa dos versiones:
Una versi ́on secuencial donde cada dato pasa por todas las etapas
antes de procesar el siguiente dato
Una versi ́on de pipeline donde cada etapa procesa todos los datos
antes de pasar a la siguiente etapa
Compara los resultados de ambas implementaciones para verificar que son
id ́enticos.
Datos de entrada: [”1”, ”2”, ”3”, ”4”]
Salida esperada: [”Resultado: 4”, ”Resultado: 16”, ”Resultado: 36”,
”Resultado: 64”
'''


def proceso_secuencial(datos):

    resultados=[]
    for dato in datos:
        #primera etapa convertir a entero y multiplicar por 2
        etapa1=int(dato)*2
        print(f"Etapa 1: {dato} -> {etapa1}")
        #segunda etapa elevar al cuadrado
        etapa2=etapa1^2
        print(f"etapa2: {etapa1} -> {etapa2}")
        #tercera etapa a;adir prefijo
        etapa3=f"Resultado: {etapa2}"
        print(f"etapa3: {etapa2} -> {etapa3}")
        resultados.append(etapa3)
    return resultados

datos=["1","2","3","4"]
resultados=proceso_secuencial(datos)
print(resultados)



