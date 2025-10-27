"""
Módulo de Adquisición de Datos (data_acquisition.py)

Responsable de conectarse a fuentes externas (yfinance) y
descargar datos crudos.
"""

import yfinance as yf
import pandas as pd
from typing import Optional
# ¡DEPENDENCIA DE CONFIG ELIMINADA!

def descargar_datos_historicos(ticker: str, periodo: str) -> Optional[pd.DataFrame]:
    """
    Descarga datos históricos OHLCV para un símbolo y período dados.
    Esta función es ahora "pura": no depende de ninguna
    configuración global.
    """
    print(f"Iniciando descarga de datos para {ticker} (período: {periodo})...")
    try:
        activo = yf.Ticker(ticker)
        datos: pd.DataFrame = activo.history(period=periodo)

        if datos.empty:
            print(f"Error: No se encontraron datos para {ticker} en el período {periodo}.")
            return None

        print(f"Descarga completada. {len(datos)} filas de datos obtenidas.")

        columnas_estandar = ['Open', 'High', 'Low', 'Close', 'Volume']
        columnas_a_mantener = [col for col in columnas_estandar if col in datos.columns]

        return datos[columnas_a_mantener]

    except Exception as e:
        print(f"Ocurrió un error inesperado durante la descarga: {e}")
        return None

# --- Bloque de prueba (Refactorizado) ---
if __name__ == "__main__":
    """
    Este bloque permite probar este módulo de forma independiente.
    Ej: 'python data_acquisition.py'
    """
    print("--- Probando el módulo de adquisición de forma aislada ---")

    # Constantes locales solo para esta prueba
    TICKER_PRUEBA = "AAPL"
    PERIODO_PRUEBA = "1y"

    datos_prueba = descargar_datos_historicos(TICKER_PRUEBA, PERIODO_PRUEBA)

    if datos_prueba is not None:
        print(f"Prueba exitosa para {TICKER_PRUEBA}. Primeras 3 filas:")
        print(datos_prueba.head(3))