library(tidyverse)
library(lubridate)
library(broom)
library(forecast)
library(jsonlite)

# Função para análise descritiva
descriptive_analysis <- function(df) {
  cat(" ANÁLISE DESCRITIVA ")
  
  # Estatísticas sumárias
  summary_stats <- df %>%
    group_by(product_id, category) %>%
    summarise(
      total_sales = sum(sales),
      avg_sales = mean(sales),
      sd_sales = sd(sales),
      total_customers = sum(customers),
      .groups = 'drop'
    )
  
  # Teste ANOVA entre categorias
  anova_test <- aov(sales ~ category, data = df)
  anova_summary <- tidy(anova_test)
  
  # Correlação
  correlation <- cor(df$sales, df$customers)
  
  # Retornar resultados
  list(
    summary_stats = summary_stats,
    anova_pvalue = anova_summary$p.value[1],
    correlation = correlation,
    total_categories = n_distinct(df$category)
  )
}

# Função para análise temporal
time_series_analysis <- function(df) {
  cat(" ANÁLISE DE SÉRIES TEMPORAIS ")
  
  # Agregar por data
  daily_sales <- df %>%
    group_by(date) %>%
    summarise(daily_sales = sum(sales), .groups = 'drop')
  
  # Converter para série temporal
  ts_data <- ts(daily_sales$daily_sales, frequency = 7)
  
  # Decomposição
  decomposition <- stl(ts_data, s.window = "periodic")
  
  # Modelo de forecast
  forecast_model <- auto.arima(ts_data)
  future_forecast <- forecast(forecast_model, h = 30)
  
  list(
    decomposition = decomposition,
    forecast = future_forecast,
    model_summary = summary(forecast_model)
  )
}

# Função para análise de regiões
regional_analysis <- function(df) {
  cat("=== ANÁLISE REGIONAL ===\n")
  
  regional_stats <- df %>%
    group_by(region) %>%
    summarise(
      total_sales = sum(sales),
      market_share = total_sales / sum(df$sales),
      avg_customers = mean(customers),
      .groups = 'drop'
    )
  
  # Teste chi-quadrado para distribuição de produtos por região
  chi_test <- chisq.test(table(df$region, df$product_id))
  
  list(
    regional_stats = regional_stats,
    chi_square_pvalue = chi_test$p.value
  )
}

# Pipeline principal
main_analysis <- function() {
  # Ler dados do Python
  df <- read_csv("data/processed_sales.csv") %>%
    mutate(date = ymd(date))
  
  cat("📊 Iniciando análise")
  cat("📈 Total de registros:", nrow(df), "\n")
  
  # Executar análises
  desc_analysis <- descriptive_analysis(df)
  ts_analysis <- time_series_analysis(df)
  reg_analysis <- regional_analysis(df)
  
  # Salvar resultados para Python
  results <- list(
    descriptive = desc_analysis,
    time_series = list(
      forecast_mean = as.numeric(ts_analysis$forecast$mean),
      forecast_lower = as.numeric(ts_analysis$forecast$lower[,2]),
      forecast_upper = as.numeric(ts_analysis$forecast$upper[,2])
    ),
    regional = reg_analysis,
    metadata = list(
      analysis_date = Sys.time(),
      records_processed = nrow(df)
    )
  )
  
  # Salvar resultados em JSON
  write_json(results, "data/r_analysis_results.json", pretty = TRUE)
  
  cat("✅ Análise R concluída! Resultados salvos em JSON.\n")
  
  return(results)
}

# Executar análise
if (interactive()) {
  analysis_results <- main_analysis()
}