"""
Módulo de Visualización (visualizer.py)

Responsable de crear y guardar todas las visualizaciones
del proyecto usando Matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional
# Importamos las constantes para saber los nombres de las columnas
from config import SMA_CORTA_PERIODO, SMA_LARGA_PERIODO


def plot_metricas(datos: pd.DataFrame, ticker: str) -> None:
    """
    Crea un gráfico del precio de cierre y las medias móviles (SMA).

    Guarda el gráfico resultante como un archivo .png.

    Args:
        datos (pd.DataFrame): El DataFrame procesado que contiene
                              'Close' y las columnas de SMA.
        ticker (str): El símbolo del activo (usado para títulos y nombres de archivo).
    """
    if datos is None or datos.empty:
        print("Error: No se proporcionaron datos para graficar.")
        return

    print("Iniciando la generación del gráfico...")

    # --- Definición de Nombres de Columnas ---
    # Nos aseguramos de que los nombres coincidan con los creados
    # en el módulo de procesamiento.
    col_sma_corta = f'SMA_{SMA_CORTA_PERIODO}'
    col_sma_larga = f'SMA_{SMA_LARGA_PERIODO}'
    filename = f"{ticker}_metricas_plot.png"

    # --- Creación del Gráfico ---
    try:
        # Establecer el tamaño de la figura (ancho, alto en pulgadas)
        plt.figure(figsize=(14, 7))

        # Graficar las series de datos
        # 'alpha' controla la transparencia (para que el cierre no sea tan dominante)
        plt.plot(datos.index, datos['Close'], label='Precio de Cierre', color='blue', alpha=0.7)
        plt.plot(datos.index, datos[col_sma_corta], label=f'SMA {SMA_CORTA_PERIODO}', color='orange', linestyle='--')
        plt.plot(datos.index, datos[col_sma_larga], label=f'SMA {SMA_LARGA_PERIODO}', color='red', linestyle='--')

        # --- Títulos y Etiquetas ---
        plt.title(f'Precio de Cierre y Medias Móviles para {ticker}', fontsize=16)
        plt.xlabel('Fecha', fontsize=12)
        plt.ylabel('Precio (USD)', fontsize=12)

        # --- Leyenda y Cuadrícula ---
        plt.legend()
        plt.grid(True)

        # --- Guardar el Gráfico ---
        # Guardamos la figura en un archivo antes de mostrarla o cerrarla
        plt.savefig(filename)

        # plt.close() es importante en scripts para liberar la memoria
        # y evitar que el gráfico se muestre en la terminal si no queremos.
        plt.close()

        print(f"Gráfico guardado exitosamente como '{filename}'.")

    except KeyError as e:
        print(f"Error al graficar: Falta una columna esperada. {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado al guardar el gráfico: {e}")


# --- Bloque de prueba (Opcional) ---
if __name__ == "__main__":
    """
    Este bloque permite probar este módulo de forma independiente.
    Necesitaría un set de datos de ejemplo (ej. un CSV) para funcionar.
    """
    print("--- Probando el módulo de visualización de forma aislada ---")
    # Para una prueba real:
    # 1. Cargar un CSV de muestra (ej. 'SPY_datos_procesados.csv' si ya existe)
    # try:
    #     df_prueba = pd.read_csv('SPY_datos_procesados.csv', index_col='Date', parse_dates=True)
    #     plot_metricas(df_prueba, "SPY (Prueba)")
    # except FileNotFoundError:
    #     print("No se encontró archivo CSV de prueba. Ejecute 'main.py' primero.")
    print("Para probar, ejecute 'main.py' o cree datos de muestra aquí.")