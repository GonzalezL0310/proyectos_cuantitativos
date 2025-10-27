"""
Módulo de Visualización (visualizer.py)

Responsable de crear y guardar todas las visualizaciones
del proyecto usando Matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt
# ¡DEPENDENCIA DE CONFIG ELIMINADA!

def plot_metricas(
    datos: pd.DataFrame,
    ticker: str,
    col_precio: str,
    col_sma_corta: str,
    col_sma_larga: str
) -> None:
    """
    Crea un gráfico del precio de cierre y las medias móviles (SMA).

    Esta función ahora es "tonta": grafica exactamente
    los nombres de columna que se le pasan como argumentos.
    """
    if datos is None or datos.empty:
        print("Error: No se proporcionaron datos para graficar.")
        return

    print("Iniciando la generación del gráfico...")

    # --- Tarea 4: Validación de Columnas ---
    columnas_requeridas = [col_precio, col_sma_corta, col_sma_larga]
    columnas_faltantes = [col for col in columnas_requeridas if col not in datos.columns]

    if columnas_faltantes:
        print(f"Error al graficar: Faltan columnas en el DataFrame: {columnas_faltantes}")
        return

    filename = f"{ticker}_metricas_plot.png"

    # --- Creación del Gráfico ---
    try:
        plt.figure(figsize=(14, 7))

        # --- Tarea 4: Usar argumentos para graficar ---
        plt.plot(datos.index, datos[col_precio], label='Precio de Cierre', color='blue', alpha=0.7)
        plt.plot(datos.index, datos[col_sma_corta], label=col_sma_corta, color='orange', linestyle='--')
        plt.plot(datos.index, datos[col_sma_larga], label=col_sma_larga, color='red', linestyle='--')

        plt.title(f'Precio de Cierre y Medias Móviles para {ticker}', fontsize=16)
        plt.xlabel('Fecha', fontsize=12)
        plt.ylabel('Precio (USD)', fontsize=12)
        plt.legend()
        plt.grid(True)
        plt.savefig(filename)
        plt.close()

        print(f"Gráfico guardado exitosamente como '{filename}'.")

    except KeyError as e:
        print(f"Error al graficar: Fallo al acceder a la columna. {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado al guardar el gráfico: {e}")

# --- Bloque de prueba (Sin cambios, solo informativo) ---
if __name__ == "__main__":
    print("--- Probando el módulo de visualización de forma aislada ---")
    print("Para probar, ejecute 'main.py' o cree datos de muestra aquí.")