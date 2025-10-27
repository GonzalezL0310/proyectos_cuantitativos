"""
Módulo de Almacenamiento de Datos (data_storage.py)

Responsable de guardar DataFrames y otros artefactos de datos
en el disco (ej. CSV, Parquet, HDF5, etc.).
"""

import pandas as pd
from typing import Optional


def guardar_datos_csv(datos: pd.DataFrame, ticker: str) -> None:
    """
    Guarda el DataFrame procesado en un archivo CSV.

    El nombre del archivo se basará en el ticker.

    Args:
        datos (pd.DataFrame): El DataFrame procesado a guardar.
        ticker (str): El símbolo del activo (usado para el nombre de archivo).
    """
    if datos is None or datos.empty:
        print("Error: No se proporcionaron datos para guardar en CSV.")
        return

    # Definimos el nombre del archivo
    filename = f"{ticker}_datos_procesados.csv"

    print(f"Iniciando guardado de datos en '{filename}'...")

    try:
        # Guardamos el DataFrame en CSV.
        # index=True es importante para conservar nuestro DatetimeIndex.
        datos.to_csv(filename, index=True)

        print(f"Datos guardados exitosamente en '{filename}'.")

    except Exception as e:
        print(f"Ocurrió un error inesperado al guardar el CSV: {e}")


# --- Bloque de prueba (Opcional) ---
if __name__ == "__main__":
    """
    Este bloque permite probar este módulo de forma independiente.
    """
    print("--- Probando el módulo de almacenamiento de forma aislada ---")
    # Para una prueba real, crearíamos un DataFrame de muestra
    # y lo pasaríamos a guardar_datos_csv()
    # df_prueba = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    # guardar_datos_csv(df_prueba, "PRUEBA")
    # print("Revise si se creó 'PRUEBA_datos_procesados.csv'")
    print("Para probar, ejecute 'main.py' o cree datos de muestra aquí.")

