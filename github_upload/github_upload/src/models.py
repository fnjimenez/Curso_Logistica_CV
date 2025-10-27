"""
Amazon Logistics - Modelo Multi-Nivel (2 Niveles)
Implementación completa de red con Centros de Distribución intermedios

Estructura:
    Nivel 1: Plantas/Fábricas → Centros Distribución Regionales
    Nivel 2: Centros Distribución → Ciudades Finales

Autor: Mejora basada en auditoría
Fecha: Octubre 2025
"""

import networkx as nx
import matplotlib.pyplot as plt
from pulp import *
import numpy as np

# ============================================================================
# CONFIGURACIÓN DE LA RED MULTI-NIVEL
# ============================================================================

# NIVEL 1: Plantas/Fábricas (Nodos de Oferta/Producción)
PLANTAS = {
    'Planta_Norte': {
        'capacidad': 80000,
        'ubicacion': 'Monterrey',
        'costo_operacion': 50  # costo fijo por unidad producida
    },
    'Planta_Centro': {
        'capacidad': 100000,
        'ubicacion': 'CDMX',
        'costo_operacion': 45
    },
    'Planta_Bajio': {
        'capacidad': 60000,
        'ubicacion': 'Querétaro',
        'costo_operacion': 48
    },
    'Planta_Sur': {
        'capacidad': 50000,
        'ubicacion': 'Puebla',
        'costo_operacion': 52
    },
}

# NIVEL 2: Centros de Distribución Regionales (Nodos Intermedios)
CENTROS_DISTRIBUCION = {
    'CD_Norte': {
        'capacidad': 55000,
        'ubicacion': 'Monterrey',
        'costo_manejo': 5  # costo por unidad manejada
    },
    'CD_Centro': {
        'capacidad': 75000,
        'ubicacion': 'CDMX',
        'costo_manejo': 4
    },
    'CD_Bajio': {
        'capacidad': 48000,
        'ubicacion': 'Guadalajara',
        'costo_manejo': 5
    },
    'CD_Sur': {
        'capacidad': 38000,
        'ubicacion': 'Veracruz',
        'costo_manejo': 6
    },
}

# NIVEL 3: Ciudades Finales (Nodos de Demanda)
CIUDADES_DEMANDA = {
    'Toluca': 27000,
    'León': 21000,
    'San Luis Potosí': 17000,
    'Cancún': 17000,
    'Mérida': 18000,
    'Veracruz': 20000,
}

# COSTOS DE TRANSPORTE NIVEL 1: Planta → Centro Distribución
# (costo en pesos mexicanos por unidad transportada)
COSTOS_PLANTA_CD = {
    # Desde Planta_Norte
    ('Planta_Norte', 'CD_Norte'): 3.0,      # Local
    ('Planta_Norte', 'CD_Centro'): 48.0,    # Monterrey → CDMX
    ('Planta_Norte', 'CD_Bajio'): 42.0,     # Monterrey → Guadalajara
    ('Planta_Norte', 'CD_Sur'): 85.0,       # Monterrey → Veracruz
    
    # Desde Planta_Centro
    ('Planta_Centro', 'CD_Norte'): 50.0,    # CDMX → Monterrey
    ('Planta_Centro', 'CD_Centro'): 2.0,    # Local
    ('Planta_Centro', 'CD_Bajio'): 38.0,    # CDMX → Guadalajara
    ('Planta_Centro', 'CD_Sur'): 55.0,      # CDMX → Veracruz
    
    # Desde Planta_Bajio
    ('Planta_Bajio', 'CD_Norte'): 45.0,     # Querétaro → Monterrey
    ('Planta_Bajio', 'CD_Centro'): 20.0,    # Querétaro → CDMX
    ('Planta_Bajio', 'CD_Bajio'): 25.0,     # Querétaro → Guadalajara
    ('Planta_Bajio', 'CD_Sur'): 65.0,       # Querétaro → Veracruz
    
    # Desde Planta_Sur
    ('Planta_Sur', 'CD_Norte'): 90.0,       # Puebla → Monterrey
    ('Planta_Sur', 'CD_Centro'): 12.0,      # Puebla → CDMX
    ('Planta_Sur', 'CD_Bajio'): 75.0,       # Puebla → Guadalajara
    ('Planta_Sur', 'CD_Sur'): 35.0,         # Puebla → Veracruz
}

