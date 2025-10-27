"""
Módulo de Configuración

Almacena todas las constantes y parámetros globales del proyecto
para facilitar los ajustes y evitar "magic numbers".
"""

# --- Parámetros de Adquisición ---
TICKER_SIMBOLO: str = "SPY"
PERIODO_DATOS: str = "5y"

# --- Parámetros de Procesamiento ---
SMA_CORTA_PERIODO: int = 50
SMA_LARGA_PERIODO: int = 200
VOLATILIDAD_PERIODO: int = 30