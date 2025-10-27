"""
Módulo de Procesamiento de Datos (data_processing.py)

Responsable de limpiar y transformar datos crudos, así como
de calcular métricas técnicas y características (features).
"""

import pandas as pd
from typing import Optional
# Importamos las constantes de procesamiento
from config import SMA_CORTA_PERIODO, SMA_LARGA_PERIODO, VOLATILIDAD_PERIODO


def procesar_datos_financieros(datos_crudos: pd.DataFrame) -> Optional[pd.DataFrame]:
    """
    Procesa los datos OHLCV crudos para calcular métricas técnicas.
    """
    if datos_crudos is None or datos_crudos.empty:
        print("Error: No se proporcionaron datos crudos para procesar.")
        return None

    print("Iniciando procesamiento de datos...")
    df = datos_crudos.copy()

    # 1. Asegurar DatetimeIndex
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)
    df.index.name = 'Date'

    # 2. Calcular retornos diarios
    df['retornos_diarios'] = df['Close'].pct_change()

    # 3. Calcular Medias Móviles Simples (SMA)
    col_sma_corta = f'SMA_{SMA_CORTA_PERIODO}'
    col_sma_larga = f'SMA_{SMA_LARGA_PERIODO}'
    df[col_sma_corta] = df['Close'].rolling(window=SMA_CORTA_PERIODO).mean()
    df[col_sma_larga] = df['Close'].rolling(window=SMA_LARGA_PERIODO).mean()

    # 4. Calcular Volatilidad Histórica (Rodante)
    col_volatilidad = f'Volatilidad_{VOLATILIDAD_PERIODO}d'
    df[col_volatilidad] = df['retornos_diarios'].rolling(window=VOLATILIDAD_PERIODO).std()

    print("Procesamiento completado. Métricas calculadas.")
    return df


# --- Bloque de prueba (Opcional) ---
if __name__ == "__main__":
    """
    Este bloque permite probar este módulo de forma independiente.
    Necesitaría un set de datos de ejemplo para funcionar.
    """
    print("--- Probando el módulo de procesamiento de forma aislada ---")
    # Para una prueba real, aquí cargaríamos un archivo CSV de muestra
    # y lo pasaríamos a procesar_datos_financieros()
    print("Para probar, ejecute 'main.py' o cree datos de muestra aquí.")

    