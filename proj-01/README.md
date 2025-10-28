Proyecto 1: Pipeline de Procesamiento de Datos Financieros

El script automatiza el proceso de descargar datos históricos de un activo financiero, procesarlos para calcular métricas técnicas clave y generar salidas listas para el análisis (un archivo CSV y un gráfico).

(El archivo SPY_metricas_plot.png será generado por el script)

🚀 Características

    Adquisición de Datos: Descarga datos históricos (OHLCV) de los últimos 5 años desde Yahoo Finance (yfinance).

    Procesamiento de Métricas: Calcula las siguientes métricas usando pandas:

        Retornos diarios.

        Media Móvil Simple (SMA) de 50 días.

        Media Móvil Simple (SMA) de 200 días.

        Volatilidad histórica (desviación estándar) de 30 días.

    Arquitectura Modular: El código está separado en módulos lógicos (adquisición, procesamiento, almacenamiento, visualización) para facilitar la mantenibilidad y las pruebas.

    Configuración Centralizada: Todas las variables (ticker, períodos) se gestionan en un único archivo config.py.

    Salida Dual: Genera dos archivos:

        Un archivo .csv con todos los datos y métricas.

        Un archivo .png con la visualización del precio y las SMAs.

📂 Estructura del Proyecto

El proyecto está organizado en módulos de "Separación de Responsabilidades" (Separation of Concerns) para un código más limpio y escalable.
Bash

```
mi_proyecto_quant/
├── config.py             # Almacena constantes y parámetros (ticker, SMA, etc.)
├── data_acquisition.py   # Módulo para descargar datos de yfinance
├── data_processing.py    # Módulo para calcular métricas (SMA, volatilidad)
├── data_storage.py       # Módulo para guardar el DataFrame en CSV
├── visualizer.py         # Módulo para crear y guardar el gráfico con Matplotlib
├── main.py               # Orquestador principal que ejecuta el pipeline
└── requirements.txt      # Dependencias del proyecto
```

🔧 Instalación

Para ejecutar este proyecto, necesitarás Python 3.8+ y las siguientes librerías:
Clona este repositorio:

```
Bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO
```

(Recomendado) Crea un entorno virtual:
```
Bash

python -m venv venv
source venv/bin/activate   # En Linux/macOS
.\venv\Scripts\activate    # En Windows
```

Instala las dependencias: (Puedes crear un archivo requirements.txt con el siguiente contenido)
```
requirements.txt
Plaintext

pandas
yfinance
matplotlib
```

Luego instala con:

```
Bash 
pip install -r requirements.txt
```

🏃‍♂️ Cómo Usarlo

La ejecución se realiza a través del script main.py.
```
Bash
python main.py
```

El script ejecutará el pipeline completo y verás los mensajes de estado en la consola:

    Descargará los datos de SPY (o el ticker en config.py).

    Procesará los datos para calcular las métricas.

    Guardará SPY_datos_procesados.csv en la carpeta.

    Guardará SPY_metricas_plot.png en la carpeta.

Para analizar un activo diferente o cambiar los períodos de las medias móviles, simplemente edita el archivo config.py. No necesitas tocar la lógica del código en los otros módulos.

🔬 Explicación del Código

Cada módulo tiene una responsabilidad única.

config.py

```
Funciona como el "panel de control" del proyecto. 
Almacena todas las constantes globales para evitar "números mágicos" en el código.
```

data_acquisition.py

    Contiene la función descargar_datos_historicos(ticker, periodo).

    Utiliza yfinance.Ticker(ticker).history(period=periodo) para obtener los datos.

    Incluye manejo de errores básico si no se encuentran datos para el ticker.

    Devuelve un DataFrame de pandas crudo con OHLCV.

data_processing.py
```
Contiene la función procesar_datos_financieros(datos_crudos).

Toma el DataFrame crudo y realiza los cálculos vectorizados de pandas.

df['retornos_diarios'] = df['Close'].pct_change()

df[col_sma] = df['Close'].rolling(window=...).mean()

df[col_vol] = df['retornos_diarios'].rolling(window=...).std()

Nota sobre los NaN: Es normal que las primeras N filas de las métricas sean NaN (o <null> en el CSV).
Esto es matemáticamente necesario, ya que un cálculo rodante (ej. SMA 50) 
necesita 49 días de datos previos para calcular su primer valor.
```
data_storage.py

    Contiene la función guardar_datos_csv(datos, ticker).

    Utiliza datos.to_csv(filename) para exportar el DataFrame procesado.

    El nombre del archivo se genera dinámicamente usando el ticker (ej. SPY_datos_procesados.csv).

visualizer.py

    Contiene la función plot_metricas(datos, ticker).

    Utiliza matplotlib.pyplot para crear el gráfico.

    Grafica el precio de Cierre ('Close'), SMA_50 y SMA_200.

    Añade títulos, etiquetas, leyenda y cuadrícula para mayor claridad.

    Guarda el gráfico en un archivo .png usando plt.savefig(filename).

    Usa plt.close() para liberar memoria y evitar que el gráfico se muestre en la consola.

main.py

    Es el orquestador y punto de entrada del programa.

    No contiene lógica de procesamiento, solo llama a las funciones de los otros módulos en el orden correcto.

    Su función ejecutar_pipeline_completo() define el flujo:

        datos_crudos = descargar_datos_historicos(...)

        datos_procesados = procesar_datos_financieros(datos_crudos)

        guardar_datos_csv(datos_procesados, ...)

        plot_metricas(datos_procesados, ...)

    Se ejecuta solo cuando se llama directamente al script, gracias al bloque if __name__ == "__main__":.