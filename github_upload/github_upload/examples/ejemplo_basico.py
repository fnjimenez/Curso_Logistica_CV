"""
Ejemplo Básico - Modelo de Transporte de 1 Nivel

Este ejemplo muestra cómo usar el modelo clásico de transporte directo.
"""

import sys
from pathlib import Path

# Agregar directorio src al path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from models import PLANTAS, CENTROS_DISTRIBUCION, CIUDADES_DEMANDA
from models import COSTOS_PLANTA_CD, COSTOS_CD_CIUDAD
from models import resolver_red_multinivel, generar_reporte

print("="*70)
print("EJEMPLO BÁSICO - MODELO MULTI-NIVEL")
print("="*70)

# Paso 1: Configuración
print("\n📊 Paso 1: Configuración de la Red")
print(f"   • Plantas: {len(PLANTAS)}")
print(f"   • Centros de Distribución: {len(CENTROS_DISTRIBUCION)}")
print(f"   • Ciudades: {len(CIUDADES_DEMANDA)}")

# Paso 2: Resolver
print("\n🔄 Paso 2: Resolviendo modelo de optimización...")
resultado = resolver_red_multinivel(
    PLANTAS,
    CENTROS_DISTRIBUCION,
    CIUDADES_DEMANDA,
    COSTOS_PLANTA_CD,
    COSTOS_CD_CIUDAD,
    incluir_costos_fijos=True,
    verbose=False
)

# Paso 3: Mostrar resultados
print("\n✅ Paso 3: Resultados")
print(f"   • Status: {resultado['status']}")
print(f"   • Costo Total: ${resultado['costo_total']:,.2f} MXN")
print(f"   • CDs Activos: {len(resultado['cds_activos'])}")
print(f"   • Rutas Nivel 1: {len(resultado['flujos_planta_cd'])}")
print(f"   • Rutas Nivel 2: {len(resultado['flujos_cd_ciudad'])}")

# Paso 4: Análisis de utilización
print("\n📈 Paso 4: Análisis de Utilización")
print("\n   Plantas:")
for planta, util in resultado['utilizacion_plantas'].items():
    print(f"      • {planta}: {util:.1%}")

print("\n   Centros de Distribución Activos:")
for cd in resultado['cds_activos']:
    util = resultado['utilizacion_cds'][cd]
    print(f"      • {cd}: {util:.1%}")

# Paso 5: Top rutas
print("\n🚚 Paso 5: Top 5 Rutas por Volumen")
print("\n   Nivel 1 (Planta → CD):")
flujos_ordenados = sorted(
    resultado['flujos_planta_cd'].items(),
    key=lambda x: x[1],
    reverse=True
)[:5]
for (origen, destino), volumen in flujos_ordenados:
    print(f"      • {origen} → {destino}: {volumen:,} unidades")

print("\n   Nivel 2 (CD → Ciudad):")
flujos_ordenados = sorted(
    resultado['flujos_cd_ciudad'].items(),
    key=lambda x: x[1],
    reverse=True
)[:5]
for (origen, destino), volumen in flujos_ordenados:
    print(f"      • {origen} → {destino}: {volumen:,} unidades")

print("\n" + "="*70)
print("✅ EJEMPLO COMPLETADO")
print("="*70)

# Opcional: Generar visualización
try:
    from models import visualizar_red_multinivel
    import matplotlib.pyplot as plt
    
    print("\n📊 Generando visualización...")
    fig = visualizar_red_multinivel(
        resultado,
        PLANTAS,
        CENTROS_DISTRIBUCION,
        CIUDADES_DEMANDA,
        filename='../results/ejemplo_basico.png'
    )
    plt.show()
    print("✅ Visualización guardada en results/ejemplo_basico.png")
except Exception as e:
    print(f"⚠️ No se pudo generar visualización: {e}")
