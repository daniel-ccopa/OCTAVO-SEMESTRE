from multiprocessing import Process, Pipe

def etapa1_validacion(in_pipe, out_pipe):
    while True:
        estudiante = in_pipe.recv()
        if estudiante is None:
            out_pipe.send(None)
            break
        # Validación
        if (estudiante['nombre'] and 
            16 <= estudiante['edad'] <= 65 and 
            0 <= estudiante['nota'] <= 20):
            out_pipe.send(estudiante)

def etapa2_categoria(in_pipe, out_pipe):
    while True:
        estudiante = in_pipe.recv()
        if estudiante is None:
            out_pipe.send(None)
            break
        # Categoría por edad
        if 16 <= estudiante['edad'] <= 25:
            estudiante['categoria'] = 'Joven'
        elif 26 <= estudiante['edad'] <= 45:
            estudiante['categoria'] = 'Adulto'
        else:
            estudiante['categoria'] = 'Mayor'
        out_pipe.send(estudiante)

def etapa3_estado(in_pipe, out_pipe):
    while True:
        estudiante = in_pipe.recv()
        if estudiante is None:
            out_pipe.send(None)
            break
        # Estado académico
        if estudiante['nota'] <= 10.5:
            estudiante['estado'] = 'Desaprobado'
        elif estudiante['nota'] <= 15.5:
            estudiante['estado'] = 'Aprobado'
        else:
            estudiante['estado'] = 'Excelente'
        out_pipe.send(estudiante)

def etapa4_reporte(in_pipe, resultados):
    while True:
        estudiante = in_pipe.recv()
        if estudiante is None:
            break
        # Formatear reporte
        reporte = (
            f"Nombre: {estudiante['nombre']}\n"
            f"Edad: {estudiante['edad']} ({estudiante['categoria']})\n"
            f"Nota: {estudiante['nota']} ({estudiante['estado']})\n"
            "----------------------"
        )
        resultados.append(reporte)

def pipeline_estudiantes(datos):
    # Crear pipes
    pipe1_2a, pipe1_2b = Pipe()
    pipe2_3a, pipe2_3b = Pipe()
    pipe3_4a, pipe3_4b = Pipe()
    
    resultados = []
    
    # Crear procesos
    p1 = Process(target=etapa1_validacion, args=(pipe1_2a, pipe1_2b))
    p2 = Process(target=etapa2_categoria, args=(pipe2_3a, pipe2_3b))
    p3 = Process(target=etapa3_estado, args=(pipe3_4a, pipe3_4b))
    p4 = Process(target=etapa4_reporte, args=(pipe3_4b, resultados))
    
    # Iniciar procesos
    p1.start(); p2.start(); p3.start(); p4.start()
    
    # Enviar datos
    for estudiante in datos:
        pipe1_2a.send(estudiante)
    pipe1_2a.send(None)  # Señal de terminación
    
    # Esperar a que terminen
    p1.join(); p2.join(); p3.join(); p4.join()
    
    return resultados

# Interfaz para probar
def probar_estudiantes():
    estudiantes = []
    print("\nINGRESE DATOS DE ESTUDIANTES (deje nombre vacío para terminar):")
    while True:
        nombre = input("Nombre: ")
        if not nombre:
            break
        edad = int(input("Edad (16-65): "))
        nota = float(input("Nota (0-20): "))
        estudiantes.append({'nombre': nombre, 'edad': edad, 'nota': nota})
    
    print("\nPROCESANDO...")
    resultados = pipeline_estudiantes(estudiantes)
    
    print("\nRESULTADOS:")
    for reporte in resultados:
        print(reporte)