# COSTOS DE TRANSPORTE NIVEL 2: Centro Distribución → Ciudad Final
COSTOS_CD_CIUDAD = {
    # Desde CD_Norte
    ('CD_Norte', 'Toluca'): 88.0,
    ('CD_Norte', 'León'): 65.0,
    ('CD_Norte', 'San Luis Potosí'): 64.0,
    ('CD_Norte', 'Cancún'): 175.0,
    ('CD_Norte', 'Mérida'): 187.0,
    ('CD_Norte', 'Veracruz'): 116.0,
    
    # Desde CD_Centro
    ('CD_Centro', 'Toluca'): 7.0,
    ('CD_Centro', 'León'): 42.0,
    ('CD_Centro', 'San Luis Potosí'): 51.0,
    ('CD_Centro', 'Cancún'): 161.0,
    ('CD_Centro', 'Mérida'): 156.0,
    ('CD_Centro', 'Veracruz'): 72.0,
    
    # Desde CD_Bajio
    ('CD_Bajio', 'Toluca'): 60.0,
    ('CD_Bajio', 'León'): 18.0,
    ('CD_Bajio', 'San Luis Potosí'): 32.0,
    ('CD_Bajio', 'Cancún'): 206.0,
    ('CD_Bajio', 'Mérida'): 215.0,
    ('CD_Bajio', 'Veracruz'): 120.0,
    
    # Desde CD_Sur
    ('CD_Sur', 'Toluca'): 75.0,
    ('CD_Sur', 'León'): 95.0,
    ('CD_Sur', 'San Luis Potosí'): 85.0,
    ('CD_Sur', 'Cancún'): 145.0,
    ('CD_Sur', 'Mérida'): 140.0,
    ('CD_Sur', 'Veracruz'): 15.0,
}


# ============================================================================
# SOLVER DE OPTIMIZACIÓN MULTI-NIVEL
# ============================================================================

