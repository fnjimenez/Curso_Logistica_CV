# 🚨 PROBLEMA IDENTIFICADO: Modelo de Red Simplificado

## 🔍 DIAGNÓSTICO

### Problema Encontrado
Tu notebook está usando un **modelo de transporte de 1 nivel** (directo origen→destino), cuando lo que necesitas es un **modelo de red multi-nivel** con centros de distribución intermedios.

### Red Actual (INCORRECTA para Amazon real)
```
ORIGENES (Oferta)          DESTINOS (Demanda)
├─ CDMX ──────────────────→ Toluca
├─ Monterrey ─────────────→ León
├─ Guadalajara ───────────→ San Luis Potosí
├─ Querétaro ─────────────→ Cancún
├─ Puebla ────────────────→ Mérida
└─ Tijuana ───────────────→ Veracruz

Problema: Envíos DIRECTOS sin centros intermedios
```

### Red que Deberías Tener (CORRECTA para Amazon)
```
PLANTAS/FÁBRICAS → CENTROS DE DISTRIBUCIÓN → CIUDADES FINALES
    (Oferta)            (Intermedios)           (Demanda)

Ejemplo:
CDMX (planta) → CD_Querétaro → Toluca
              → CD_Guadalajara → León
Monterrey     → CD_Bajío       → San Luis Potosí
```

---

## 🎯 CAUSAS DEL PROBLEMA

### 1. Estructura del Modelo
**Código actual:**
```python
ORIGENES = ['CDMX', 'Monterrey', 'Guadalajara', 'Querétaro', 'Puebla', 'Tijuana']
DESTINOS = ['Toluca', 'León', 'San Luis Potosí', 'Cancún', 'Mérida', 'Veracruz']

# Rutas directas (1 nivel)
rutas = [(i,j) for i in ORIGENES for j in DESTINOS]
```

**Problema:** No hay nodos intermedios definidos.

### 2. Visualización
El código dibuja conexiones directas:
```python
def draw_flow_network(assign, ...):
    # Dibuja arcos directos de origen a destino
    G.add_edge(origin, dest, weight=qty)
```

---

## ✅ SOLUCIONES PROPUESTAS

### Opción 1: Modelo de 2 Niveles (Recomendado para clase)
```
Nivel 1: Plantas → Centros Distribución Regionales
Nivel 2: CD Regionales → Ciudades Finales
```

### Opción 2: Modelo de 3 Niveles (Más realista Amazon)
```
Nivel 1: Centros Producción → CD Nacionales
Nivel 2: CD Nacionales → CD Regionales  
Nivel 3: CD Regionales → Última Milla (ciudades)
```

### Opción 3: Mantener Modelo Actual pero Renombrar
Si el objetivo pedagógico es solo optimización de transporte:
- Renombrar "ORIGENES" → "ALMACENES/BODEGAS"
- Renombrar "DESTINOS" → "TIENDAS/CLIENTES"
- Clarificar que es un modelo simplificado

---

## 💻 IMPLEMENTACIÓN: Modelo de 2 Niveles

### Paso 1: Definir Estructura de Red

