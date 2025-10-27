"""
Amazon Logistics Optimization Package
Sistema de optimización para redes de distribución

Módulos:
- models: Modelos de optimización (1 y 2 niveles)
- visualization: Funciones de visualización
- utils: Utilidades y helpers
"""

__version__ = "4.0.0"
__author__ = "Francisco Jiménez - SABES San Felipe"
__email__ = "tu-email@ejemplo.com"

from .models import (
    ModeloTransporteBasico,
    ModeloMultiNivel,
    generar_datos_estudiante,
    resolver_red_multinivel,
)

__all__ = [
    "ModeloTransporteBasico",
    "ModeloMultiNivel",
    "generar_datos_estudiante",
    "resolver_red_multinivel",
]