def resolver_red_multinivel(plantas, cds, ciudades, costos_p_cd, costos_cd_c,
                           incluir_costos_fijos=True, verbose=True):
    """
    Resuelve problema de transporte de 2 niveles con centros intermedios.
    
    Args:
        plantas (dict): Diccionario de plantas con capacidades
        cds (dict): Diccionario de centros de distribución
        ciudades (dict): Diccionario de ciudades con demandas
        costos_p_cd (dict): Costos de transporte planta→CD
        costos_cd_c (dict): Costos de transporte CD→ciudad
        incluir_costos_fijos (bool): Si incluir costos operacionales
        verbose (bool): Imprimir información detallada
        
    Returns:
        dict: Resultados con status, costo, flujos y análisis
    """
    if verbose:
        print("="*70)
        print("RESOLVIENDO MODELO DE RED MULTI-NIVEL")
        print("="*70)
    
    # Crear problema
    prob = LpProblem("Amazon_MultiNivel_México", LpMinimize)
    
    # ========================================================================
    # VARIABLES DE DECISIÓN
    # ========================================================================
    
    # Nivel 1: x[i,j] = cantidad transportada de planta i a CD j
    rutas_p_cd = [(p, cd) for p in plantas.keys() for cd in cds.keys()]
    x = LpVariable.dicts("flujo_planta_cd", rutas_p_cd, lowBound=0, cat="Integer")
    
    # Nivel 2: y[j,k] = cantidad transportada de CD j a ciudad k
    rutas_cd_c = [(cd, c) for cd in cds.keys() for c in ciudades.keys()]
    y = LpVariable.dicts("flujo_cd_ciudad", rutas_cd_c, lowBound=0, cat="Integer")
    
    # Variables binarias: z[j] = 1 si CD j está activo
    z = LpVariable.dicts("cd_activo", cds.keys(), cat="Binary")
    
    # ========================================================================
    # FUNCIÓN OBJETIVO: Minimizar Costo Total
    # ========================================================================
    
    # Costos de transporte nivel 1 (planta → CD)
    costo_transporte_1 = lpSum([
        costos_p_cd[(p, cd)] * x[(p, cd)] 
        for (p, cd) in rutas_p_cd
    ])
    
    # Costos de transporte nivel 2 (CD → ciudad)
    costo_transporte_2 = lpSum([
        costos_cd_c[(cd, c)] * y[(cd, c)] 
        for (cd, c) in rutas_cd_c
    ])
    
    # Costos de manejo en CDs
    costo_manejo_cd = lpSum([
        cds[cd]['costo_manejo'] * lpSum([x[(p, cd)] for p in plantas.keys()])
        for cd in cds.keys()
    ])
    
    if incluir_costos_fijos:
        # Costo fijo de mantener CD activo
        COSTO_FIJO_CD = 10000  # pesos por período
        costo_fijo = lpSum([COSTO_FIJO_CD * z[cd] for cd in cds.keys()])
        
        prob += costo_transporte_1 + costo_transporte_2 + costo_manejo_cd + costo_fijo
    else:
        prob += costo_transporte_1 + costo_transporte_2 + costo_manejo_cd
    
    # ========================================================================
    # RESTRICCIONES
    # ========================================================================
    
    # 1. CAPACIDAD DE PLANTAS (no exceder producción máxima)
    for p in plantas.keys():
        prob += lpSum([x[(p, cd)] for cd in cds.keys()]) <= plantas[p]['capacidad'], \
                f"Cap_Planta_{p}"
    
    # 2. BALANCE EN CENTROS DE DISTRIBUCIÓN
    for cd in cds.keys():
        # Lo que entra debe ser igual a lo que sale
        entrada = lpSum([x[(p, cd)] for p in plantas.keys()])
        salida = lpSum([y[(cd, c)] for c in ciudades.keys()])
        
        prob += salida <= entrada, f"Balance_Entrada_{cd}"
        prob += entrada <= cds[cd]['capacidad'], f"Cap_CD_{cd}"
        
        # Si el CD no está activo, no puede haber flujo
        M = cds[cd]['capacidad']  # Big M
        prob += entrada <= M * z[cd], f"Activacion_{cd}"
    
    # 3. SATISFACER DEMANDA DE CIUDADES
    for c in ciudades.keys():
        prob += lpSum([y[(cd, c)] for cd in cds.keys()]) >= ciudades[c], \
                f"Demanda_{c}"
    
    # ========================================================================
    # RESOLVER
    # ========================================================================
    
    if verbose:
        print("\n🔄 Resolviendo modelo de optimización...")
    
    status = prob.solve(PULP_CBC_CMD(msg=0))
    
    if LpStatus[prob.status] != 'Optimal':
        raise ValueError(f"❌ Solución no óptima: {LpStatus[prob.status]}")
    
    if verbose:
        print(f"✅ Solución óptima encontrada!")
        print(f"   Status: {LpStatus[prob.status]}")
        print(f"   Costo Total: ${value(prob.objective):,.2f} MXN")
    
    # ========================================================================
    # EXTRAER RESULTADOS
    # ========================================================================
    
    flujos_p_cd = {
        (p, cd): int(x[(p, cd)].varValue)
        for (p, cd) in rutas_p_cd
        if x[(p, cd)].varValue and x[(p, cd)].varValue > 0.5
    }
    
    flujos_cd_c = {
        (cd, c): int(y[(cd, c)].varValue)
        for (cd, c) in rutas_cd_c
        if y[(cd, c)].varValue and y[(cd, c)].varValue > 0.5
    }
    
    cds_activos = [cd for cd in cds.keys() if z[cd].varValue > 0.5]
    
    # Análisis adicional
    utilizacion_plantas = {
        p: sum(flujos_p_cd.get((p, cd), 0) for cd in cds.keys()) / plantas[p]['capacidad']
        for p in plantas.keys()
    }
    
    utilizacion_cds = {
        cd: sum(flujos_cd_c.get((cd, c), 0) for c in ciudades.keys()) / cds[cd]['capacidad']
        for cd in cds_activos
    }
    
    return {
        'status': LpStatus[prob.status],
        'costo_total': value(prob.objective),
        'flujos_planta_cd': flujos_p_cd,
        'flujos_cd_ciudad': flujos_cd_c,
        'cds_activos': cds_activos,
        'utilizacion_plantas': utilizacion_plantas,
        'utilizacion_cds': utilizacion_cds,
    }


# ============================================================================
# VISUALIZACIÓN
# ============================================================================

