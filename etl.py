import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime
import os

def extract_data():
    """Simula extração de dados de múltiplas fontes - VERSÃO CORRIGIDA"""
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', '2024-01-01', freq='D')
    n_records = len(dates)  # Isso evita erro de tamanho
    
    print(f"📅 Criando {n_records} registros...")
    
    # CORREÇÃO: Garantir que todos os arrays tenham o mesmo tamanho
    sales_data = pd.DataFrame({
        'date': dates,
        'product_id': np.random.choice(['A', 'B', 'C', 'D'], size=n_records),
        'category': np.random.choice(['Eletrônicos', 'Roupas', 'Casa'], size=n_records),
        'sales': np.random.normal(1000, 200, size=n_records),
        'customers': np.random.poisson(50, size=n_records),
        'region': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], size=n_records)
    })
    
    # Adicionar sazonalidade CORRETAMENTE
    sales_data['sales'] = sales_data['sales'] * (
        1 + 0.3 * np.sin(2 * np.pi * sales_data.index / 365)
    )
    
    return sales_data

def transform_data(df):
    """Transformação e feature engineering - VERSÃO CORRIGIDA"""
    print("🔄 Transformando dados...")
    
    # Garantir que a coluna date é datetime
    df['date'] = pd.to_datetime(df['date'])
    
    df['month'] = df['date'].dt.month
    df['day_of_week'] = df['date'].dt.day_name()
    df['weekend'] = df['day_of_week'].isin(['Saturday', 'Sunday'])
    df['sales_category'] = pd.cut(df['sales'], 
                                 bins=[0, 800, 1200, np.inf],
                                 labels=['Baixo', 'Médio', 'Alto'])
    
    # Calcular métricas rolling de forma segura
    def safe_rolling(x):
        try:
            return x.rolling(window=7, min_periods=1).mean()
        except Exception as e:
            print(f"Erro no rolling: {e}")
            return x
    
    df['sales_7d_avg'] = df.groupby('product_id')['sales'].transform(safe_rolling)
    
    return df

def load_data(df):
    """Salvar dados para R e criar database - VERSÃO CORRIGIDA"""
    print("💾 Salvando dados...")
    
    # Garantir que o diretório existe
    os.makedirs('data', exist_ok=True)
    
    try:
        # Salvar CSV para R
        df.to_csv('data/processed_sales.csv', index=False)
        print("✅ CSV salvo com sucesso!")
        
        # Salvar em SQLite
        conn = sqlite3.connect('data/sales_database.db')
        df.to_sql('sales', conn, if_exists='replace', index=False)
        conn.close()
        print("✅ Database SQLite salvo!")
        
        # Salvar metadados
        metadata = {
            'last_update': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'total_records': len(df),
            'date_range': f"{df['date'].min()} to {df['date'].max()}"
        }
        
        print("✅ Dados processados e salvos!")
        print(f"📊 Total de registros: {len(df)}")
        print(f"📅 Período: {df['date'].min()} to {df['date'].max()}")
        
        return metadata
        
    except Exception as e:
        print(f"❌ Erro ao salvar dados: {e}")
        return None

if __name__ == "__main__":
    print("🚀 Iniciando pipeline ETL...")
    
    try:
        # Pipeline completo
        raw_data = extract_data()
        print(f"✅ Dados extraídos: {len(raw_data)} registros")
        
        processed_data = transform_data(raw_data)
        print(f"✅ Dados transformados: {len(processed_data)} registros")
        
        metadata = load_data(processed_data)
        
        if metadata:
            print("🎉 Pipeline ETL concluído com sucesso!")
        else:
            print("💥 Pipeline ETL falhou!")
            
    except Exception as e:
        print(f"💥 Erro no pipeline: {e}")
        import traceback
        traceback.print_exc()