"""
Script Principal del Proyecto Quant (main.py)

Orquesta el pipeline completo del procesador de datos:
1. Carga la configuración.
2. Llama al módulo de adquisición para descargar datos.
3. Llama al módulo de procesamiento para calcular métricas.
4. Llama al módulo de almacenamiento para guardar los datos en CSV.
5. Llama al módulo de visualización para generar el gráfico.

Para ejecutar el proyecto completo, corra este archivo:
$ python main.py
"""

# --- Importaciones de nuestros módulos ---
from data_acquisition import descargar_datos_historicos
from data_processing import procesar_datos_financieros
from data_storage import guardar_datos_csv
from visualizer import plot_metricas

# --- Importaciones de configuración ---
from config import TICKER_SIMBOLO, PERIODO_DATOS


def ejecutar_pipeline_completo():
    """
    Función principal que ejecuta todo el pipeline de análisis de datos.
    """
    print(f"=== Iniciando Pipeline de Análisis para {TICKER_SIMBOLO} ===")

    # --- PASO 1: ADQUISICIÓN DE DATOS ---
    datos_crudos = descargar_datos_historicos(TICKER_SIMBOLO, PERIODO_DATOS)

    # Si la descarga falla, datos_crudos será None.
    # Verificamos antes de continuar al siguiente paso.
    if datos_crudos is None:
        print("Error: La descarga de datos falló. El pipeline se detiene.")
        print("==========================================================")
        return  # Termina la ejecución

    # --- PASO 2: PROCESAMIENTO Y CÁLCULO DE MÉTRICAS ---
    datos_procesados = procesar_datos_financieros(datos_crudos)

    if datos_procesados is None:
        print("Error: El procesamiento de datos falló. El pipeline se detiene.")
        print("=============================================================")
        return  # Termina la ejecución

    print("Datos procesados y métricas calculadas con éxito.")

    # --- PASO 3: ALMACENAMIENTO (Salida CSV) ---
    # Guardamos el DataFrame resultante
    guardar_datos_csv(datos_procesados, TICKER_SIMBOLO)

    # --- PASO 4: VISUALIZACIÓN (Salida PNG) ---
    # Creamos y guardamos el gráfico
    plot_metricas(datos_procesados, TICKER_SIMBOLO)

    print(f"=== Pipeline completado exitosamente para {TICKER_SIMBOLO} ===")


# --- Punto de Entrada del Script ---
if __name__ == "__main__":
    """
    Este es el punto de entrada estándar de Python.
    Llama a nuestra función principal para ejecutar el pipeline.
    """
    ejecutar_pipeline_completo()