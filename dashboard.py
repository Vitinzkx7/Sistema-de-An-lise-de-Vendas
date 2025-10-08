import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
from datetime import datetime

# Configurar página
st.set_page_config(
    page_title="Dashboard de Vendas",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    """Carregar dados processados"""
    df = pd.read_csv('data/processed_sales.csv')
    df['date'] = pd.to_datetime(df['date'])
    
    with open('data/r_analysis_results.json', 'r') as f:
        r_results = json.load(f)
    
    return df, r_results

def create_kpi_cards(df, r_results):
    """Criar cards de KPI"""
    st.header("📈 KPIs Principais")
    
    col1, col2, col3, col4 = st.columns(4)
    
    total_sales = df['sales'].sum()
    avg_sales = df['sales'].mean()
    total_customers = df['customers'].sum()
    correlation = r_results['descriptive']['correlation']
    
    with col1:
        st.metric("Vendas Totais", f"R$ {total_sales:,.0f}")
    with col2:
        st.metric("Ticket Médio", f"R$ {avg_sales:.2f}")
    with col3:
        st.metric("Total Clientes", f"{total_customers:,.0f}")
    with col4:
        st.metric("Correlação Vendas/Clientes", f"{correlation:.3f}")

def create_sales_visualizations(df, r_results):
    """Criar visualizações de vendas"""
    st.header("📊 Análise de Vendas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Vendas por categoria
        sales_by_category = df.groupby('category')['sales'].sum().reset_index()
        fig1 = px.pie(sales_by_category, values='sales', names='category', 
                     title='Vendas por Categoria')
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Vendas ao longo do tempo
        daily_sales = df.groupby('date')['sales'].sum().reset_index()
        fig2 = px.line(daily_sales, x='date', y='sales', 
                      title='Vendas Diárias ao Longo do Tempo')
        st.plotly_chart(fig2, use_container_width=True)
    
    # Forecast from R
    st.subheader("Previsão de Vendas (Próximos 30 dias)")
    forecast_data = r_results['time_series']
    
    future_dates = pd.date_range(
        start=df['date'].max() + pd.Timedelta(days=1),
        periods=30,
        freq='D'
    )
    
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=df['date'], y=df.groupby('date')['sales'].sum(),
        name='Vendas Históricas', line=dict(color='blue')
    ))
    fig3.add_trace(go.Scatter(
        x=future_dates, y=forecast_data['forecast_mean'],
        name='Previsão', line=dict(color='red', dash='dash')
    ))
    fig3.add_trace(go.Scatter(
        x=future_dates, y=forecast_data['forecast_upper'],
        fill=None, mode='lines', line=dict(color='red', width=0),
        showlegend=False
    ))
    fig3.add_trace(go.Scatter(
        x=future_dates, y=forecast_data['forecast_lower'],
        fill='tonexty', mode='lines', line=dict(color='red', width=0),
        name='Intervalo de Confiança'
    ))
    
    fig3.update_layout(title='Previsão de Vendas com ARIMA (R)')
    st.plotly_chart(fig3, use_container_width=True)

def create_regional_analysis(df, r_results):
    """Análise regional"""
    st.header("Análise Regional")
    
    regional_stats = pd.DataFrame(r_results['regional']['regional_stats'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = px.bar(regional_stats, x='region', y='total_sales',
                     title='Vendas Totais por Região')
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = px.pie(regional_stats, values='market_share', names='region',
                     title='Market Share por Região')
        st.plotly_chart(fig2, use_container_width=True)

def main():
    st.title("🚀 Dashboard  - Análise de Vendas")
    
    # Carregar dados
    df, r_results = load_data()
    
    # Sidebar com filtros
    st.sidebar.header("Filtros")
    categories = st.sidebar.multiselect(
        "Categorias:",
        options=df['category'].unique(),
        default=df['category'].unique()
    )
    
    regions = st.sidebar.multiselect(
        "Regiões:",
        options=df['region'].unique(),
        default=df['region'].unique()
    )
    
    # Aplicar filtros
    filtered_df = df[
        (df['category'].isin(categories)) & 
        (df['region'].isin(regions))
    ]
    
    # Seções do dashboard
    create_kpi_cards(filtered_df, r_results)
    create_sales_visualizations(filtered_df, r_results)
    create_regional_analysis(filtered_df, r_results)
    
    # Mostrar dados
    with st.expander("📋 Visualizar Dados"):
        st.dataframe(filtered_df)
        
    # Download de dados
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="dados_filtrados.csv",
        mime="text/csv"
    )

if __name__ == "__main__":
    main()