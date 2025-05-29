def validar_transacciones(transacciones):
    return list(filter(lambda t: t["vendedor"] and t["cantidad"] > 0 and t["precio"] > 0 and t["region"] in ["Norte", "Sur", "Este", "Oeste"], transacciones))

def calcular_ingreso_y_categoria(transacciones):
    for t in transacciones:
        t["ingreso"] = t["cantidad"] * t["precio"]
        if t["ingreso"] <= 100:
            t["categoria"] = "Baja"
        elif t["ingreso"] <= 500:
            t["categoria"] = "Media"
        else:
            t["categoria"] = "Alta"
    return transacciones

def calcular_bonificacion(transacciones):
    porcentajes = {"Norte": 0.05, "Sur": 0.08, "Este": 0.06, "Oeste": 0.07}
    for t in transacciones:
        t["bonificacion"] = t["ingreso"] * porcentajes.get(t["region"], 0)
    return transacciones

def generar_reporte_ventas(transacciones):
    reportes = []
    for t in transacciones:
        reporte = f"{t['vendedor']} | Región: {t['region']} | Ingreso: {t['ingreso']:.2f} ({t['categoria']}) | Bonificación: {t['bonificacion']:.2f} | ESTADO: PROCESADO"
        reportes.append(reporte)
    return reportes

def pipeline_ventas(transacciones):
    return generar_reporte_ventas(
        calcular_bonificacion(
            calcular_ingreso_y_categoria(
                validar_transacciones(transacciones)
            )
        )
    )
transacciones = [
    {"vendedor": "Carlos", "cantidad": 5, "precio": 10, "region": "Norte"},   # Ingreso 50 - Baja
    {"vendedor": "Lucía", "cantidad": 20, "precio": 30, "region": "Sur"},    # Ingreso 600 - Alta
    {"vendedor": "", "cantidad": 10, "precio": 15, "region": "Este"},        # Inválido
    {"vendedor": "Marta", "cantidad": 10, "precio": 40, "region": "Oeste"}   # Ingreso 400 - Media
]

print("=== Versión Secuencial ===")
for r in procesar_ventas_secuencial(transacciones):
    print(r)

print("\n=== Versión Pipeline ===")
for r in pipeline_ventas(transacciones):
    print(r)