def visualizar_red_multinivel(resultado, plantas, cds, ciudades, filename='red_multinivel.png'):
    """
    Visualiza la red multi-nivel con NetworkX y Matplotlib.
    """
    fig, ax = plt.subplots(figsize=(18, 12))
    G = nx.DiGraph()
    
    # ========================================================================
    # CREAR NODOS Y POSICIONES
    # ========================================================================
    
    pos = {}
    
    # Columna 1: Plantas (izquierda, x=0)
    n_plantas = len(plantas)
    for i, planta in enumerate(plantas.keys()):
        y_pos = 1 - (i + 1) / (n_plantas + 1)
        pos[planta] = (0, y_pos)
        G.add_node(planta, tipo='planta', 
                  capacidad=plantas[planta]['capacidad'])
    
    # Columna 2: CDs activos (centro, x=0.5)
    cds_activos = resultado['cds_activos']
    n_cds = len(cds_activos)
    for i, cd in enumerate(cds_activos):
        y_pos = 1 - (i + 1) / (n_cds + 1)
        pos[cd] = (0.5, y_pos)
        G.add_node(cd, tipo='cd',
                  capacidad=cds[cd]['capacidad'])
    
    # Columna 3: Ciudades (derecha, x=1.0)
    n_ciudades = len(ciudades)
    for i, ciudad in enumerate(ciudades.keys()):
        y_pos = 1 - (i + 1) / (n_ciudades + 1)
        pos[ciudad] = (1.0, y_pos)
        G.add_node(ciudad, tipo='ciudad',
                  demanda=ciudades[ciudad])
    
    # ========================================================================
    # AGREGAR ARCOS
    # ========================================================================
    
    # Nivel 1: Planta → CD
    max_flujo_1 = max(resultado['flujos_planta_cd'].values()) if resultado['flujos_planta_cd'] else 1
    for (p, cd), flujo in resultado['flujos_planta_cd'].items():
        ancho = 1 + 5 * (flujo / max_flujo_1)  # Width proporcional al flujo
        G.add_edge(p, cd, weight=flujo, nivel=1, ancho=ancho)
    
    # Nivel 2: CD → Ciudad
    max_flujo_2 = max(resultado['flujos_cd_ciudad'].values()) if resultado['flujos_cd_ciudad'] else 1
    for (cd, c), flujo in resultado['flujos_cd_ciudad'].items():
        ancho = 1 + 5 * (flujo / max_flujo_2)
        G.add_edge(cd, c, weight=flujo, nivel=2, ancho=ancho)
    
    # ========================================================================
    # DIBUJAR NODOS
    # ========================================================================
    
    # Plantas (cuadrados azules)
    plantas_nodes = [n for n in G.nodes() if G.nodes[n]['tipo'] == 'planta']
    nx.draw_networkx_nodes(G, pos, nodelist=plantas_nodes,
                          node_color='#3498db', node_size=4000,
                          node_shape='s', ax=ax, 
                          edgecolors='black', linewidths=2)
    
    # CDs (círculos verdes)
    cd_nodes = [n for n in G.nodes() if G.nodes[n]['tipo'] == 'cd']
    nx.draw_networkx_nodes(G, pos, nodelist=cd_nodes,
                          node_color='#2ecc71', node_size=3500,
                          node_shape='o', ax=ax,
                          edgecolors='black', linewidths=2)
    
    # Ciudades (triángulos rojos)
    ciudad_nodes = [n for n in G.nodes() if G.nodes[n]['tipo'] == 'ciudad']
    nx.draw_networkx_nodes(G, pos, nodelist=ciudad_nodes,
                          node_color='#e74c3c', node_size=2500,
                          node_shape='v', ax=ax,
                          edgecolors='black', linewidths=2)
    
    # ========================================================================
    # DIBUJAR ARCOS
    # ========================================================================
    
    # Nivel 1: azul
    edges_nivel1 = [(u, v) for u, v, d in G.edges(data=True) if d['nivel'] == 1]
    anchos_1 = [G[u][v]['ancho'] for u, v in edges_nivel1]
    nx.draw_networkx_edges(G, pos, edgelist=edges_nivel1,
                          edge_color='#3498db', width=anchos_1, alpha=0.7,
                          arrows=True, arrowsize=25, ax=ax,
                          arrowstyle='->', connectionstyle='arc3,rad=0.1')
    
    # Nivel 2: verde
    edges_nivel2 = [(u, v) for u, v, d in G.edges(data=True) if d['nivel'] == 2]
    anchos_2 = [G[u][v]['ancho'] for u, v in edges_nivel2]
    nx.draw_networkx_edges(G, pos, edgelist=edges_nivel2,
                          edge_color='#2ecc71', width=anchos_2, alpha=0.7,
                          arrows=True, arrowsize=25, ax=ax,
                          arrowstyle='->', connectionstyle='arc3,rad=0.1')
    
    # ========================================================================
    # ETIQUETAS
    # ========================================================================
    
    # Nombres de nodos
    labels = {}
    for node in G.nodes():
        if G.nodes[node]['tipo'] == 'planta':
            nombre = node.replace('Planta_', '')
            util = resultado['utilizacion_plantas'][node]
            labels[node] = f"{nombre}\n{util:.0%}"
        elif G.nodes[node]['tipo'] == 'cd':
            nombre = node.replace('CD_', '')
            util = resultado['utilizacion_cds'][node]
            labels[node] = f"{nombre}\n{util:.0%}"
        else:
            labels[node] = node
    
    nx.draw_networkx_labels(G, pos, labels, font_size=11, 
                           font_weight='bold', ax=ax)
    
    # Etiquetas de flujo
    edge_labels = {}
    for u, v in G.edges():
        flujo = G[u][v]['weight']
        if flujo > 1000:
            edge_labels[(u, v)] = f"{flujo/1000:.1f}k"
        else:
            edge_labels[(u, v)] = f"{flujo}"
    
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=9, ax=ax)
    
    # ========================================================================
    # TÍTULO Y LEYENDA
    # ========================================================================
    
    titulo = (
        f"Red de Distribución Multi-Nivel Amazon México\n"
        f"Costo Total: ${resultado['costo_total']:,.2f} MXN | "
        f"CDs Activos: {len(resultado['cds_activos'])}/{len(cds)}"
    )
    ax.set_title(titulo, fontsize=16, fontweight='bold', pad=20)
    
    # Leyenda personalizada
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D
    
    legend_elements = [
        Patch(facecolor='#3498db', edgecolor='black', label='Plantas'),
        Patch(facecolor='#2ecc71', edgecolor='black', label='Centros Distribución'),
        Patch(facecolor='#e74c3c', edgecolor='black', label='Ciudades'),
        Line2D([0], [0], color='#3498db', lw=3, label='Flujo Planta→CD'),
        Line2D([0], [0], color='#2ecc71', lw=3, label='Flujo CD→Ciudad'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=11)
    
    ax.axis('off')
    plt.tight_layout()
    
    # Guardar
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"\n✅ Visualización guardada: {filename}")
    
    return fig


