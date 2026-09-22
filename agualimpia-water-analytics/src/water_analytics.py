import pandas as pd
import numpy as np
from scipy import stats
import joblib

def calcular_eficiencia_remocion(df, col_entrada='DBO_entrada_mg_L', col_salida='DBO_salida_mg_L'):
    entrada = df[col_entrada].to_numpy()
    salida = df[col_salida].to_numpy()
    eficiencia = ((entrada - salida) / entrada) * 100
    return np.round(eficiencia, 2)

def evaluar_anomalias_scipy(df, col='DBO_salida_mg_L'):
    z_scores = stats.zscore(df[col])
    es_anomalia = np.abs(z_scores) > 2.0
    return z_scores, es_anomalia

def clasificar_alertas_operativas(df):
    def definir_alerta(row):
        if row['DBO_salida_mg_L'] > 30:
            return 'ALERTA CRÍTICA: DBO Salida > 30 mg/L'
        elif row['eficiencia_DBO'] < 85:
            return 'ADVERTENCIA: Eficiencia < 85%'
        return 'OPERACIÓN NORMAL'
    return df.apply(definir_alerta, axis=1)

def exportar_reportes(df_ops, df_env):
    df_ops.to_excel('outputs/reporte_operaciones.xlsx', index=False)
    df_env.to_excel('outputs/reporte_gestion_ambiental.xlsx', index=False)

def serializar_procesador(objeto_pipeline, filepath='outputs/pipeline_aqualimpia.joblib'):
    joblib.dump(objeto_pipeline, filepath)