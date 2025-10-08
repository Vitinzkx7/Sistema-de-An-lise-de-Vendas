import subprocess
import sys
import os

def run_python_etl():
    """Executar ETL em Python"""
    print("🚀 Executando ETL em Python...")
    try:
        result = subprocess.run([sys.executable, "etl.py"], 
                              capture_output=True, text=True, check=True)
        print("✅ ETL Python concluído!")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("❌ Erro no ETL Python:")
        print(e.stderr)
        return False

def run_r_analysis():
    """Executar análise em R"""
    print("📊 Executando análise em R...")
    try:
        result = subprocess.run(["Rscript", "Análise Descritiva.R"], 
                              capture_output=True, text=True, check=True)
        print("✅ Análise R concluída!")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("❌ Erro na análise R:")
        print(e.stderr)
        return False

def run_dashboard():
    """Executar dashboard Streamlit"""
    print("🎨 Iniciando dashboard Streamlit...")
    try:
        # Para produção, use: streamlit run 03_python_dashboard.py --server.port 8501
        os.system("streamlit run 03_python_dashboard.py")
    except KeyboardInterrupt:
        print("🛑 Dashboard interrompido pelo usuário")

def main():
    """Pipeline completo"""
    print("PIPELINE COMPLETO")
    
    # Executar pipeline
    if run_python_etl() and run_r_analysis():
        print("\n🎯 Pipeline concluído! Iniciando dashboard...")
        run_dashboard()
    else:
        print("\n💥 Pipeline falhou!")

if __name__ == "__main__":
    main()