```python
# NIVEL 1: Plantas/Fábricas (Producción)
PLANTAS = {
    'Planta_Norte': {'capacidad': 80000, 'ubicacion': 'Monterrey'},
    'Planta_Centro': {'capacidad': 100000, 'ubicacion': 'CDMX'},
    'Planta_Bajío': {'capacidad': 60000, 'ubicacion': 'Querétaro'},
}

# NIVEL 2: Centros de Distribución Regionales (Intermedios)
CENTROS_DISTRIBUCION = {
    'CD_Norte': {'capacidad': 50000, 'ubicacion': 'Monterrey'},
    'CD_Centro': {'capacidad': 70000, 'ubicacion': 'CDMX'},
    'CD_Bajío': {'capacidad': 45000, 'ubicacion': 'Guadalajara'},
    'CD_Sur': {'capacidad': 35000, 'ubicacion': 'Puebla'},
}

# NIVEL 3: Ciudades Finales (Demanda)
CIUDADES_DEMANDA = {
    'Toluca': 27000,
    'León': 21000,
    'San Luis Potosí': 17000,
    'Cancún': 17000,
    'Mérida': 18000,
    'Veracruz': 20000,
}

# COSTOS NIVEL 1: Planta → CD
COSTOS_PLANTA_CD = {
    ('Planta_Norte', 'CD_Norte'): 5.0,
    ('Planta_Norte', 'CD_Centro'): 45.0,
    ('Planta_Norte', 'CD_Bajío'): 40.0,
    ('Planta_Centro', 'CD_Norte'): 45.0,
    ('Planta_Centro', 'CD_Centro'): 3.0,
    ('Planta_Centro', 'CD_Bajío'): 35.0,
    ('Planta_Centro', 'CD_Sur'): 15.0,
    # ... más rutas
}

# COSTOS NIVEL 2: CD → Ciudad Final
COSTOS_CD_CIUDAD = {
    ('CD_Centro', 'Toluca'): 7.0,
    ('CD_Centro', 'León'): 42.0,
    ('CD_Bajío', 'León'): 20.0,
    ('CD_Bajío', 'San Luis Potosí'): 25.0,
    # ... más rutas
}
```

### Paso 2: Modelo de Optimización Multi-Nivel

```python
from pulp import *

def resolver_red_multinivel(plantas, cds, ciudades, costos_p_cd, costos_cd_c):
    """
    Resuelve problema de transporte de 2 niveles.
    
    Niveles:
    1. Plantas → Centros Distribución
    2. Centros Distribución → Ciudades Finales
    """
    
    prob = LpProblem("Amazon_MultiNivel", LpMinimize)
    
    # VARIABLES DE DECISIÓN
    # x[i,j] = flujo de planta i a CD j
    rutas_p_cd = [(p, cd) for p in plantas.keys() for cd in cds.keys()]
    x = LpVariable.dicts("flujo_planta_cd", rutas_p_cd, lowBound=0, cat="Integer")
    
    # y[j,k] = flujo de CD j a ciudad k
    rutas_cd_c = [(cd, c) for cd in cds.keys() for c in ciudades.keys()]
    y = LpVariable.dicts("flujo_cd_ciudad", rutas_cd_c, lowBound=0, cat="Integer")
    
    # FUNCIÓN OBJETIVO: Minimizar costo total
    prob += (
        lpSum([costos_p_cd[(p, cd)] * x[(p, cd)] for (p, cd) in rutas_p_cd]) +
        lpSum([costos_cd_c[(cd, c)] * y[(cd, c)] for (cd, c) in rutas_cd_c])
    )
    
    # RESTRICCIONES
    
    # 1. Capacidad de Plantas (oferta máxima)
    for p in plantas.keys():
        prob += lpSum([x[(p, cd)] for cd in cds.keys()]) <= plantas[p]['capacidad']
    
    # 2. Capacidad de CDs (lo que entra = lo que sale)
    for cd in cds.keys():
        # Lo que entra al CD desde plantas
        entrada = lpSum([x[(p, cd)] for p in plantas.keys()])
        # Lo que sale del CD hacia ciudades
        salida = lpSum([y[(cd, c)] for c in ciudades.keys()])
        
        prob += salida <= entrada  # No puede salir más de lo que entra
        prob += entrada <= cds[cd]['capacidad']  # Respeta capacidad del CD
    
    # 3. Demanda de Ciudades (debe satisfacerse)
    for c in ciudades.keys():
        prob += lpSum([y[(cd, c)] for cd in cds.keys()]) >= ciudades[c]
    
    # RESOLVER
    prob.solve(PULP_CBC_CMD(msg=0))
    
    if LpStatus[prob.status] != 'Optimal':
        raise ValueError(f"Solución no óptima: {LpStatus[prob.status]}")
    
    # EXTRAER RESULTADOS
    flujos_p_cd = {
        (p, cd): int(x[(p, cd)].varValue)
        for (p, cd) in rutas_p_cd
        if x[(p, cd)].varValue and x[(p, cd)].varValue > 0
    }
    
    flujos_cd_c = {
        (cd, c): int(y[(cd, c)].varValue)
        for (cd, c) in rutas_cd_c
        if y[(cd, c)].varValue and y[(cd, c)].varValue > 0
    }
    
    return {
        'status': LpStatus[prob.status],
        'costo_total': value(prob.objective),
        'flujos_planta_cd': flujos_p_cd,
        'flujos_cd_ciudad': flujos_cd_c,
    }
```

