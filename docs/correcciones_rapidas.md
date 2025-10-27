# 🔧 CORRECCIONES RÁPIDAS - Amazon Logistics Notebook

## ✅ ERROR CRÍTICO YA CORREGIDO

### Error: TypeError en make_pdf_infographic

**Ubicación:** Celda #15 (función `make_pdf_infographic`)

**❌ Código anterior (con error):**
```python
# INCORRECTO - NO USAR
qr_bytes = io.BytesIO()
qr_img.save(qr_bytes, format="PNG")
qr_bytes.seek(0)
c.drawImage(Image.open(qr_bytes), 50, 50, width=300, height=300, mask='auto')
```

**✅ Código corregido:**
```python
# CORRECTO - YA IMPLEMENTADO EN v3.2
import tempfile
import os

qr_img = generate_qr(qr_text)
with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_qr_file:
    qr_img.save(tmp_qr_file.name, format="PNG")
    tmp_qr_path = tmp_qr_file.name

c.drawImage(tmp_qr_path, 50, 50, width=300, height=300, mask='auto')

# Limpieza del archivo temporal
os.remove(tmp_qr_path)
```

---

## ⚠️ MEJORAS RECOMENDADAS (PRIORIDAD ALTA)

### 1. Validar `student_id` antes de usar

**Ubicación:** Celda #17 (celda principal de ejecución)

**❌ Código actual:**
```python
student_id = 4021  # Definido en alguna celda anterior
qr_reference = "Amazon Logistics Simulation | ID=" + str(student_id)
```

**✅ Código mejorado:**
```python
# Opción 1: Definir con valor por defecto
if 'student_id' not in globals():
    student_id = 4021  # Valor por defecto
    print(f"⚠️ Usando student_id por defecto: {student_id}")

# Opción 2: Validar que existe
try:
    student_id
except NameError:
    raise ValueError("❌ Error: Debe definir 'student_id' antes de ejecutar esta celda")

# Validar que es un entero válido
if not isinstance(student_id, int) or student_id < 0:
    raise ValueError(f"❌ Error: student_id debe ser un entero positivo, recibido: {student_id}")

qr_reference = f"Amazon Logistics Simulation | ID={student_id}"
```

---

### 2. Validar directorio de resultados

**Ubicación:** Celda #17

**❌ Código actual:**
```python
os.makedirs("results", exist_ok=True)
```

**✅ Código mejorado:**
```python
from pathlib import Path

def crear_directorio_resultados(directorio="results"):
    """Crea directorio validando permisos."""
    ruta = Path(directorio)
    
    try:
        ruta.mkdir(exist_ok=True)
        
        # Verificar que es escribible
        test_file = ruta / ".test"
        test_file.touch()
        test_file.unlink()
        
        print(f"✅ Directorio '{directorio}' listo")
        return ruta
        
    except PermissionError:
        print(f"❌ Error: No hay permisos para escribir en '{directorio}'")
        raise

# Uso
crear_directorio_resultados("results")
```

---

### 3. Mejorar manejo de errores en solver

**Ubicación:** Celda #15 (función `resolver_problema`)

**❌ Código actual:**
```python
prob.solve(PULP_CBC_CMD(msg=0))

asign = {(i,j):int(x[(i,j)].varValue) for (i,j) in rutas if x[(i,j)].varValue and x[(i,j)].varValue>0}
return {
    "status": LpStatus[prob.status],
    "cost": value(prob.objective),
    "assign": asign,
}
```

**✅ Código mejorado:**
```python
from pulp import LpStatus

# Resolver
status = prob.solve(PULP_CBC_CMD(msg=0))

# VALIDAR RESULTADO
if LpStatus[prob.status] != 'Optimal':
    print(f"⚠️ Advertencia: Solución {LpStatus[prob.status]}")
    
    if LpStatus[prob.status] == 'Infeasible':
        raise ValueError(
            "❌ El problema no tiene solución factible.\n"
            "Posibles causas:\n"
            "  - Oferta total < Demanda total\n"
            "  - Restricciones incompatibles"
        )
    elif LpStatus[prob.status] == 'Unbounded':
        raise ValueError("❌ El problema no está acotado")

# Extraer asignaciones solo si hay solución
asign = {}
if LpStatus[prob.status] in ['Optimal', 'Feasible']:
    asign = {
        (i,j): int(x[(i,j)].varValue) 
        for (i,j) in rutas 
        if x[(i,j)].varValue and x[(i,j)].varValue > 0
    }

return {
    "status": LpStatus[prob.status],
    "cost": value(prob.objective) if prob.objective else 0,
    "assign": asign,
}
```

---

### 4. Agregar docstrings básicos

**Para TODAS las funciones, agregar:**

```python
def funcion_ejemplo(parametro1, parametro2):
    """
    Descripción breve de lo que hace la función.
    
    Args:
        parametro1: Descripción del parámetro 1
        parametro2: Descripción del parámetro 2
        
    Returns:
        Descripción de lo que retorna
        
    Example:
        >>> resultado = funcion_ejemplo(1, 2)
        >>> print(resultado)
        3
    """
    # código aquí
    pass
```

