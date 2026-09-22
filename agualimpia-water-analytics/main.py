import pandas as pd
from src.water_analytics import (
    calcular_eficiencia_remocion,
    evaluar_anomalias_scipy,
    clasificar_alertas_operativas,
    exportar_reportes,
    serializar_procesador
)

def ejecutar_pipeline():
    df = pd.read_excel('data/dataset_set_A_aguas_residuales.xlsx')
    df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])
    
    df['eficiencia_DBO'] = calcular_eficiencia_remocion(df)
    
    z_scores, anomalias = evaluar_anomalias_scipy(df)
    df['z_score_DBO_salida'] = z_scores
    df['es_anomalia_estadistica'] = anomalias
    
    df['alerta_operativa'] = clasificar_alertas_operativas(df)
    
    cols_ops = [
        'fecha_registro', 'planta', 'caudal_entrada_m3_d', 
        'DBO_entrada_mg_L', 'DBO_salida_mg_L', 'eficiencia_DBO',
        'energia_aeracion_kWh', 'lodos_generados_kg_d', 'alerta_operativa'
    ]
    df_ops = df[cols_ops].sort_values(by=['planta', 'fecha_registro'])
    
    cols_env = ['fecha_registro', 'planta', 'DBO_salida_mg_L', 'cumplimiento_norma']
    df_env = df[cols_env].copy()
    df_env['estado_cumplimiento'] = df_env['cumplimiento_norma'].map({1: 'Conforme', 0: 'No Conforme'})
    df_env = df_env.sort_values(by=['planta', 'fecha_registro'])
    
    exportar_reportes(df_ops, df_env)
    
    pipeline_artefacto = {
        'media_dbo_salida': float(df['DBO_salida_mg_L'].mean()),
        'std_dbo_salida': float(df['DBO_salida_mg_L'].std()),
        'columnas_procesadas': list(df.columns)
    }
    serializar_procesador(pipeline_artefacto)
    
    print("Pipeline procesado con éxito. Archivos generados en outputs/")

if __name__ == '__main__':
    ejecutar_pipeline()