### Paso 3: Visualización Multi-Nivel

```python
import networkx as nx
import matplotlib.pyplot as plt

def visualizar_red_multinivel(resultado, plantas, cds, ciudades):
    """
    Visualiza red de 2 niveles con posiciones estratégicas.
    """
    fig, ax = plt.subplots(figsize=(16, 12))
    G = nx.DiGraph()
    
    # POSICIONES DE NODOS (3 columnas: plantas, CDs, ciudades)
    pos = {}
    
    # Columna 1: Plantas (izquierda)
    y_spacing = 1.0 / (len(plantas) + 1)
    for i, planta in enumerate(plantas.keys()):
        pos[planta] = (0, 1 - (i + 1) * y_spacing)
        G.add_node(planta, tipo='planta')
    
    # Columna 2: CDs (centro)
    y_spacing = 1.0 / (len(cds) + 1)
    for i, cd in enumerate(cds.keys()):
        pos[cd] = (0.5, 1 - (i + 1) * y_spacing)
        G.add_node(cd, tipo='cd')
    
    # Columna 3: Ciudades (derecha)
    y_spacing = 1.0 / (len(ciudades) + 1)
    for i, ciudad in enumerate(ciudades.keys()):
        pos[ciudad] = (1.0, 1 - (i + 1) * y_spacing)
        G.add_node(ciudad, tipo='ciudad')
    
    # AGREGAR ARCOS NIVEL 1: Planta → CD
    for (p, cd), flujo in resultado['flujos_planta_cd'].items():
        G.add_edge(p, cd, weight=flujo, nivel=1)
    
    # AGREGAR ARCOS NIVEL 2: CD → Ciudad
    for (cd, c), flujo in resultado['flujos_cd_ciudad'].items():
        G.add_edge(cd, c, weight=flujo, nivel=2)
    
    # DIBUJAR NODOS
    # Plantas (azul)
    plantas_nodes = [n for n in G.nodes() if G.nodes[n]['tipo'] == 'planta']
    nx.draw_networkx_nodes(G, pos, nodelist=plantas_nodes, 
                          node_color='skyblue', node_size=3000, 
                          node_shape='s', ax=ax, label='Plantas')
    
    # CDs (verde)
    cd_nodes = [n for n in G.nodes() if G.nodes[n]['tipo'] == 'cd']
    nx.draw_networkx_nodes(G, pos, nodelist=cd_nodes,
                          node_color='lightgreen', node_size=2500,
                          node_shape='o', ax=ax, label='Centros Distribución')
    
    # Ciudades (rojo)
    ciudad_nodes = [n for n in G.nodes() if G.nodes[n]['tipo'] == 'ciudad']
    nx.draw_networkx_nodes(G, pos, nodelist=ciudad_nodes,
                          node_color='lightcoral', node_size=2000,
                          node_shape='v', ax=ax, label='Ciudades')
    
    # DIBUJAR ARCOS
    # Nivel 1: Planta → CD (azul)
    edges_nivel1 = [(u, v) for u, v, d in G.edges(data=True) if d['nivel'] == 1]
    nx.draw_networkx_edges(G, pos, edgelist=edges_nivel1,
                          edge_color='blue', width=2, alpha=0.6,
                          arrows=True, arrowsize=20, ax=ax)
    
    # Nivel 2: CD → Ciudad (verde)
    edges_nivel2 = [(u, v) for u, v, d in G.edges(data=True) if d['nivel'] == 2]
    nx.draw_networkx_edges(G, pos, edgelist=edges_nivel2,
                          edge_color='green', width=2, alpha=0.6,
                          arrows=True, arrowsize=20, ax=ax)
    
    # ETIQUETAS
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', ax=ax)
    
    # Etiquetas de flujo en arcos
    edge_labels = {(u, v): f"{G[u][v]['weight']:,}" for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8, ax=ax)
    
    ax.set_title(f"Red Multi-Nivel Amazon México\nCosto Total: ${resultado['costo_total']:,.2f}",
                fontsize=16, fontweight='bold')
    ax.legend(loc='upper left')
    ax.axis('off')
    
    plt.tight_layout()
    return fig

# EJEMPLO DE USO
resultado = resolver_red_multinivel(PLANTAS, CENTROS_DISTRIBUCION, 
                                    CIUDADES_DEMANDA, COSTOS_PLANTA_CD, 
                                    COSTOS_CD_CIUDAD)

fig = visualizar_red_multinivel(resultado, PLANTAS, CENTROS_DISTRIBUCION, 
                                 CIUDADES_DEMANDA)
plt.savefig('red_multinivel.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

## 🎓 EXPLICACIÓN PEDAGÓGICA

### ¿Por qué Amazon usa redes multi-nivel?

1. **Economías de Escala**
   - Consolida envíos grandes: Planta → CD
   - Distribuye localmente: CD → Cliente

2. **Optimización de Inventario**
   - Inventory pooling en CDs
   - Reduce stock de seguridad total

3. **Flexibilidad**
   - CDs pueden servir a múltiples ciudades
   - Reasignación dinámica de demanda

4. **Costos de Transporte**
   - Transporte masivo (planta→CD): bajo costo/unidad
   - Última milla (CD→ciudad): alto costo pero distancias cortas

### Comparación de Costos

**Modelo 1 Nivel (actual):**
```
Planta CDMX → Cancún: 1,000 unidades × $161/unidad = $161,000
```

**Modelo 2 Niveles (propuesto):**
```
Planta CDMX → CD_Sur: 1,000 unidades × $15/unidad = $15,000
CD_Sur → Cancún: 1,000 unidades × $100/unidad = $100,000
Total: $115,000 (AHORRO: $46,000 o 28%)
```

---

## 🔧 ACCIÓN REQUERIDA

### Opción A: Mantener Modelo Simple (Para Clase Introductoria)
1. Agregar nota aclaratoria en notebook:
   ```markdown
   **Nota:** Este es un modelo simplificado de transporte directo
   con fines pedagógicos. En realidad, Amazon usa redes multi-nivel
   con centros de distribución intermedios.
   ```

2. Renombrar conceptos:
   - ORIGENES → "Almacenes/Bodegas Principales"
   - DESTINOS → "Tiendas/Clientes Finales"

### Opción B: Implementar Modelo Multi-Nivel (Recomendado)
1. Usar el código proporcionado arriba
2. Crear nueva versión: `Amazon_Logistics_v4.0_MultiNivel.ipynb`
3. Mantener v3.2 como referencia del modelo simple

### Opción C: Híbrido (Lo Mejor de Ambos)
1. Notebook con 2 secciones:
   - Parte 1: Modelo simple (pedagógico)
   - Parte 2: Modelo multi-nivel (realista)
2. Permite comparar ambos enfoques

---

## 📊 COMPARACIÓN VISUAL

### Tu Visualización Actual
```
[Plantas] ────────────→ [Ciudades]
  (directo, 1 salto)
```

### Visualización Correcta Amazon
```
[Plantas] → [CD Regional] → [CD Local] → [Ciudades]
    (consolidación)   (distribución)   (última milla)
```

---

## 💡 RECOMENDACIÓN FINAL

Para tu caso educativo, sugiero **Opción C (Híbrido)**:

1. **Mantén el modelo actual** como "Parte 1: Modelo Básico"
2. **Agrega nueva sección** "Parte 2: Modelo Multi-Nivel Realista"
3. **Compara resultados** entre ambos modelos
4. **Explica diferencias** en costos y estructura

Esto te permite:
✅ Enseñar conceptos básicos primero (modelo simple)
✅ Mostrar aplicación real (modelo multi-nivel)
✅ Comparar y analizar diferencias
✅ Mantener rigor académico

---

¿Quieres que implemente el modelo multi-nivel completo para ti?
