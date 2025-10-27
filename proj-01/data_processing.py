"""
Módulo de Procesamiento de Datos (data_processing.py)

Responsable de limpiar y transformar datos crudos, así como
de calcular métricas técnicas y características (features).
"""

import pandas as pd
import numpy as np # Importado para el bloque de prueba
from typing import Optional
# ¡DEPENDENCIA DE CONFIG ELIMINADA!

def procesar_datos_financieros(
    datos_crudos: pd.DataFrame,
    sma_corta: int = 50,
    sma_larga: int = 200,
    vol_periodo: int = 30
) -> Optional[pd.DataFrame]:
    """
    Procesa los datos OHLCV crudos para calcular métricas técnicas.

    Esta función ahora recibe los períodos de ventana como argumentos,
    haciéndola flexible y reutilizable.
    """
    if datos_crudos is None or datos_crudos.empty:
        print("Error: No se proporcionaron datos crudos para procesar.")
        return None

    print(f"Iniciando procesamiento de datos (SMA {sma_corta}/{sma_larga}, Vol {vol_periodo}d)...")
    df = datos_crudos.copy()

    # 1. Asegurar DatetimeIndex
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)
    df.index.name = 'Date'

    # 2. Calcular retornos diarios
    df['retornos_diarios'] = df['Close'].pct_change()

    # 3. Calcular Medias Móviles Simples (SMA)
    # Usamos los ARGUMENTOS de la función, no constantes globales
    col_sma_corta = f'SMA_{sma_corta}'
    col_sma_larga = f'SMA_{sma_larga}'

    df[col_sma_corta] = df['Close'].rolling(window=sma_corta).mean()
    df[col_sma_larga] = df['Close'].rolling(window=sma_larga).mean()

    # 4. Calcular Volatilidad Histórica (Rodante)
    # Usamos el ARGUMENTO vol_periodo
    col_volatilidad = f'Volatilidad_{vol_periodo}d'
    df[col_volatilidad] = df['retornos_diarios'].rolling(window=vol_periodo).std()

    print("Procesamiento completado. Métricas calculadas.")
    return df

# --- Bloque de prueba (Refactorizado) ---
if __name__ == "__main__":
    """
    Este bloque permite probar este módulo de forma independiente.
    """
    print("--- Probando el módulo de procesamiento de forma aislada ---")

    # 1. Crear un DataFrame de prueba (ej. 100 días de datos)
    fechas_prueba = pd.date_range(start='2024-01-01', periods=100, freq='D')
    precios_prueba = np.random.rand(100) * 10 + 100 # Precios aleatorios
    df_prueba = pd.DataFrame({'Close': precios_prueba}, index=fechas_prueba)

    print(f"Datos de prueba creados ({len(df_prueba)} filas).")

    # 2. Llamar a la función con parámetros de prueba
    datos_procesados_prueba = procesar_datos_financieros(
        df_prueba,
        sma_corta=10,
        sma_larga=30,
        vol_periodo=15
    )

    if datos_procesados_prueba is not None:
        print("Prueba de procesamiento exitosa.")
        print("Últimas 5 filas del resultado (deberían tener valores):")
        print(datos_procesados_prueba.tail(5))