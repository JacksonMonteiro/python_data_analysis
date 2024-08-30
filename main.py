from src.data_loader import loadData
from src.processing import process
from src.visualization import plotBar, plotPie

def main(): 
    path = "assets/Clientes.xlsx"

    try:
        df = loadData(path)
        df.columns = df.columns.str.strip()
        
        metrics = process(df)

        plotBar(metrics['servicoFrequente'], 'Serviços com Mais Frequência', 'Serviço', 'Contagem')
        plotBar(metrics['parceiroFrequente'], 'Parceiros com Mais Frequência', 'Parceiro', 'Contagem')
        plotPie(metrics['nichoFrequente'], 'Distribuição dos Nichos')
    except Exception as e:
        print(f"Ocorreu um erro ao executar a aplicação: {e}")

if __name__ == "__main__":
    main()        