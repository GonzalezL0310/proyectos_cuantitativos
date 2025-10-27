```markdown
# Quantitative Finance & Engineering Portfolio

## 1. Objetivo

Este repositorio documenta mi trabajo sistemático para el rol de **Quantitative Developer**. Contiene una serie de proyectos progresivos que aplican mi formación en **Ingeniería en Telecomunicaciones** y **Matemáticas Aplicadas** al dominio de las finanzas cuantitativas.

El objetivo es construir un conjunto de herramientas de nivel profesional para el análisis de datos, el modelado estadístico, el *backtesting* de estrategias y la optimización de sistemas.

## 2. Stack Tecnológico (Core)

* **Lenguaje:** Python 3
* **Análisis y Modelado:** Pandas, NumPy, SciPy, Statsmodels, Scikit-learn, TensorFlow/Keras, Hugging Face Transformers
* **Sistemas y Datos:** SQL (PostgreSQL), FastAPI, SQLAlchemy
* **Optimización:** Numba, Cython, `cProfile`
* **Entorno:** Linux (Ubuntu), Git, PyCharm Professional, Pytest

## 3. Estructura del Repositorio

Este es un monorepo que contiene múltiples proyectos. Cada proyecto reside en su propio directorio y está diseñado para ser funcional e independiente, con sus propias dependencias (`requirements.txt`) y su `README.md` específico.

---

## 4. Proyectos

A continuación se listan los proyectos principales en orden de complejidad.

### Nivel Fundamental: Datos e Infraestructura

* **[01] Market Data Processor (Proyecto 1)**
    * **Descripción:** Script de análisis de datos para procesar series temporales de precios (OHLCV).
    * **Habilidades:** `Pandas` (manipulación, ventanas rodantes), `Matplotlib` (visualización).

* **[02] Market Data Pipeline (Proyecto 2)**
    * **Descripción:** Un pipeline ETL que consume una API de mercado y persiste los datos en una base de datos `PostgreSQL`.
    * **Habilidades:** `SQL` (diseño de esquemas, `INSERT`), `SQLAlchemy`, `cronjobs`.

* **[03] Backtesting Engine API (Proyecto 3)**
    * **Descripción:** Un motor de *backtesting* de estrategias simples (ej. MVA Crossover) expuesto como una API REST.
    * **Habilidades:** `FastAPI` (creación de *endpoints*), `OOP` (diseño de clases de estrategia), `JSON`.

### Nivel Intermedio: Modelado Quant y ML

* **[04] VaR Calculator (Proyecto 4)**
    * **Descripción:** Módulo de análisis de riesgo que implementa tres métodos de cálculo de Valor en Riesgo (VaR).
    * **Habilidades:** `Métodos Numéricos` (Simulación Monte Carlo), `SciPy.stats` (VaR Paramétrico), `Pandas` (VaR Histórico).

* **[05] Statistical Arbitrage Backtester (Proyecto 5)**
    * **Descripción:** Implementación de una estrategia de *Pair Trading* (Arbitraje Estadístico) basada en pruebas de cointegración.
    * **Habilidades:** `Statsmodels` (Test de Dickey-Fuller), modelado de series temporales.

* **[06] Option Pricer (Proyecto 6)**
    * **Descripción:** Calculadora de precios de opciones que implementa el modelo Black-Scholes-Merton y sus "Griegas".
    * **Habilidades:** `OOP` (implementación de fórmulas), `Pytest` (pruebas unitarias para precisión matemática).

* **[07] ML Strategy Backtester (Proyecto 7)**
    * **Descripción:** Extensión del motor de *backtesting* para usar modelos de ML (ej. Random Forest) como generadores de señales.
    * **Habilidades:** `Scikit-learn` (ingeniería de características, `Pipeline`, `RandomForestClassifier`), `joblib` (serialización).

### Nivel Avanzado: DSP, NLP y Optimización

* **[08] Cyclical Analysis (Proyecto 8)**
    * **Descripción:** Aplicación de técnicas de Procesamiento Digital de Señales (DSP) para encontrar ciclos de mercado.
    * **Habilidades:** `NumPy.fft` (Transformada Rápida de Fourier), `SciPy.signal` (análisis espectral, filtrado).

* **[11] NLP Sentiment Strategy (Proyecto 11)**
    * **Descripción:** Estrategia híbrida que incorpora análisis de sentimiento de noticias financieras en tiempo real.
    * **Habilidades:** `Hugging Face Transformers` (uso de FinBERT), `APIs` de noticias, `regex`.

* **[12] HPC Backtesting Engine (Proyecto 12)**
    * **Descripción:** Optimización de alto rendimiento del motor de *backtesting* (Proyecto 03) para *grid search*.
    * **Habilidades:** `cProfile` (identificación de cuellos de botella), `Numba` (compilación JIT), `NumPy` (vectorización).
```