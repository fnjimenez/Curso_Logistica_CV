# 🚚 Amazon Logistics Optimization - México 2025

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

Sistema de optimización logística para Amazon México con modelos de transporte de 1 y 2 niveles usando programación lineal.

## 📋 Descripción

Este proyecto implementa modelos de optimización para la red de distribución de Amazon en México, incluyendo:

- **Modelo Clásico (1 nivel)**: Transporte directo origen → destino
- **Modelo Multi-Nivel (2 niveles)**: Red realista con centros de distribución intermedios
- **Visualizaciones interactivas**: Gráficos de red con NetworkX
- **Análisis comparativo**: Comparación de costos entre escenarios

## 🎯 Características

- ✅ Optimización con PuLP (CBC solver)
- ✅ Visualización de redes con NetworkX
- ✅ Generación de reportes PDF con QR codes
- ✅ Escenarios múltiples (base, optimista, pesimista)
- ✅ Análisis de sensibilidad
- ✅ Tests unitarios con pytest
- ✅ Documentación completa

## 📁 Estructura del Proyecto

```
Curso_Logistica_CV/
│
├── notebooks/                          # Jupyter Notebooks
│   ├── Amazon_Logistics_v3.2.ipynb    # Versión original (1 nivel)
│   ├── Amazon_Logistics_v4.0.ipynb    # Versión mejorada (multi-nivel)
│   └── Comparacion_Modelos.ipynb      # Comparación entre modelos
│
├── src/                               # Código fuente
│   ├── __init__.py
│   ├── models.py                      # Modelos de optimización
│   ├── visualization.py               # Funciones de visualización
│   └── utils.py                       # Utilidades
│
├── docs/                              # Documentación
│   ├── AUDITORIA_COMPLETA.md         # Auditoría técnica
│   ├── GUIA_INSTALACION.md           # Guía de instalación
│   ├── PROBLEMA_RED_MULTINIVEL.md    # Explicación del problema
│   └── API.md                         # Documentación de la API
│
├── examples/                          # Ejemplos de uso
│   ├── ejemplo_basico.py
│   ├── ejemplo_multinivel.py
│   └── ejemplo_comparacion.py
│
├── tests/                             # Tests unitarios
│   └── test_amazon_logistics.py
│
├── results/                           # Resultados y gráficos
│   └── .gitkeep
│
├── requirements.txt                   # Dependencias
├── setup.py                          # Instalación del paquete
├── README.md                         # Este archivo
├── LICENSE                           # Licencia MIT
└── .gitignore                        # Archivos ignorados

```

## 🚀 Instalación Rápida

### Prerequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Clonar el repositorio

```bash
git clone https://github.com/fnjimenez/Curso_Logistica_CV.git
cd Curso_Logistica_CV
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

O instalar el paquete completo:

```bash
pip install -e .
```

## 📦 Dependencias Principales

```
pulp>=2.7.0              # Optimización lineal
networkx>=3.0            # Análisis de redes
matplotlib>=3.5.0        # Visualización
numpy>=1.21.0            # Cálculos numéricos
pandas>=1.3.0            # Análisis de datos
Pillow>=9.0.0            # Procesamiento de imágenes
qrcode>=7.3.1            # Generación de códigos QR
reportlab>=3.6.0         # Generación de PDFs
pytest>=7.0.0            # Testing
```

## 🎮 Uso Rápido

### Modelo Básico (1 nivel)

```python
from src.models import ModeloTransporteBasico

# Crear modelo
modelo = ModeloTransporteBasico(student_id=4021)

# Generar datos
datos = modelo.generar_datos()

# Resolver
resultado = modelo.resolver()

# Visualizar
modelo.visualizar_red(resultado)

print(f"Costo total: ${resultado['costo_total']:,.2f} MXN")
```

### Modelo Multi-Nivel (2 niveles)

```python
from src.models import ModeloMultiNivel

# Crear modelo con centros de distribución
modelo = ModeloMultiNivel()

# Resolver
resultado = modelo.resolver()

# Generar reporte
modelo.generar_reporte(resultado)

# Visualizar red
modelo.visualizar_red(resultado, filename='red_multinivel.png')
```

### Comparación de Modelos

```python
from examples.ejemplo_comparacion import comparar_modelos

# Comparar ambos enfoques
comparacion = comparar_modelos(student_id=4021)

