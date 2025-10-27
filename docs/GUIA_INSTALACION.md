# 📦 Guía de Instalación - Amazon Logistics Optimization

## 🎯 Prerequisitos

Antes de comenzar, asegúrate de tener instalado:

### 1. Python
- **Versión mínima**: Python 3.8
- **Recomendada**: Python 3.10 o superior

**Verificar instalación:**
```bash
python --version
# o
python3 --version
```

**Descargar Python:**
- Windows/Mac: https://www.python.org/downloads/
- Linux (Ubuntu/Debian): `sudo apt install python3 python3-pip`
- Linux (Fedora): `sudo dnf install python3 python3-pip`

### 2. pip (Gestor de paquetes)
**Verificar:**
```bash
pip --version
# o
pip3 --version
```

**Instalar pip (si no está instalado):**
```bash
python -m ensurepip --upgrade
```

### 3. Git
**Verificar:**
```bash
git --version
```

**Instalar Git:**
- Windows: https://git-scm.com/download/win
- Mac: `brew install git` (requiere Homebrew)
- Linux: `sudo apt install git` (Ubuntu/Debian)

---

## 🚀 Instalación Rápida

### Opción 1: Clonar desde GitHub (Recomendado)

```bash
# 1. Clonar el repositorio
git clone https://github.com/fnjimenez/Curso_Logistica_CV.git

# 2. Entrar al directorio
cd Curso_Logistica_CV

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Verificar instalación
python -c "import pulp, networkx, matplotlib; print('✅ Instalación exitosa')"
```

### Opción 2: Instalar como paquete

```bash
# Después de clonar
cd Curso_Logistica_CV
pip install -e .
```

### Opción 3: Solo descargar archivos

Si no tienes Git, descarga el ZIP:
1. Ve a: https://github.com/fnjimenez/Curso_Logistica_CV
2. Click en "Code" → "Download ZIP"
3. Descomprime el archivo
4. Abre terminal en la carpeta
5. Ejecuta: `pip install -r requirements.txt`

---

## 🌐 Entornos Virtuales (Recomendado)

Usar un entorno virtual mantiene las dependencias aisladas.

### Windows

```bash
# Crear entorno virtual
python -m venv venv

# Activar
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Mac/Linux

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Desactivar entorno virtual
```bash
deactivate
```

---

## 🐍 Instalación con Conda (Alternativa)

Si usas Anaconda o Miniconda:

```bash
# Crear entorno
conda create -n amazon_logistics python=3.10

# Activar
conda activate amazon_logistics

# Instalar dependencias
pip install -r requirements.txt

# O instalar con conda cuando sea posible
conda install numpy pandas matplotlib jupyter
pip install pulp networkx qrcode reportlab
```

---

## 📦 Dependencias Detalladas

### Obligatorias (Core)
```
pulp>=2.7.0              # Optimización lineal (5.2 MB)
networkx>=3.0            # Análisis de redes (2.1 MB)
matplotlib>=3.5.0        # Visualización (8.5 MB)
numpy>=1.21.0            # Cálculos numéricos (15 MB)
```

### Procesamiento
```
pandas>=1.3.0            # Análisis de datos (12 MB)
Pillow>=9.0.0            # Imágenes (3.2 MB)
qrcode>=7.3.1            # QR codes (35 KB)
reportlab>=3.6.0         # PDFs (2.8 MB)
```

### Desarrollo (Opcional)
```
jupyter>=1.0.0           # Notebooks interactivos
pytest>=7.0.0            # Testing
black>=22.0.0            # Formateo de código
```

**Espacio total aproximado**: ~100 MB

---

## ✅ Verificación de Instalación

### Test Rápido

```python
# Ejecuta este script para verificar todo
python -c """
import sys
print(f'Python: {sys.version}')

try:
    import pulp
    print('✅ PuLP instalado')
except ImportError:
    print('❌ PuLP NO instalado')

try:
    import networkx as nx
    print('✅ NetworkX instalado')
except ImportError:
    print('❌ NetworkX NO instalado')

try:
    import matplotlib.pyplot as plt
    print('✅ Matplotlib instalado')
except ImportError:
    print('❌ Matplotlib NO instalado')

try:
    import numpy as np
    print('✅ NumPy instalado')
except ImportError:
    print('❌ NumPy NO instalado')

print('\\n🎉 Verificación completada')
"""
```

### Test Completo

```bash
# Ejecutar tests del proyecto
pytest tests/ -v
```

---

## 🧪 Ejecutar Notebooks

### 1. Iniciar Jupyter

```bash
# En el directorio del proyecto
jupyter notebook
```

Se abrirá tu navegador con la interfaz de Jupyter.

### 2. Abrir notebook

Navega a: `notebooks/Amazon_Logistics_v4.0.ipynb`

### 3. Ejecutar celdas

- **Ejecutar celda**: `Shift + Enter`
- **Ejecutar todas**: Menu → Cell → Run All

---

## 🐛 Solución de Problemas

### Problema: "No module named 'pulp'"

**Solución:**
```bash
pip install pulp --upgrade
```

### Problema: Error con matplotlib en Mac

**Solución:**
```bash
# Reinstalar con backend correcto
pip uninstall matplotlib
pip install matplotlib
```

### Problema: "Permission denied" en Linux

**Solución:**
```bash
# Instalar para el usuario actual
pip install --user -r requirements.txt
```

### Problema: Solver CBC no encontrado

**Solución:**
```bash
# PuLP incluye CBC, pero si falla:
# Windows: descargar de https://github.com/coin-or/Cbc/releases
# Linux: sudo apt install coinor-cbc
# Mac: brew install cbc
```

### Problema: Jupyter no abre

**Solución:**
```bash
# Reinstalar Jupyter
pip uninstall jupyter
pip install jupyter

