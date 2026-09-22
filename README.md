[README.md](https://github.com/user-attachments/files/32493233/README.md)
Proyecto Analítico AquaLimpia S. A. - Control y Gestión de Efluentes
1. Objetivos del Proyecto
General: Diagnosticar analíticamente la causa de los incumplimientos en la calidad del efluente (DBO Salida) en las plantas de tratamiento de AquaLimpia S. A.

Específicos:

Identificar la tasa de cumplimiento normativo (DBO Salida <= 30 mg/L) por planta.

Determinar la relación entre caudal de entrada, carga orgánica (DBO Entrada) y consumo energético de aireación.

Automatizar la generación de reportes sectorizados para Operaciones y Gestión Ambiental.

2. Metodología y Stack Tecnológico
Carga y Validación: Ingesta del dataset oficial (dataset_set_A_aguas_residuales.xlsx) con 200 registros.

Ingeniería de Características: Cálculo de la Eficiencia de Remoción de DBO (%) y categorización de alertas operativas.

Análisis Estadístico: Evaluación de asimetría (skewness) y detección de anomalías usando SciPy.

Persistencia y Módulos: Creación de funciones reutilizables en src/water_analytics.py y serialización del artefacto analítico usando Joblib.

Entorno Tecnológico: Python (Pandas, NumPy, SciPy, Joblib, Matplotlib, Seaborn), VS Code, Jupyter Notebooks y Git/GitHub.

3. Resumen de Resultados por Planta
Planta Centro: Caudal Promedio = 5,160 m³/día | DBO Salida Promedio = 35.90 mg/L | Eficiencia Promedio = 86.8% | Cumplimiento Normativo = 22.7%

Planta Norte: Caudal Promedio = 5,115 m³/día | DBO Salida Promedio = 36.56 mg/L | Eficiencia Promedio = 86.6% | Cumplimiento Normativo = 16.9%

Planta Sur: Caudal Promedio = 4,888 m³/día | DBO Salida Promedio = 36.06 mg/L | Eficiencia Promedio = 87.2% | Cumplimiento Normativo = 29.6%

Promedio Global: Caudal Promedio = 5,059 m³/día | DBO Salida Promedio = 36.18 mg/L | Eficiencia Promedio = 86.9% | Cumplimiento Normativo = 22.5%

4. Estructura del Repositorio
aqualimpia-water-analytics/
data/ (Dataset fuente)
dashboards/ (Dashboard exploratorio renderizado)
notebooks/ (Cuaderno interactivo de análisis)
outputs/ (Reportes generados en Excel y artefacto Joblib)
src/ (Módulo de funciones reutilizables)
main.py (Script principal de ejecución)
requirements.txt (Dependencias del proyecto)
README.md (Documentación técnica principal)

5. Instrucciones de Ejecución
Clonar el repositorio desde GitHub.

Instalar las dependencias usando el comando: py -m pip install -r requirements.txt

Ejecutar el pipeline analítico mediante el comando: py main.py

6. Conclusiones y Decisiones Basadas en Datos
Ajuste Operacional (OPEX): Implementar control automático de aireación guiado por sensores de Oxígeno Disuelto y DBO para estabilizar la salida por debajo del límite legal (30 mg/L).

Priorización de CAPEX: Priorizar la actualización de infraestructura e inversión en la Planta Norte, por registrar el menor porcentaje de cumplimiento (16.9%).

Gobierno de Datos: Corregir la lógica de etiquetado en la base de datos origen, donde se detectaron 28 registros no conformes etiquetados incorrectamente.
