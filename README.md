📊 Dashboard  Python + R - Análise de Vendas
https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/R-4.0%252B-blue
https://img.shields.io/badge/Streamlit-1.28%252B-red
https://img.shields.io/badge/License-MIT-green

Um projeto completo de ciência de dados que integra Python e R para análise preditiva de vendas com dashboard interativo.

🚀 Visão Geral
Este projeto demonstra uma integração perfeita entre Python e R, aproveitando os pontos fortes de cada linguagem:

Python: ETL, machine learning e dashboard web

R: Análise estatística avançada e modelagem de séries temporais

Integração: Troca de dados via JSON/CSV/SQLite

📋 Funcionalidades
🔧 Processamento de Dados
Extração: Geração de dados sintéticos de vendas

Transformação: Feature engineering e limpeza de dados

Carga: Armazenamento em múltiplos formatos (CSV, SQLite)

📈 Análise Estatística (R)
Análise descritiva e testes estatísticos (ANOVA, correlação)

Modelagem de séries temporais com ARIMA

Previsão de vendas para os próximos 30 dias

Análise regional e segmentação de mercado

🎨 Dashboard Interativo (Streamlit)
KPIs em tempo real

Visualizações interativas com Plotly

Previsões de vendas

Filtros dinâmicos por categoria e região

Download de dados processados

🏗 Arquitetura do Projeto
text
sales_analysis/
├── 01_python_etl.py          # Pipeline de ETL
├── 02_r_analysis.R           # Análise estatística
├── 03_python_dashboard.py    # Dashboard Streamlit
├── run_pipeline.py           # Orquestrador principal
├── requirements.txt          # Dependências Python
├── data/                     # Dados processados
│   ├── processed_sales.csv
│   ├── sales_database.db 
└── README.md
⚙️ Instalação e Configuração
Pré-requisitos
Python 3.8+

R 4.0+

Git

1. Clone o Repositório
bash
git clone https://github.com/seu-usuario/sales-analysis-dashboard.git
cd sales-analysis-dashboard
2. Configuração do Python
bash
# Criar ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
3. Configuração do R
r
# Instalar pacotes necessários
install.packages(c(
  "tidyverse", 
  "forecast", 
  "jsonlite", 
  "lubridate", 
  "broom",
  "cluster",
  "factoextra"
))
🚀 Como Executar
Opção 1: Pipeline Completo
bash
python run_pipeline.py
Opção 2: Execução Manual
bash
# 1. Processamento de dados com Python
python 01_python_etl.py

# 2. Análise estatística com R
Rscript 02_r_analysis.R

# 3. Executar dashboard
streamlit run 03_python_dashboard.py
Opção 3: Docker (Recomendado para produção)
bash
# Build da imagem
docker build -t sales-dashboard .

# Executar container
docker run -p 8501:8501 sales-dashboard
📊 Funcionalidades do Dashboard
🎯 KPIs Principais
Vendas totais

Ticket médio

Total de clientes

Correlação vendas/clientes

📈 Visualizações
Vendas por categoria: Gráfico de pizza

Séries temporais: Tendência de vendas ao longo do tempo

Previsões: Modelo ARIMA para próximos 30 dias

Análise regional: Market share por região

🔍 Filtros Interativos
Seleção por categoria de produtos

Filtro por região geográfica

Período personalizado

🛠 Tecnologias Utilizadas
Python
pandas - Manipulação de dados

numpy - Computação numérica

streamlit - Dashboard web

plotly - Visualizações interativas

sqlite3 - Banco de dados embutido

R
tidyverse - Manipulação e visualização de dados

forecast - Modelagem de séries temporais

lubridate - Manipulação de datas

broom - Tidy model outputs

📁 Estrutura de Dados
Schema dos Dados
Coluna	Tipo	Descrição
date	datetime	Data da venda
product_id	string	ID do produto (A-D)
category	string	Categoria do produto
sales	float	Valor da venda
customers	int	Número de clientes
region	string	Região geográfica
Arquivos Gerados
processed_sales.csv - Dados processados

sales_database.db - Banco SQLite



🧪 Exemplos de Uso
Para Empresas de Varejo
Previsão de demanda sazonal

Identificação de tendências de mercado

Otimização de estoque

Para Equipes de Marketing
Segmentação de clientes

Análise de performance por região

Planejamento de campanhas

Para Analistas de Dados
Template de integração Python/R

Exemplos de modelagem estatística

Dashboard replicável

🤝 Contribuindo
Contribuições são bem-vindas! Siga estos passos:

Fork o projeto

Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)

Commit suas mudanças (git commit -m 'Add some AmazingFeature')

Push para a branch (git push origin feature/AmazingFeature)

Abra um Pull Request

📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

👥 Autores
Victor Souza - github.com/Vitinzkx7

🙋‍♂️ Suporte
Se você encontrar algum problema ou tiver dúvidas:

Verifique as Issues

Crie uma nova issue descrevendo o problema

Entre em contato: victornex2006@hotmail.com

🔄 Próximas Atualizações
Integração com APIs de e-commerce

Modelos de machine learning adicionais

Autenticação de usuários

Relatórios automatizados

Deploy em cloud (AWS/Azure)

📚 Recursos Adicionais
Documentação
Streamlit Documentation

Tidyverse Documentation

Pandas Documentation

Artigos Relacionados
Integração Python e R

Dashboard com Streamlit

⭐ Se este projeto foi útil, deixe uma estrela no repositório!

<div align="center">
Desenvolvido usando as Linguagens Python e R

https://img.shields.io/badge/Made%2520with-Python-1f425f.svg
https://img.shields.io/badge/Made%2520with-R-276DC3.svg
https://img.shields.io/badge/Made%2520with-Streamlit-FF4B4B.svg

</div>
🎯 Quick Start
bash
# Clone e execute em 3 comandos:
git clone https://github.com/seu-usuario/sales-analysis-dashboard.git
cd sales-analysis-dashboard
python run_pipeline.py
O dashboard estará disponível em http://localhost:8501 🎉