# ============================================================================
# ANÁLISIS Y REPORTES
# ============================================================================

def generar_reporte(resultado, plantas, cds, ciudades):
    """Genera reporte detallado de resultados."""
    
    print("\n" + "="*70)
    print("📊 REPORTE DE RESULTADOS - RED MULTI-NIVEL")
    print("="*70)
    
    print(f"\n💰 COSTO TOTAL: ${resultado['costo_total']:,.2f} MXN")
    
    print(f"\n🏭 CENTROS DE DISTRIBUCIÓN ACTIVOS ({len(resultado['cds_activos'])}/" \
          f"{len(cds)}):")
    for cd in resultado['cds_activos']:
        util = resultado['utilizacion_cds'][cd]
        print(f"   • {cd}: Utilización {util:.1%}")
    
    print(f"\n📦 UTILIZACIÓN DE PLANTAS:")
    for p, util in resultado['utilizacion_plantas'].items():
        produccion = sum(resultado['flujos_planta_cd'].get((p, cd), 0) 
                        for cd in cds.keys())
        print(f"   • {p}: {util:.1%} ({produccion:,} / {plantas[p]['capacidad']:,} unidades)")
    
    print(f"\n🚚 FLUJOS PRINCIPALES (Nivel 1: Planta → CD):")
    flujos_ordenados = sorted(resultado['flujos_planta_cd'].items(), 
                             key=lambda x: x[1], reverse=True)
    for (p, cd), flujo in flujos_ordenados[:5]:
        print(f"   • {p} → {cd}: {flujo:,} unidades")
    
    print(f"\n🏙️ FLUJOS PRINCIPALES (Nivel 2: CD → Ciudad):")
    flujos_ordenados = sorted(resultado['flujos_cd_ciudad'].items(),
                             key=lambda x: x[1], reverse=True)
    for (cd, c), flujo in flujos_ordenados[:5]:
        print(f"   • {cd} → {c}: {flujo:,} unidades")
    
    print("\n" + "="*70)


# ============================================================================
# EJECUCIÓN PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("\n🚀 INICIANDO ANÁLISIS DE RED MULTI-NIVEL")
    
    # Resolver
    resultado = resolver_red_multinivel(
        PLANTAS,
        CENTROS_DISTRIBUCION,
        CIUDADES_DEMANDA,
        COSTOS_PLANTA_CD,
        COSTOS_CD_CIUDAD,
        incluir_costos_fijos=True,
        verbose=True
    )
    
    # Generar reporte
    generar_reporte(resultado, PLANTAS, CENTROS_DISTRIBUCION, CIUDADES_DEMANDA)
    
    # Visualizar
    fig = visualizar_red_multinivel(resultado, PLANTAS, CENTROS_DISTRIBUCION,
                                    CIUDADES_DEMANDA, 'red_multinivel.png')
    
    print("\n✅ ANÁLISIS COMPLETADO")
    print("📁 Archivos generados:")
    print("   • red_multinivel.png - Visualización de la red")