**Ejemplo aplicado a `generar_datos_estudiante`:**

```python
def generar_datos_estudiante(student_id):
    """
    Genera datos personalizados de logística para un estudiante.
    
    Los datos se generan de forma determinística basándose en el
    student_id, permitiendo reproducibilidad.
    
    Args:
        student_id (int): Identificador único del estudiante
        
    Returns:
        dict: Diccionario con claves:
            - 'id': ID del estudiante
            - 'demanda': Dict {destino: cantidad}
            - 'oferta': Dict {origen: cantidad}
            - 'costos': Dict {(origen, destino): costo}
            
    Example:
        >>> datos = generar_datos_estudiante(4021)
        >>> print(datos['id'])
        4021
    """
    # resto del código...
```

---

## 🚀 MEJORAS OPCIONALES (PRIORIDAD MEDIA)

### 5. Agregar logging básico

**Agregar al inicio del notebook:**

```python
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Uso en funciones
def resolver_problema(datos, multiplicador_costo=1.0, cerrar_veracruz=False):
    logger.info(f"Resolviendo con multiplicador={multiplicador_costo}")
    
    # ... código ...
    
    logger.info(f"Solución: {LpStatus[prob.status]}, Costo: ${value(prob.objective):,.2f}")
    return resultado
```

---

### 6. Separar imports por tipo

**❌ Actual:**
```python
import os, io, math, base64
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from PIL import Image
```

**✅ Mejorado (siguiendo PEP 8):**
```python
# Standard library
import base64
import io
import math
import os

# Third-party
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from PIL import Image
import qrcode
from pulp import *

# Local/project specific
# (si hubiera módulos propios)
```

---

### 7. Usar f-strings consistentemente

**❌ Evitar:**
```python
qr_reference = "Amazon Logistics Simulation | ID=" + str(student_id)
```

**✅ Usar:**
```python
qr_reference = f"Amazon Logistics Simulation | ID={student_id}"
```

---

## 📝 CHECKLIST DE IMPLEMENTACIÓN

### Prioridad ALTA (hacer ahora)
- [x] ✅ Corregir error de `make_pdf_infographic` (YA HECHO)
- [ ] ⬜ Agregar validación de `student_id`
- [ ] ⬜ Validar creación de directorio `results`
- [ ] ⬜ Mejorar manejo de errores en solver
- [ ] ⬜ Agregar docstrings a funciones principales

### Prioridad MEDIA (hacer pronto)
- [ ] ⬜ Implementar logging básico
- [ ] ⬜ Organizar imports según PEP 8
- [ ] ⬜ Usar f-strings consistentemente

### Prioridad BAJA (opcional)
- [ ] ⬜ Agregar type hints
- [ ] ⬜ Crear tests unitarios
- [ ] ⬜ Exportar resultados a Excel

---

## 🧪 CÓMO PROBAR LAS CORRECCIONES

### Test 1: Verificar que no hay NameError
```python
# Ejecutar esta celda ANTES de la celda principal
student_id = 4021
print(f"✅ student_id definido: {student_id}")
```

### Test 2: Verificar directorio de resultados
```python
from pathlib import Path

ruta = Path("results")
if ruta.exists() and ruta.is_dir():
    print("✅ Directorio 'results' existe")
    
    # Probar escritura
    test_file = ruta / ".test"
    try:
        test_file.touch()
        test_file.unlink()
        print("✅ Directorio es escribible")
    except:
        print("❌ No se puede escribir en el directorio")
else:
    print("❌ Directorio 'results' no existe")
```

### Test 3: Verificar solver
```python
datos = generar_datos_estudiante(4021)
resultado = resolver_problema(datos)

print(f"Status: {resultado['status']}")
print(f"Costo: ${resultado['cost']:,.2f}")
print(f"Asignaciones: {len(resultado['assign'])}")

assert resultado['status'] == 'Optimal', "❌ Solución no óptima"
assert resultado['cost'] > 0, "❌ Costo debe ser positivo"
assert len(resultado['assign']) > 0, "❌ Debe haber asignaciones"

print("✅ Todas las validaciones pasaron")
```

---

## 💡 TIPS GENERALES

1. **Ejecutar celdas en orden**: Siempre ejecutar de arriba hacia abajo
2. **Restart & Run All**: Probar con "Restart Kernel and Run All Cells"
3. **Guardar frecuentemente**: Ctrl+S después de cada cambio importante
4. **Comentar cambios**: Agregar comentarios explicando modificaciones
5. **Versionar**: Si usas Git, hacer commit después de cada corrección

---

## 🔗 RECURSOS ADICIONALES

- [PuLP Documentation](https://coin-or.github.io/pulp/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Reportlab User Guide](https://www.reportlab.com/docs/reportlab-userguide.pdf)
- [Python Logging Tutorial](https://docs.python.org/3/howto/logging.html)

---

**Última actualización:** 26 de octubre de 2025
**Versión del documento:** 1.0