# O usar JupyterLab (más moderno)
pip install jupyterlab
jupyter lab
```

### Problema: Errores de encoding en Windows

**Solución:**
```python
# Agregar al inicio del notebook
import sys
sys.stdout.reconfigure(encoding='utf-8')
```

---

## 🔧 Configuración Avanzada

### Configurar Solver Alternativo

Si quieres usar un solver diferente a CBC:

```python
from pulp import *

# GLPK (open source)
prob.solve(GLPK())

# Gurobi (comercial, muy rápido)
prob.solve(GUROBI())

# CPLEX (comercial)
prob.solve(CPLEX())
```

### Configurar Matplotlib para mejor calidad

```python
import matplotlib.pyplot as plt

# Configuración global
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 12
plt.rcParams['figure.figsize'] = (12, 8)
```

---

## 📱 Instalación en Google Colab

Si prefieres ejecutar en la nube:

```python
# En la primera celda del notebook
!pip install pulp networkx matplotlib qrcode reportlab

# Clonar repositorio
!git clone https://github.com/fnjimenez/Curso_Logistica_CV.git
%cd Curso_Logistica_CV

# Ejecutar código
from src.models import ModeloMultiNivel
# ... resto del código
```

---

## 🎓 Instalación en Entornos Educativos

### Laboratorios de Cómputo

Para instalar en múltiples computadoras:

1. **Crear instalador portable** (Windows):
```bash
# Crear carpeta portable
mkdir amazon_logistics_portable
cd amazon_logistics_portable

# Copiar archivos del proyecto
# Crear requirements_portable.txt con versiones específicas

# Distribuir a los estudiantes
```

2. **Script de instalación batch** (Windows):
```batch
@echo off
echo Instalando Amazon Logistics...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo Instalación completada!
pause
```

3. **Script de instalación shell** (Linux/Mac):
```bash
#!/bin/bash
echo "Instalando Amazon Logistics..."
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
echo "¡Instalación completada!"
```

---

## 💡 Consejos

1. **Usa entorno virtual siempre** - Evita conflictos de versiones
2. **Actualiza pip primero** - `pip install --upgrade pip`
3. **Instala una dependencia a la vez** - Si hay errores, más fácil debuggear
4. **Guarda el output** - `pip freeze > requirements_actual.txt`
5. **Documenta problemas** - Si algo falla, anota el error completo

---

## 📚 Recursos Adicionales

- **Documentación PuLP**: https://coin-or.github.io/pulp/
- **NetworkX Tutorial**: https://networkx.org/documentation/stable/tutorial.html
- **Matplotlib Gallery**: https://matplotlib.org/stable/gallery/index.html
- **Python Packaging**: https://packaging.python.org/

---

## ✅ Checklist Final

Antes de empezar a trabajar, verifica:

- [ ] Python 3.8+ instalado
- [ ] pip funcionando
- [ ] Repositorio clonado
- [ ] Entorno virtual creado y activado
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] Jupyter funcionando (`jupyter notebook`)
- [ ] Tests pasando (`pytest tests/ -v`)
- [ ] Ejemplo básico ejecutándose

---

## 🆘 Ayuda

Si después de seguir esta guía sigues teniendo problemas:

1. **Revisa la sección de problemas comunes** arriba
2. **Busca el error en Google** - Probablemente alguien ya lo resolvió
3. **Crea un issue** en: https://github.com/fnjimenez/Curso_Logistica_CV/issues
4. **Incluye**:
   - Sistema operativo
   - Versión de Python
   - Error completo
   - Pasos que seguiste

---

**¡Listo para optimizar logística! 🚀**

*Última actualización: Octubre 2025*