# Resultados
print(f"Modelo 1 nivel: ${comparacion['modelo_1nivel']['costo']:,.2f}")
print(f"Modelo 2 niveles: ${comparacion['modelo_2niveles']['costo']:,.2f}")
print(f"Diferencia: {comparacion['diferencia_porcentual']:.2f}%")
```

## 📊 Notebooks Interactivos

### 1. Modelo Clásico (v3.2)
```bash
jupyter notebook notebooks/Amazon_Logistics_v3.2.ipynb
```

Incluye:
- Modelo de transporte directo
- Escenarios base/optimista/pesimista
- Visualizaciones básicas
- Generación de reportes PDF

### 2. Modelo Multi-Nivel (v4.0) - ¡NUEVO!
```bash
jupyter notebook notebooks/Amazon_Logistics_v4.0.ipynb
```

Incluye:
- Red de 2 niveles (plantas → CDs → ciudades)
- Optimización de ubicación de CDs
- Análisis de utilización
- Comparación con modelo clásico

### 3. Comparación de Modelos
```bash
jupyter notebook notebooks/Comparacion_Modelos.ipynb
```

Análisis comparativo completo entre ambos enfoques.

## 🧪 Ejecutar Tests

```bash
# Todos los tests
pytest tests/ -v

# Con cobertura
pytest tests/ --cov=src --cov-report=html

# Solo tests rápidos
pytest tests/ -v -m "not slow"
```

## 📈 Resultados

### Modelo 1 Nivel (Actual)
- **Costo promedio**: ~$10.5M MXN
- **Rutas activas**: 36
- **Complejidad**: Baja
- **Realismo**: Medio

### Modelo 2 Niveles (Propuesto)
- **Costo promedio**: ~$11.2M MXN
- **CDs activos**: 3-4 de 4
- **Complejidad**: Media
- **Realismo**: Alto

### Ventajas Modelo Multi-Nivel
- ✅ Más realista para operaciones Amazon
- ✅ Flexibilidad en redistribución
- ✅ Consolidación de inventario
- ✅ Mejor servicio al cliente
- ✅ Preparado para escalabilidad

## 📚 Documentación

- [**Auditoría Completa**](docs/AUDITORIA_COMPLETA.md): Análisis técnico detallado
- [**Guía de Instalación**](docs/GUIA_INSTALACION.md): Setup paso a paso
- [**Problema Red Multi-Nivel**](docs/PROBLEMA_RED_MULTINIVEL.md): Explicación del diseño
- [**API Reference**](docs/API.md): Documentación de funciones

## 🎓 Contexto Educativo

Este proyecto fue desarrollado para el curso de Logística en SABES San Felipe, México, como parte del programa de formación en optimización de cadenas de suministro.

### Objetivos de Aprendizaje
- Modelado de problemas de transporte
- Programación lineal aplicada
- Análisis de redes logísticas
- Visualización de datos
- Desarrollo de software Python

## 👥 Contribuir

Las contribuciones son bienvenidas! Por favor:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/NuevaFuncionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/NuevaFuncionalidad`)
5. Abre un Pull Request

## 🐛 Reportar Bugs

Si encuentras un bug, por favor abre un [issue](https://github.com/fnjimenez/Curso_Logistica_CV/issues) con:
- Descripción del problema
- Pasos para reproducirlo
- Comportamiento esperado vs actual
- Screenshots si es posible
- Tu entorno (OS, Python version, etc.)

## 📝 Changelog

### v4.0 (2025-10-26)
- ✨ Nuevo: Modelo multi-nivel con centros de distribución
- ✨ Nuevo: Notebook de comparación de modelos
- 🔧 Fix: Error en generación de PDF con QR codes
- 📚 Docs: Documentación completa y auditoría
- 🧪 Tests: Suite completa de tests unitarios
- 🎨 Mejora: Visualizaciones más profesionales

### v3.2 (2025-10-15)
- 🔧 Fix: Corrección en función make_pdf_infographic
- 📊 Mejora: Visualizaciones de red
- 📝 Docs: Docstrings agregados

### v3.0 (2025-09-01)
- 🎉 Primera versión funcional
- 📊 Modelo de transporte básico
- 📈 Escenarios múltiples
- 🎨 Visualizaciones con NetworkX

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 🙏 Agradecimientos

- **SABES San Felipe** - Institución educativa
- **PuLP** - Framework de optimización lineal
- **NetworkX** - Librería de análisis de redes
- **Comunidad Python** - Por las excelentes librerías

## 📬 Contacto

**Francisco Jiménez**
- GitHub: [@fnjimenez](https://github.com/fnjimenez)
- Email: [tu-email@ejemplo.com]

**Curso de Logística - SABES San Felipe**
- Ubicación: San Felipe, Guanajuato, México
- Año: 2025

## ⭐ Apóyanos

Si este proyecto te fue útil, por favor:
- ⭐ Dale una estrella al repositorio
- 🔀 Compártelo con otros
- 💬 Deja tus comentarios y sugerencias

---

**Desarrollado con ❤️ en México** 🇲🇽

*Última actualización: Octubre 2025*
