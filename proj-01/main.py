"""
Script Principal del Proyecto Quant (main.py)

Orquesta el pipeline completo del procesador de datos.
Este script es ahora el ÚNICO módulo que conoce 'config.py'.
"Inyecta" las configuraciones en los módulos de lógica "tontos".
"""

# --- Importaciones de nuestros módulos ---
from data_acquisition import descargar_datos_historicos
from data_processing import procesar_datos_financieros
from data_storage import guardar_datos_csv
from visualizer import plot_metricas

# --- Importaciones de configuración (¡AHORA INTELIGENTE!) ---
# Tarea 5: Importar TODAS las constantes necesarias
from config import (
    TICKER_SIMBOLO,
    PERIODO_DATOS,
    SMA_CORTA_PERIODO,
    SMA_LARGA_PERIODO,
    VOLATILIDAD_PERIODO
)

def ejecutar_pipeline_completo():
    """
    Función principal que ejecuta todo el pipeline de análisis de datos.
    """
    print(f"=== Iniciando Pipeline de Análisis para {TICKER_SIMBOLO} ===")

    # --- PASO 1: ADQUISICIÓN DE DATOS ---
    # Inyectamos los parámetros de config en la función
    datos_crudos = descargar_datos_historicos(TICKER_SIMBOLO, PERIODO_DATOS)

    if datos_crudos is None:
        print("Error: La descarga de datos falló. El pipeline se detiene.")
        return

    # --- PASO 2: PROCESAMIENTO Y CÁLCULO DE MÉTRICAS ---
    # Tarea 5: Inyectar los períodos de SMA y Volatilidad
    datos_procesados = procesar_datos_financieros(
        datos_crudos,
        SMA_CORTA_PERIODO,
        SMA_LARGA_PERIODO,
        VOLATILIDAD_PERIODO
    )

    if datos_procesados is None:
        print("Error: El procesamiento de datos falló. El pipeline se detiene.")
        return

    print("Datos procesados y métricas calculadas con éxito.")

    # --- PASO 3: ALMACENAMIENTO (Salida CSV) ---
    guardar_datos_csv(datos_procesados, TICKER_SIMBOLO)

    # --- PASO 4: VISUALIZACIÓN (Salida PNG) ---

    # Tarea 5: Generar los nombres de columna dinámicamente
    # para pasárselos al visualizador.
    col_sma_corta_nombre = f'SMA_{SMA_CORTA_PERIODO}'
    col_sma_larga_nombre = f'SMA_{SMA_LARGA_PERIODO}'

    # Inyectar los nombres de columna exactos en la función
    plot_metricas(
        datos_procesados,
        TICKER_SIMBOLO,
        'Close',  # Columna de precio
        col_sma_corta_nombre,
        col_sma_larga_nombre
    )

    print(f"=== Pipeline completado exitosamente para {TICKER_SIMBOLO} ===")

# --- Punto de Entrada del Script ---
if __name__ == "__main__":
    ejecutar_pipeline_completo()